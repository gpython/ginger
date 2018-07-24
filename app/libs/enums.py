#encoding:utf-8
from enum import Enum


#执行ClientTypeEnum(100) 返回 ClientTypeEnum.USER_EMAIL
#ClientTypeEnum(100).name   => 'USER_EMAIL'
#ClientTypeEnum(100).value  => 100
class ClientTypeEnum(Enum):
  USER_EMAIL = 100
  USER_MOBILE = 101

  USER_MINA = 200
  USER_WX = 201