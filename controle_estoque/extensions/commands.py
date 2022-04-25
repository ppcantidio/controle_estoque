import imp
from controle_estoque.resources.restapi.models import product
from controle_estoque.extensions.database import db


def create_db():
    db.create_all()


def init_app(app):
    print('t')
    app.cli.add_command(app.cli.command(create_db))
