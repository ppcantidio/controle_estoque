from flask import jsonify
from controle_estoque.extensions.blueprints import bp_restapi


class Products:
    @bp_restapi.route('/products', methods=['POST'])
    def create_product():
        pass
