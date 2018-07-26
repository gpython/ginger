
class ClientForm(Form):
  account = StringField(validators=[DataRequired(), length(min=6, max=32)])
  secret = StringField()
  type = IntegerField(validators=[DataRequired()])

  #form校验时 立即执行此函数  校验type字段
  #value.data 存储 validate_之后相关字段的值

  def validate_type(self, value):
    pass

form = ClientForm(request.json)
form.validate()

form.validate() 执行校验时 会自动执行Form表单中 相应字段的 validate_表单字段() 函数
传入的value 参数 中 value.data 为相应字段的值

form.validate() 执行校验失败时 form.errors 中记录具体的错误信息
校验不通过时 须自行抛出异常
