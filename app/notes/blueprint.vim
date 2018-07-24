#encoding:utf-8

                 app


蓝图        蓝图        蓝图        蓝图


静态文件    静态文件     ...
视图函数    试图函数
模板文件    模板文件


视图函数注册到蓝图上  要想使蓝图生效 还要将蓝图注册到app的核心对象上
蓝图是模块级别的拆分

##############################################################
Flask核心对象           app


蓝图层         v1_user             v1_book


视图函数      get_user()            get_book()
             create_user()         create_book()

视图函数 注册到 蓝图层 再将蓝图层 注册到 Flask核心对象app

view_func -> Blueprint -> Flask_app


#######View_func -> Blueprint##########
from flask import Blueprint

user = Blueprint('user', __name__)

@user.route('/user')
def get_user():
  return 'User...'

######Blueprint -> app#####
from flask import Flask
from view_func import user

app = Flask(__name__)
app.register_blueprint(user)
##############################



##############################################################
新添加一层 Redprint

        Flask核心对象   flask_app

        蓝图层             v1

        Redprint     book   user  other

        视图函数      get_book  get_user create_user ....

view_func -> Redprint -> Blueprint -> Flask_app


#################Redpoint##############
class Redpoint:
  def __init__(self, name):
    self.name = name
    self.mound = []

  def route(self, rule, **options):
    def decorator(f):
      self.mound.append((f, rule, **options))
      print(f.__name__)
      return f
    return decorator

  def register(self, bp, url_prefix=None):
    if url_prefix is None:
      url_prefix = '/' + self.name

    for f, rule, options in self.mound:
      endpoint = options.pop('endpoint', f.__name__)
      bp.add_url_rule(url_prefix+rule, endpoint, **options)

########view_func->Redpoint#########
import Redpoint

user = Redpoint()
@user.route('/user', endpiont = 'user')
def get_user():
  return '....'

########Redpoint -> Blueprint####
from flask import Blueprint
from view_func import user

def register_blueprint():
  bp_v1 = Blueprint('v1', __name__)    <----------
  user.register(bp_v1)

  return bp_v1                         <----------

#####Blueprint -> app#####
from Blueprint import register_blueprint
from flask import Flask

app = Flask(__name__)
app.register_blueprint(register_blueprint(), url_prefix='/v1')
##############################






