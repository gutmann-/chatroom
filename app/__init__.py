from flask import Flask, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)

@app.route("/")
def index():
    return redirect('/static/index.html?user=user&room=room')

flask_app = app

from app.server import run_socketio_server
import app.models
from app.handlers import rooms

flask_app.register_blueprint(rooms)

db.create_all()
