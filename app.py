import os

from flask import Flask
from flask_cors import CORS
from flask_socketio import SocketIO

from app.config import TEMP_FILES_DIR
from app.files.directories import createDirectory
from app.files.files import INPUT_FOLDER, OUTPUT_FOLDER
from app.routes import genericRoutes, fileRoutes, yoloRoutes

# Declare temporary files directory
TEMP_FILES_INPUT_DIR = os.path.join(TEMP_FILES_DIR, 'input')

# Create temporary file directories
createDirectory(INPUT_FOLDER, deleteContent=True)
createDirectory(OUTPUT_FOLDER, deleteContent=True)

# Create flask app
app = Flask(__name__)
CORS(app)
socketio = SocketIO(app)

# Register routes
app.register_blueprint(genericRoutes)
app.register_blueprint(fileRoutes, url_prefix='/api/v1/files')
app.register_blueprint(yoloRoutes, url_prefix='/api/v1/predict')


if __name__ == '__main__':
    # app.run(debug=True, host='0.0.0.0', port=8000)
    socketio.run(app, debug=True, host='127.0.0.1', port=8000)
