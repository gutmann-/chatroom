from flask_socketio import SocketIO, send, emit, join_room, leave_room

from app import app

socketio = SocketIO(app)

@socketio.on('join', namespace='/chat')
def on_join(data):
    username = data['username']
    room = data['room']
    join_room(room)
    emit('enter', {'room': room, 'username': username}, room=room)
    #send(username + ' has entered the room.', room=room)

@socketio.on('leave', namespace='/chat')
def on_leave(data):
    username = data['username']
    room = data['room']
    leave_room(room)
    #send(username + ' has left the room.', room=room)

@socketio.on('message', namespace='/chat')
def on_message(data):
    username = data['username']
    room = data['room']
    emit('message', data, room=room)

def run_socketio_server():
    socketio.run(app)
