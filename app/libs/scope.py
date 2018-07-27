#encoding:utf-8
#关于 继承 变量寻找关系
#子类继承父类 若某个方法在父类中 子类执行此方法时 执行某个变量的操作
#此变量的寻找 (若此变量在父类中存在) 先从子类中寻找 若子类中没有 再去父类中寻找
#变量寻找关系 先从子类中寻找  再去父类中寻找

class Scope:
  allow_api = []
  allow_module = []
  forbidden = []

  def __add__(self, other):
    #寻找allow_api 线路 先从继承此类的 子类当中寻找allow_api
    #若子类当中没有 allow_api 在从当前父类中寻找
    self.allow_api += other.allow_api
    self.allow_api = list(set(self.allow_api))

    self.allow_module += other.allow_module
    self.allow_module = list(set(self.allow_module))

    self.forbidden += other.forbidden
    self.forbidden = list(set(self.forbidden))

    return self

class UserScope(Scope):
  forbidden = ['v1.user+super_get_user',
               'v1.user+super_delete_user']
  def __init__(self):
    self + AdminScope()

class AdminScope(Scope):
  allow_module = ['v1.user']

  def __init__(self):
    pass

class SuperScope(Scope):
  allow_module = ['v1.user']

  def __init__(self):
    #运算符重载 直接调用基类的 __add__
    pass

AdminScope()
SuperScope()

def is_in_scope(scope, endpoint):
  scope = globals()[scope]()
  splits = endpoint.split('+')
  red_name = splits[0]

  if endpoint in scope.forbidden:
    return False

  if endpoint in scope.allow_api:
    return True

  if red_name in scope.allow_module:
    return True
  else:
    return False
