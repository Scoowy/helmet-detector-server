from base64 import b64decode, b64encode
from io import StringIO, BytesIO

from PIL import Image


def decodeDataImage(dataImage: str) -> Image.Image | None:
    headers, data = dataImage.split(',')
    buffer = StringIO()
    buffer.write(data)

    bytesData = BytesIO(b64decode(data))

    try:
        img = Image.open(bytesData)
        return img
    except Exception as e:
        return None


def encodeDataImage(imgEncode) -> str:
    """
    Base64 encoding image for send via internet
    @param imgEncode: cv2.imencode() result
    """
    stringData = b64encode(imgEncode).decode('utf-8')
    return 'data:image/jpeg;base64,' + stringData
