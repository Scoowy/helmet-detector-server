from flask import Blueprint
from app.server.responses.genericResponses import genericResponse

genericRoutes = Blueprint('genericRoutes', __name__)


@genericRoutes.get('/')
def index():
    return genericResponse('IA Project - Helmet detection')


@genericRoutes.get('/ping')
def ping():
    return genericResponse('Ok API is correct!')
