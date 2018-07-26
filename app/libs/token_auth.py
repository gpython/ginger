#encoding:utf-8
from collections import namedtuple

from flask import current_app, g
from flask_httpauth import HTTPBasicAuth
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer, BadSignature, SignatureExpired

from app.libs.error_code import AuthException

auth = HTTPBasicAuth()
User = namedtuple('User', ['uid', 'ac_type', 'scope'])


@auth.verify_password
def verify_password(account, password):
  #token
  #HTTP账号密码 存储在http头中发送过来
  #header key:value
  #key=Authorization
  #value=basic base64(account:password)
  print(account)
  user_info = verify_auth_token(account)
  if not user_info:
    return False
  else:
    g.user = user_info
    return True


def verify_auth_token(token):
  s = Serializer(current_app.config['SECRET_KEY'])
  try:
    data = s.loads(token)
  except BadSignature:
    raise AuthException(msg='token is invalid',
                        error_code = 1002)
  except SignatureExpired:
    raise AuthException(msg='token is expired',
                        error_code = 1003)
  uid = data['uid']
  ac_type = data['type']
  return User(uid, ac_type, '')
