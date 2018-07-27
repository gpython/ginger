#encoding:utf-8
from flask import jsonify, g

from app.libs.error_code import DeleteSuccess
from app.libs.redprint import Redprint
from app.libs.token_auth import auth
from app.models.base import db
from app.models.user import User

api = Redprint('user')

#super admin
@api.route('/<int:uid>', methods=['GET'])
@auth.login_required
def super_get_user(uid):
  user = User.query.filter_by(id=uid).first_or_404()
  return jsonify(user)

#super admin
@api.route('/<int:uid>', methods = ['DELETE'])
def supr_delete_user(uid):
  pass


#普通用户查询自己的信息
@api.route('', methods=['GET'])
@auth.login_required
def get_user():
  uid = g.user.id
  user = User.query.filter_by(id=uid).first_or_404()
  return jsonify(user)


@api.route('', methods=['DELETE'])
@auth.login_required
def delete_user():
  #用户只能注销自己的账户
  #g 线程隔离
  #uid 号在用户的令牌里
  uid = g.user.uid
  with db.auto_commit():
    user = User.query.filter_by(id=uid).first_or_404()
    user.delete()
  return DeleteSuccess()