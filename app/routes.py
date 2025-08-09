import os
import uuid
from flask import Blueprint, render_template, request
from .services import process_image
from . import socketio

bp = Blueprint("main", __name__)

UPLOAD_FOLDER = "app/static/uploads"
PROCESSED_FOLDER = "app/static/processed"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(PROCESSED_FOLDER, exist_ok=True)

@bp.route("/")
def index():
    return render_template("index.html")

@bp.route("/upload", methods=["POST"])
def upload():
    file = request.files["image"]
    if file:
        filename = f"{uuid.uuid4().hex}.jpg"
        filepath = os.path.join(UPLOAD_FOLDER, filename)
        file.save(filepath)

        processed_files = process_image(filepath, filename, PROCESSED_FOLDER)
        # Emit socket event so all clients update instantly
        socketio.emit("new_image", {"files" : processed_files})

    return {"status" : "ok"}

@bp.route("/gallery")
def gallery():
    images = os.listdir(PROCESSED_FOLDER)
    return render_template("gallery.html", images=images)