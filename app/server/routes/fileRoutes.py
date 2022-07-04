import os.path

from flask import Blueprint, request, send_from_directory

from app.config import OUTPUT_FOLDER
from app.server.responses.genericResponses import genericResponse
from app.lib.files.files import uploadFiles

fileRoutes = Blueprint('fileRoutes', __name__)


@fileRoutes.get('/<path:filename>')
def getFile(filename):
    return send_from_directory(os.path.abspath(OUTPUT_FOLDER), path=filename, as_attachment=False)


@fileRoutes.post('/upload')
def upload():
    # print(request.files)
    if request.method != 'POST':
        return genericResponse('Only POST method is allowe', 405)

    if 'file' not in request.files:
        return genericResponse('No file part', 400)

    files = request.files.getlist('file')

    if any([file.filename == '' for file in files]):
        return genericResponse('No file selected', 400)

    filepaths = uploadFiles(files)

    if not filepaths:
        return genericResponse('No file uploaded', 400)

    return genericResponse({'message': 'Ok', 'filepaths': filepaths})
