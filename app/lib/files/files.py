import os
import uuid
import base64
from io import BytesIO
from PIL import Image

from werkzeug.datastructures import FileStorage

from app.config import INPUT_FOLDER, OUTPUT_FOLDER
from app.lib.files.directories import createDirectory


def __uploadFile(file: FileStorage) -> dict[str, str]:
    extensionFile = file.content_type.split('/')[-1]
    filename = str(uuid.uuid4()) + '.' + extensionFile
    filepath = os.path.join(INPUT_FOLDER, filename)

    file.save(filepath)

    return {'filename': filename, 'filepath': filepath}


def uploadFiles(files: list[FileStorage]) -> list[dict[str, str]]:
    createDirectory(INPUT_FOLDER, deleteContent=True)

    result = []

    for file in files:
        if file:
            result.append(__uploadFile(file))

    return result


def __encodeImg(filepath: str) -> str:
    img = Image.open(filepath, mode='r')
    buffered = BytesIO()
    img.save(buffered, format='JPEG')
    imgBase64 = base64.b64encode(buffered.getvalue()).decode('utf-8')

    return imgBase64


def encodeImgs(filepaths: list[str]) -> list[str]:
    result = []

    for filepath in filepaths:
        result.append(__encodeImg(filepath))

    return result


def __downloadFile(filename: str) -> str:
    filepath = os.path.join(OUTPUT_FOLDER, filename)
    img = __encodeImg(filepath)
    return img


def downloadFiles(filesnames: list[str]) -> list[str]:
    filepaths = [os.path.join(OUTPUT_FOLDER, filename)
                 for filename in filesnames]
    imgs = encodeImgs(filepaths)

    return imgs
