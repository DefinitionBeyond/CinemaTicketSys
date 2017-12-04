完整的目录在[这里]()。


# 使用说明

在MySQL中导入数据库:

    mysql -h127.0.0.1 -uroot -proot -Dtest -P3306 < key.sql

修改app.py，配置访问数据库的用户名、密码和端口号。

# TODO

* 密码加密
* 用户注册
* 以用户为维度，管理TodoList
