#encoding:utf-8
from flask import request

from app.libs.enums import ClientTypeEnum
from app.libs.error_code import ClientTypeError, Success
from app.libs.redprint import Redprint
from app.models.user import User
from app.validators.forms import ClientForm, UserEmailForm
from werkzeug.exceptions import HTTPException

api = Redprint('client')

@api.route('/register', methods=['POST'])
def create_client():
  #直接获取客户端发送过来的json数据
  #data = request.json
  #print('client requrst.json = ', type(data), 'value = ', data)
  #1/0
  form = ClientForm().validate_for_api()

  promise = {
    ClientTypeEnum.USER_EMAIL: __register_user_by_email,
  }
  promise[form.type.data]()

  return Success()

def __register_user_by_email():
  form = UserEmailForm().validate_for_api()
  #if form.validate_for_api():
  User.register_by_email(form.nickname.data,
                        form.account.data,
                        form.secret.data)
