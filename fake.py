#encoding:utf-8

from app import create_app
from app.models.base import db
from app.models.user import User

app = create_app()

with app.app_context():
  with db.auto_commit():
    #离线脚本 创建超级管理员帐户
    user =  User()
    user.nickname = 'super'
    user.password = '123456'
    user.email = '999@gamil.com'
    user.auth = 2
    db.session.add(user)