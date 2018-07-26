#encoding:utf-8
from wtforms import StringField, IntegerField, ValidationError
from wtforms.validators import DataRequired, length, Email, Regexp

from app.libs.enums import ClientTypeEnum
from app.models.user import User
from app.validators.base import BaseForm as Form


class ClientForm(Form):
  account = StringField(validators=[DataRequired(), length(min=6, max=32)])
  secret = StringField()
  type = IntegerField(validators=[DataRequired()])

  #form校验时 立即执行此函数  校验type字段
  #value.data 存储 validate_之后相关字段的值
  def validate_type(self, value):
    try:
      print('即刻执行')
      print('value = ', value, type(value), value.data)
      #枚举类型 传入相关value数值 可以获得其key 字段值
      client = ClientTypeEnum(value.data)
      print('client = ', client)
    except ValueError as e:
      raise e

    #validate表单校验通过后 更改表单type的值
    self.type.data = client

    print('self.type = ', self.type, 'self.type.data = ', self.type.data)

    pass

class UserEmailForm(ClientForm):
  account = StringField(validators=[Email(message='invalidate email')])
  secret = StringField(validators=[DataRequired(), Regexp(r'^[A-Za-z0-9_~!@#$%^&*()<>]{6,22}$')])
  nickname = StringField(validators=[DataRequired(), length(min=2, max=22)])

  #表单校验 form.validate()校验时 立即执行此函数  校验相关字段
  def validate_account(self, value):
    print('validate_account = 即刻执行')
    if User.query.filter_by(email=value.data).first():
      raise ValidationError()