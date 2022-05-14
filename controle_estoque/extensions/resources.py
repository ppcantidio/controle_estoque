from flask_restful import Api
from dynaconf import settings

Api = Api()

def init_app(app):
    api = Api(app)
    
    #IMPORTANDO RESOURCES
    from controle_estoque.api.resources.produto_resources import ProdutoResource

    # REGISTRANDO RESOURCES
    BASE_PATH_URL = settings['BASE_PATH_URL']

    api.add_resource(ProdutoResource, f'{BASE_PATH_URL}/produto')
