from marshmallow import validate
from controle_estoque.api.utils.messages import MSG_INVALID_DATE


VALIDATE_DATE_REGEX = r"[0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}:[0-9]{2}(.[0-9]+|)"

MARSHMALLOW_VALIDATE_DATE = validate.Regexp(VALIDATE_DATE_REGEX, error=MSG_INVALID_DATE)
