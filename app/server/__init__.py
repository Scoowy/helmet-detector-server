from flask import Blueprint
from app.server.routes.genericRoutes import genericRoutes
from app.server.routes.fileRoutes import fileRoutes
from app.server.routes.yoloRoutes import yoloRoutes

mainRoutes = Blueprint('mainRoutes', __name__)

mainRoutes.register_blueprint(genericRoutes)
mainRoutes.register_blueprint(fileRoutes, url_prefix='/api/v1/files')
mainRoutes.register_blueprint(yoloRoutes, url_prefix='/api/v1/predict')
# mainRoutes.register_blueprint(routes.socketRoutes, url_prefix='/api/v1/socket')
