"""
python 循环之 while 循环
for循环用于针对集合中的每个元素都一个代码块，而while循环不断地运行，直到指定的条件不满足为止。
"""

num = 1
while num <= 5:
    print(num)
    num += 1

print("\n<==========================================================>\n")

# break - 跳出循环
num_b = 1
while num_b <= 10:
    print(num_b)
    if num_b > 5:
        break
    num_b += 1
# continue - 跳过当前循环
print("\n<==========================================================>\n")
num_c = 0
while num_c < 10:
    num_c += 1
    if num_c % 2 == 0:
        continue
    print(num_c)
