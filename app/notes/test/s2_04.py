#encoding:utf-8
#关于 继承 变量寻找关系
#子类继承父类 若某个方法在父类中 子类执行此方法时 执行某个变量的操作
#此变量的寻找 (若此变量在父类中存在) 先从子类中寻找 若子类中没有 再去父类中寻找
#变量寻找关系 先从子类中寻找  再去父类中寻找

class Scope:
  # allow_api = ['v2.googogogoogogog']
  # def __init__(self):
  #   self.allow_api = ['v2.googogogoogogog']
  def __add__(self, other):
    #寻找allow_api 线路 先从继承此类的 子类当中寻找allow_api
    #若子类当中没有 allow_api 在从当前父类中寻找
    self.allow_api += other.allow_api
    return self

class UserScope(Scope):
  allow_api = ['v1.get_user']

class AdminScope(Scope):
  allow_api = ['v1.A']

  def __init__(self):
    self + UserScope
    print(self.allow_api)

class SuperScope(Scope):
  allow_api = ['v1.super_get_user']

  def __init__(self):
    #运算符重载 直接调用基类的 __add__
    self + AdminScope + UserScope
    print(self.allow_api)

AdminScope()
SuperScope()