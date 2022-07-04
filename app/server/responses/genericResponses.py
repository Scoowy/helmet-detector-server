from flask import jsonify, Response


def genericResponse(data: any, statusCode=200) -> Response:
    if isinstance(data, str):
        return __genericMessageResponse(data, statusCode)

    if isinstance(data, dict):
        return __genericDictionaryResponse(data, statusCode)

    if isinstance(data, object):
        return __genericObjectResponse(data, statusCode)


def __genericMessageResponse(message: str, statusCode: int) -> Response:
    response = jsonify({'message': message})
    response.status_code = statusCode
    return response


def __genericObjectResponse(obj: object, statusCode: int) -> Response:
    response = jsonify({'data': obj})
    response.status_code = statusCode
    return response


def __genericDictionaryResponse(dictionary: dict, statusCode: int) -> Response:
    response = jsonify({'data': dictionary})
    response.status_code = statusCode
    return response
