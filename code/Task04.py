print("-------（一）啥是函数-------")


# 创建函数
# 使用def创建函数
# 函数名只包含字符和_
# 函数名后放“（”
# “（”后放参数，参数之间可以用“，”隔开
# “）”后发“：”
# 与函数相关的代码里加上四个空格的缩进
# 另一行不缩进结束函数
# 调用函数

def print_two(*args):
    arg1, arg2 = args
    print(f"arg1:{arg1},arg2:{arg2}")


def print_two_again(arg1, arg2):
    print(f"arg1:{arg1},arg2:{arg2}")


def print_one(arg1):
    print(f"arg1:{arg1}")


def print_none():
    print("I got nothing.")


print_two("EuthL", "千根")
print_two_again("EuthL", "千根")
print_one("First!")
print_none()

print("-------（二）函数和变量-------")


# 定义了一个函数，有两个参数
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    # 打印第一个参数所含的话
    print(f"You have {cheese_count} cheeses!")
    # 打印第二个参数所含的话
    print(f"You have {boxes_of_crackers} boxes of crackers!")
    # 打印一句话
    print("Man that's enough for a party!")
    # 又打印一句话
    print("Get a blanket.\n")


print("We can just give the function numbers directly:")
# 调用这个函数，并赋值
cheese_and_crackers(20, 30)

# 使用变量调用函数
print("OR, we can use variables from our script:")
amount_of_cheese = 10
amount_of_crackers = 50
cheese_and_crackers(amount_of_cheese, amount_of_crackers)

# 调用时也可以包含数学表达式
print("We can even do math inside too:")
cheese_and_crackers(10 + 20, 5 + 6)

# 也可以有变量和数字的运算
print("And we can combine the two, variables and math:")
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)
# 函数的参数有点类似给变量赋值
# 如何分析函数
# 每行加注释这种方式、大声把代码读出来、把代码打印出来然后在上面画图

print("-------（四）函数可以返回一些东西-------")


# +
def add(a, b):
    print(f"ADDING{a}+{b}")
    return a + b


# -
def subtract(a, b):
    print(f"SUBTRACTING{a}-{b}")
    return a - b


# *
def multiply(a, b):
    print(f"MULTIPLY{a}*{b}")
    return a * b


# /
def divide(a, b):
    print(f"DIVIDING{a}/{b}")
    return a / b


# 使用函数进行数学计算
print("Let's do some math with just functions!")
# 35
age = add(30, 5)
# 74
height = subtract(78, 4)
# 200
weight = multiply(100, 2)
# 50
iq = divide(100, 2)
print(f"Age: {age}, Height: {height}, Weight: {weight}, IQ: {iq}")
# 35+(74-200*(50/2))= -4891
what = add(age, subtract(height, multiply(weight, divide(iq, 2))))
print("That becomes: ", what, "Can you do it by hand?")
