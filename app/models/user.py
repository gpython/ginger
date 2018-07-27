#encoding:utf-8
import datetime

from sqlalchemy import Column, Integer, SmallInteger, String
from werkzeug.security import generate_password_hash, check_password_hash

from app.libs.error_code import NotFoundException, AuthException
from app.models.base import db, Base



class User(Base):
  id = Column(Integer, primary_key=True)
  email = Column(String(24), unique=True, nullable=False)
  nickname = Column(String(24), unique=True)
  auth = Column(SmallInteger, default=1)
  time = datetime.date(2018, 7, 20)
  _password = Column('password', String(100))

  def keys(self):
    return ['id', 'email', 'nickname', 'auth', 'time']

  @property
  def password(self):
    return self._password

  @password.setter
  def password(self, raw):
    self._password = generate_password_hash(raw)

  @staticmethod
  def register_by_email(nickname, account, secret):
    with db.auto_commit():
      user = User()
      user.nickname = nickname
      user.email = account
      user.password = secret
      db.session.add(user)

  @staticmethod
  def verify(email, password):
    user = User.query.filter_by(email=email).first_or_404()

    if not user.check_password(password):
      raise AuthException(msg='Authenticate Error')
    scope = 'SuperScope' if user.auth == 2 else 'UserScope'
    return {'uid': user.id, 'scope': scope}

  def check_password(self, raw):
    if not raw:
      return False
    return check_password_hash(self._password, raw)
