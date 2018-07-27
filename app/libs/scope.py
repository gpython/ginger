#encoding:utf-8
import importlib


class SuperScope:
  allow_api = ['v1.super_get_user']

class UserScope:
  allow_api = ['v1.get_user']

def is_in_scope(scope, endpoint):
  cls = globals()[scope]
  print(cls.allow_api)
  print(endpoint)
  if endpoint in cls().allow_api:
    return True
  else:
    return False
