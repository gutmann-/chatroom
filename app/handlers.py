from flask import Blueprint, jsonify
from app.models import Room

rooms = Blueprint('rooms', __name__, url_prefix='/rooms')

@rooms.route("/list")
def roomlist():
    rooms = Room.query.all()
    return jsonify({'rooms':
        [dict(id=r.id, name=r.name) for r in rooms]})
