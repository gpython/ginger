#encoding:utf-8
from app.libs.error import APIException


class Success(APIException):
  code = 201
  msg = 'Success'
  error_code = 0

class ClientTypeError(APIException):
  code = 400
  msg = 'Client Type Error'
  error_code = 1000

class ParameterException(APIException):
  code = 400
  msg = 'invalid parameterexception'
  error_code = 1000


class NotFoundException(APIException):
  code = 404
  msg = 'the resource is not found'
  error_code = 1001

class AuthException(APIException):
  code = 401
  msg = ''
  error_code = 1002

