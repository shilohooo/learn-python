"""
Python 泛型 Demo

注意：对泛型的语法支持是在 Python 3.12 中新增的。

@author: shiloh
@date: 2024/12/25 16:31
"""

from collections.abc import Mapping, Sequence
from typing import TypeVar


class Employee:
    """
    员工类
    """

    def __init__(self, name: str, age: int, salary: float):
        """
        构造函数
        :param str name: 姓名
        :param int age: 年龄
        :param float salary: 工资
        """
        self.name = name
        self.age = age
        self.salary = salary

    def __str__(self):
        return f"Employee(name={self.name}, age={self.age}, salary={self.salary})"


def print_employee_info(employees: Sequence[Employee], overrides: Mapping[str, str]):
    """
    打印员工信息
    :param employees: 元素类型为 Employee 的序列
    :param overrides: key 和 value 都必须是 str 类型的 Mapping
    :return:
    """
    for employee in employees:
        print(f"{employee.name} is {employee.age} years old and earns ${employee.salary:.2f}")
        print(f"{overrides.get(employee.name)}")


# 参数化泛型
# 也可以使用 TypeVar 来创建一个泛型
U = TypeVar('U')


# def first[T](list_data: Sequence[T]) -> T:
def first(list_data: Sequence[U]) -> U:
    """
    获取列表中的第一个元素
    :param list_data: 列表
    :return: 第一个元素
    """
    return list_data[0]


def main():
    employees = [
        Employee("John", 30, 50000),
        Employee("Jane", 28, 45000),
        Employee("Jim", 35, 60000),
    ]
    overrides = {
        "John": "He is a great employee.",
        "Jane": "She is a hard worker.",
        "Jim": "He is a reliable employee.",
    }
    print_employee_info(employees, overrides)

    nums = [1, 2, 3, 4]
    # 自动推导出了变量的类型为 int
    first_num = first(nums)
    print(f'{first_num=}')
    colors = ["red", "green", "blue"]
    # 自动推导出了变量的类型为 str
    first_color = first(colors)
    print(f'{first_color=}')


if __name__ == "__main__":
    main()
