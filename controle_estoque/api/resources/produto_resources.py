from flask import request
from flask_restful import Resource
from controle_estoque.db.produto_db import ProdutoDB
from controle_estoque.api.utils.responses import resp_error, resp_ok
from controle_estoque.api.models.produto_models import ProdutoSchema


class ProdutoResource(Resource):
    def post(self):
        """
        Insere um produto novo na tabela
        """

        req_data = request.get_json()

        produto, erros = ProdutoSchema().load(req_data)
        if erros:
            resp_error('Produto', erros, 'Não foi possível inserir o produto')

        produto = ProdutoDB().inserir_produto(produto)

        return resp_ok('Produto', 'Produto inserido com sucesso!', produto)


    def get(self):
        pass
