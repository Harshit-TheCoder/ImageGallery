from flask import Flask
from flask_socketio import SocketIO

socketio = SocketIO()

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'secret123'

    from .routes import bp
    app.register_blueprint(bp)
    socketio.init_app(app, cors_allowed_origins="*")
    return app