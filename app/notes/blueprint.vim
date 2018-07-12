#encoding:utf-8

                 app


蓝图        蓝图        蓝图        蓝图


静态文件    静态文件     ...
视图函数    试图函数
模板文件    模板文件


视图函数注册到蓝图上  要想使蓝图生效 还要将蓝图注册到app的核心对象上
蓝图是模块级别的拆分

##############################################################
Flask核心对象           app


蓝图层         v1_user             v1_book


视图函数      get_user()            get_book()
             create_user()         create_book()

视图函数 注册到 蓝图层 再将蓝图层 注册到 Flask核心对象app

view_func -> Blueprint -> Flask_app

##############################################################
新添加一层 Redprint

        Flask核心对象   flask_app

        蓝图层             v1

        Redprint     book   user  other

        视图函数      get_book  get_user create_user ....

view_func -> Redprint -> Blueprint -> Flask_app