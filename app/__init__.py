import warnings

from flask import Flask
from flask_cors import CORS
from flask_socketio import SocketIO

from app.config import INPUT_FOLDER, OUTPUT_FOLDER
from app.lib.files.directories import createDirectory

warnings.filterwarnings(
    "ignore", message="torch.distributed.reduce_op is deprecated")

# Declare temporary files directory
# TEMP_FILES_INPUT_DIR = os.path.join(TEMP_FILES_DIR, 'input')

# Create temporary file directories
createDirectory(INPUT_FOLDER, deleteContent=True)
createDirectory(OUTPUT_FOLDER, deleteContent=True)

socketio = SocketIO()


def createApp(debug=False) -> Flask:
    """Create an application."""
    app = Flask(__name__)
    CORS(app, origins=['http://localhost:3000'])
    app.debug = debug
    # app.config['SECRET_KEY'] = 'dagedascgs'

    from app.server import mainRoutes
    app.register_blueprint(mainRoutes)

    socketio.init_app(app, cors_allowed_origins="*")
    return app
