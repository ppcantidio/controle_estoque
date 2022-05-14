from marshmallow import Schema, validate
from marshmallow.fields import Str, Integer, Boolean, Nested, Decimal, List

from controle_estoque.api.utils.messages import MSG_FIELD_REQUIRED
from controle_estoque.api.utils.categorias_validate import MARSHMALLOW_VALIDATE_CATEGORYS
from controle_estoque.api.utils.date_validate import MARSHMALLOW_VALIDATE_DATE


class ProdutoSchema(Schema):
    nome = Str(required=True, error_messages={'required': MSG_FIELD_REQUIRED})
    categoria = Str(required=True, error_messages={'required': MSG_FIELD_REQUIRED}, validate=MARSHMALLOW_VALIDATE_CATEGORYS)
    data_validade = Str(required=True, error_messages={'required': MSG_FIELD_REQUIRED}, validate=MARSHMALLOW_VALIDATE_DATE)
    quantidade = Integer(required=True, error_messages={'required': MSG_FIELD_REQUIRED})
    valor = Decimal(required=True, error_messages={'required': MSG_FIELD_REQUIRED})
