from flask import jsonify
from controle_estoque.resources.restapi.blueprint import bp


class Products:
    @bp.route('/products', methods=['POST'])
    def create_product():
        pass