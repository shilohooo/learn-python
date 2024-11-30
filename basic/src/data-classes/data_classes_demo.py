"""
python data classes - 用于存储数据的类（Model）
就像 ORM 里面的实体
"""
from dataclasses import dataclass
from typing import Any


# 不使用 dataclass
class MyNumber:
    def __init__(self, val):
        self.val = val


obj = MyNumber(4)
print(obj.val)


# 使用 dataclass
@dataclass
class MyNumberUsingDataClass:
    """
    dataclass 装饰器可以为自动生成一些方法，比如： __init__()、__repr__()
    """

    # 这个字段会加到__init__()方法中
    val: int


my_num = MyNumberUsingDataClass(3)
print(my_num.val)


# 带默认值的 data class
@dataclass
class Product:
    name: str
    # 如果不知道某个字段的类型，可以使用 Any
    desc: Any
    count: int = 0
    price: float = 0.5


# product = Product('Python', 1)
product = Product('Python', 'Desc msg')
print(product.name)
print(product.count)
print(product.price)
# product.desc = 1
print(product.desc)
