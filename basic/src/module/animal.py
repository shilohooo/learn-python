# 导入模块
# import cat
# 导入某个模块中的函数，导入多个函数用逗号分隔
# from cat import eat, sleep
# from cat import eat

# 使用 as 给函数指定别名
# 如果要导入的函数的名称可能与程序中现有的名称冲突，或者函数的名称太长，
# 可指定简短而独一无二的别名——函数的另一个名称，类似于外号
# from cat import eat as cat_eat_fn

# 还可以给模块指定别名。通过给模块指定简短的别名，能够更轻松地调用模块中的函数
# import cat as c

# 使用 * 号导入某个模块里面的所有函数
# 注意：不推荐这种做法，应该使用到哪个函数就导入那个函数，减少依赖大小
from cat import *

# 调用导入模块的方法
food = 'fish'
# cat.eat(food)
eat(food)
run()
# cat_eat_fn(food)
# c.eat(food)
