from flask import render_template
from controle_estoque.extensions.blueprints import bp_web

def index():
    pass


bp_web.add_url_rule("/", view_func=index)
