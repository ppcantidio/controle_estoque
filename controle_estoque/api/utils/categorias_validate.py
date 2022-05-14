from marshmallow import validate
from controle_estoque.db.database import connection
from controle_estoque.api.utils.messages import MSG_INVALID_CATEGORY

dynamodb = connection()
_table = dynamodb.Table('categorias')

categorias = _table.scan()

categorias_list = []
for categoria in categorias :
    categorias_list.append(categoria['categoria'])

MARSHMALLOW_VALIDATE_CATEGORYS = validate.ContainsOnly(iterable=categorias_list, error=MSG_INVALID_CATEGORY)
