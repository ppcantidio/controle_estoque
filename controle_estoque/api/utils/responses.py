from flask import jsonify
from controle_estoque.api.utils.messages import MSG_INVALID_DATA, MSG_SUCCESS


def resp_error(resource: str, errors: object, msg: str = MSG_INVALID_DATA):
    '''
    Responses 400
    '''

    if not isinstance(resource, str):
        raise ValueError('O recurso precisa ser uma string.')

    resp = jsonify({
        'resource': resource,
        'message': msg,
        'errors': errors,
    })

    resp.status_code = 400

    return resp


def resp_ok(resource: str, message: str, data=None):
    '''
    Responses 200
    '''
    if not resource:
        resource = ''

    if not message:
        message = MSG_SUCCESS

    response = {'status': 200, 'message': message, 'resource': resource}

    if data:
        response['dados'] = data

    resp = jsonify(response)
    resp.status_code = 200

    return resp