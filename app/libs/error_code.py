#encoding:utf-8
from app.libs.error import APIException


class Success(APIException):
  code = 201
  error_code = 0
  msg = 'Success'


class DeleteSuccess(APIException):
  code = 202
  error_code = 1
  msg = 'Delete Success'

class ClientTypeError(APIException):
  code = 400
  error_code = 1000
  msg = 'Client Type Error'


class ParameterException(APIException):
  code = 400
  error_code = 1000
  msg = 'Invalid Parameterexception'



class NotFoundException(APIException):
  code = 404
  error_code = 1001
  msg = 'The Resource Is Not Found'

class AuthException(APIException):
  #授权失败
  code = 401
  error_code = 1002
  msg = ''

class Forbidden(APIException):
  #禁止访问 权限不够
  code = 403
  error_code = 1004
  msg = 'Forbidden not in scope'

