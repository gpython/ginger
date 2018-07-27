request.json        =>以json形式发送过来的数据
request.method      =>请求方法(GET POST)
request.full_path   =>请求的完整路径 包括?后边参数
request.endpoint    =>当前请求 要访问的视图函数


HTTPBasasicAuth
from flask_httpauth import HTTPBasicAuth

auth = HTTPBasicAuth()

@auth.verify_password  #自动传入 account 和 password 参数值
def verify_password(account, password):
  pass

  #可以将token作为account password为空 传入进来
  #反解token 来确认token的正确性




视图函数中添加 登录认证装饰器 只有登录过的用户才能够访问此URL
@app.route('/')
@auth.login_required       #执行此装饰器时需要
def get_user():            #先执行被auth.verify_password装饰的函数
  pass

当请求 执行到被@auth.login_required装饰的函数时
会先执行被@auth.verify_password装饰的函数 以此函数返回结果确定时候要
执行后续视图函数
HTTPBasicAuth 发送账号密码 形式为 http头形式
key = Authorization
value = basic base64(username:password)

类变量 不会存储到__dict__中


请求token中 包含不同用户对用的不同权限类  不同权限类中包含各种可以请求访问的视图函数
request.endpoint 获得到用户请求的视图函数

                SuperScope  {View_A View_B View_C ..}

token           AdminScope  {View_A View_B ..}

                UserScope   {View_A ..}

globals() 当前模块下所有变量 包括当前的所有类都变成一个字典
key 为 字符串形式 value 为对象类型

