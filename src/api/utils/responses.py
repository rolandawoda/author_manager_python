from flask import make_response

INVALID_FIELD_NAME_SENT_422 = {
    "http_code": 422,
    "code": "invalidField",
    "message": "Invalid fields found"
}
INVALID_INPUT_422 = {
    "http_code": 422,
    "code": "invalidInput",
    "message": "Invalid input"
}
MISSING_PARAMETERS_422 = {
    "http_code": 422,
    "code": "missingParameter",
    "message": "Missing parameters."
}
BAD_REQUEST_400 = {
    "http_code": 400,
    "code": "badRequest",
    "message": "Bad request"
}
SERVER_ERROR_500 = {
    "http_code": 500,
    "code": "serverError",
    "message": "Server error"
}
SERVER_ERROR_404 = {
    "http_code": 404,
    "code": "notFound",
    "message": "Resource not found"
}
SERVER_ERROR_401 = {
    "http_code": 401,
    "code": "notAuthourized",
    "message": "valid authentication credentials"
}
UNAUTHORIZED_403 = {
    "http_code": 403,
    "code": "notAuthorized",
    "message": "You are not authorised to execute this."
}

UNAUTHORIZED_401 = {
    "http_code": 401,
    "code": "notAuthorized",
    "message": "User could not be found"
}

SUCCESS_200 = {
    'http_code': 200,
    'code': 'success'
}
SUCCESS_201 = {
    'http_code': 201,
    'code': 'success'
}
SUCCESS_204 = {
    'http_code': 204,
    'code': 'success'
}


def response_with(response, value=None, message=None, error=None, headers={}, pagination=None):
    result = {}
    if value is not None:
        result.update(value)
    if response.get('message', None) is not None:
        result.update({'message': response['message']})
        result.update({'code': response['code']})
    if error is not None:
        result.update({'errors': error})
    if pagination is not None:
        result.update({'pagination': pagination})
    headers.update({'Access-Control-Allow-Origin': '*'})
    headers.update({'server': 'Flask REST API'})
    return make_response(result, response['http_code'], headers)
