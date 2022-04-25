from flask import Blueprint


bp_restapi = Blueprint("restapi", __name__, url_prefix="/api/v1")
bp_web = Blueprint("web", __name__, template_folder="templates")


def init_app(app):
    app.register_blueprint(bp_restapi)
    app.register_blueprint(bp_web)
