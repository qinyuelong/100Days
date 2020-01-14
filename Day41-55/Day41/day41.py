'''
https://github.com/jackfrued/Python-100-Days/blob/master/Day41-55/41.%E5%BF%AB%E9%80%9F%E4%B8%8A%E6%89%8B.md
'''


'''
进入项目文件夹，创建并激活虚拟环境
$ cd hellodjango
$ python3 -m venv venv
$ source venv/bin/activate

在虚拟环境下使用Python解释器和包管理工具时，对应的命令是python和pip，而不再需要键入python3和pip3
'''

'''
启动Django自带的服务器运行项目。
python manage.py runserver

在浏览器中输入http://127.0.0.1:8000访问我们的服务器，效果如下图所示


创建名为hrs（人力资源系统）的应用，一个Django项目可以包含一个或多个应用。
(venv)$ python manage.py startapp hrs

执行上面的命令会在当前路径下创建hrs目录，其目录结构如下所示：

__init__.py：一个空文件，告诉Python解释器这个目录应该被视为一个Python的包。
admin.py：可以用来注册模型，用于在Django的管理界面管理模型。
apps.py：当前应用的配置文件。
migrations：存放与模型有关的数据库迁移信息。
__init__.py：一个空文件，告诉Python解释器这个目录应该被视为一个Python的包。
models.py：存放应用的数据模型，即实体类及其之间的关系（MVC/MTV中的M）。
tests.py：包含测试应用各项功能的测试类和测试函数。
views.py：处理请求并返回响应的函数（MVC中的C，MTV中的V）。


'''