"""
Python 类型提示 - 类对象的类型

https://docs.python.org/zh-cn/3.13/library/typing.html#the-type-of-class-objects

@author: shiloh
@date: 2025/1/13 11:34
"""

# 标注了 int 类型的变量，可以接收 int 类型的值
# 变量 a 的类型为 int
a: int = 3
# 变量 b 的类型为 type(int)，类型放到 type() 里面，代表它可以接收本身是类的值，比如 int 类的对象
b = int
# 变量 c 的类型为 type(int)
c = type(a)


# type(类型) 协变，举例：
class User:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age


class BasicUser(User):
    def __init__(self, name: str, age: int):
        super().__init__(name, age)


class ProUser(User):
    def __init__(self, name: str, age: int, pro_level: int):
        super().__init__(name, age)
        self.pro_level = pro_level


class TeamUser(User):
    def __init__(self, name: str, age: int, team_id: int):
        super().__init__(name, age)
        self.team_id = team_id


# 模拟创建用户
def make_new_user(user_class: type[BasicUser | ProUser]):
    """
    注意：type[类型]，合法类型为 class、Any、类型变量（int、str...），或者类型的并集 type[class1 | class2]
    type[Any] = type，它是 python 类层级中的根对象
    :param user_class:
    :return:
    """
    if user_class is BasicUser:
        return user_class('shiloh', 18)

    if user_class is ProUser:
        return user_class('shiloh', 18, 1)


if __name__ == '__main__':
    make_new_user(BasicUser)
    make_new_user(ProUser)
    # 下面的调用会给出类型不匹配的警告
    make_new_user(TeamUser)
    make_new_user(int)
    # 同样会出现警告，因为 make_new_user() 方法需要的是 type[类型]，不是一个具体的对象
    make_new_user(ProUser('shiloh', 18, 1))
