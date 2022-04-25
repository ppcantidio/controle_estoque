from flask import Blueprint


bp = Blueprint("restapi", __name__, url_prefix="/api/v1")


def init_app(app):
    app.register_blueprint(bp)