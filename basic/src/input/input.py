"""
用户输入：函数input()让程序暂停运行，等待用户输入一些文本。获取用户输入后，Python将其存储在一个变量中，以方便你使用。
如果你使用的是Python 2.7，应使用函数raw_input()来提示用户输入。这个函数与Python 3中的input()一样，也将输入解读为字符串。
Python 2.7也包含函数input()，但它将用户输入解读为Python代码，并尝试运行它们。如果你使用的是Python 2.7，请使用raw_input()而不是input()来获取输入。
"""
name = input('Please input your name:\n')
print('Hi, ' + name)