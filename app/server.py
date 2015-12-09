from flask_socketio import SocketIO, send, emit, join_room, leave_room
from flask import request

from app import app, db
from app.models import User, Room, Message

socketio = SocketIO(app)

def get_or_create(Cls, **kw):
    o = Cls.query.filter_by(**kw).first()
    if o is None:
        o = Cls(**kw)
        db.session.add(o)
    return o

def send_room_history(room):
    messages = room.messages                        \
            .order_by(Message.id.asc())             \
            .all()

    for message in messages:
        data = dict(username=message.user.name,
                    room=room.id, text=message.text)
        emit('message', data, room=request.sid)

@socketio.on('join', namespace='/chat')
def on_join(data):
    username = data['username']

    user = get_or_create(User, name=username)
    room = get_or_create(Room, name=data['room'])
    if not user in room.users:
        room.users.append(user)
        db.session.merge(room)
        db.session.commit()

    join_room(room.id)

    send_room_history(room)
    emit('enter', {'room': room.id, 'username': username}, room=room.id)

@socketio.on('leave', namespace='/chat')
def on_leave(data):
    username = data['username']

    user = get_or_create(User, name=username)
    room = get_or_create(Room, name=data['room'])

    if user in room.users:
        room.users.remove(user)
        db.session.commit()

    leave_room(room.id)

@socketio.on('message', namespace='/chat')
def on_message(data):
    username = data['username']

    user = get_or_create(User, name=username)
    room = get_or_create(Room, name=data['room'])

    message = Message(data['text'])
    user.messages.append(message)
    room.messages.append(message)
    db.session.commit()

    emit('message', data, room=room.id)

def run_socketio_server():
    socketio.run(app)
