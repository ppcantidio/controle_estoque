from controle_estoque.db.database import connection


class ProdutoDB:
    def __init__(self):
        self.dynamodb = connection()
        self.tabela = self.dynamodb.Table('produtos')

    
    def inserir_produto(self, produto):
        retorno = self.tabela.put_item(
            Item=produto
        )

        return retorno

