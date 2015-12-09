from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True)
    messages = db.relationship('Message', backref='user',
                               lazy='dynamic')

    def __init__(self, name):
        self.name = name

user_in_room = db.Table('user_in_room',
        db.Column('user_id', db.Integer, db.ForeignKey('user.id')),
        db.Column('room_id', db.Integer, db.ForeignKey('room.id')),

        db.UniqueConstraint('user_id', 'room_id', name='uix_1')
)

class Room(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True)
    messages = db.relationship('Message', backref='room',
                               lazy='dynamic')
    users = db.relationship('User', secondary=user_in_room,
                    backref=db.backref('rooms', lazy='dynamic'))

    def __init__(self, name):
        self.name = name

class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    room_id = db.Column(db.Integer, db.ForeignKey('room.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    text = db.Column(db.String(1024))

    def __init__(self, text):
        self.text = text

