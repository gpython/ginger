#encoding:utf-8
from datetime import date

from flask import Flask as _Flask
from flask.json import JSONEncoder as _JSONEncoder

class JSONEncoder(_JSONEncoder):
  #递归调用 只要遇到不能序列化的对象都会递归调用此default方法
  def default(self, o):
    if hasattr(o, 'keys') and hasattr(o, '__getitem__'):
      return dict(o)
    if isinstance(o, date):
      return o.strftime("%Y-%m-%d %H:%M:%S")
    return super(JSONEncoder, self).default(o)


class Flask(_Flask):
  json_encoder = JSONEncoder
  pass


