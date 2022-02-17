import random

print('hallo world')
# 添加注释
print("I could have code like this.")
print("This will run.")

print("-------数学运算--------")
# 现在将计算我的鸡
print("I will now count my chickens:")
# 母鸡的总数为25+（30/6)
# 公鸡的总数为 100-（25*3%4），25*3%4=75%4=3
# 计算顺序为：先乘除后加减
# “/”真除法、“%”求余数
# “//”求整除，如果操作数中有实数，结果为实数形式的整数
# “//”、“%”的运算级等同于乘除
print("Hens", 25 + 30 / 6)
print("Roosters", 100 - 25 * 3 % 4)

# 现在我将计算鸡蛋数
print("Now I will count the eggs.")
# 鸡蛋数为，3+2+1-5+4%2-1/4+6=6.75
print(3 + 2 + 1 - 5 + 4 % 2 - 1 / 4 + 6)
# 3+2是否小于5-7？
print("Is is true that 3+2<5-7?")
# 5
print("What is 3+2?", 3 + 2)
# -2
print("What is 5-7?", 5 - 7)
print("Oh,that's why it's False.")

# 举多栗子
print("How about some more.")
# True
print("Is it greater?", 5 > -2)
# True,>=时都为True
print("Is it greater or equal?", 5 >= -2)
# False
print("Is it less or equal?", 5 <= -2)

print("-------字符串和文本--------")
cars = 100
space_in_a_car = 4.0
drivers = 30
passages = 90
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passages / cars_driven

print("There ", cars, "cars available.")
print("There are only", drivers, "drivers available.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We have", passages, "to carpool today")
print("We need to put about", average_passengers_per_car, "in each car")

# 附加练习
print("附加练习：")
my_name = "Wang Siyang"
my_age = 21
my_height = 163
my_weight = 65
my_eyes = "Black"
my_teeth = "white"
my_hair = "Black"
# 格式化的字符串常量（Formatted String Literals）
# 其含义与字符串对象的format()类似，但是形式更加简洁
print(f"Let's talk about {my_name}.")
print(f"She's {my_height} cm tall.")
print(f"She's {my_weight} pounds heavy")
print("Actually that's more heavy.")
print(f"She's got {my_eyes} and {my_hair} hair.")
print(f"Her teeth are usually {my_teeth} depending on the coffee.")
total = my_age + my_height + my_weight
print(f"If I add {my_age},{my_height},and {my_weight} I get {total}.")

print("输入一整段字符串、变量和格式:")
# 定义人种类数
types_of_people = 10
# 1、把字符串types_of_people放到字符串x中
x = f"There are {types_of_people} types of people."

# 定义一个字符串变量
binary = "binary"
# 再定义一个字符串变量
do_not = "don't"
# 2、把字符串binary和do_not放到字符串y中
y = f"Those who know {binary} and those who {do_not}."

# 输出
print(x)
print(y)

# 3、把字符串x放字符串中并输出
print(f"I said:{x}")
# 4、把字符串y放字符串中并输出
print(f"I also said:'{y}'")

hilarious = False
# 字符串常用双引号，其内部用单引号
joke_evaluation = "Isn't that joke so funny?!{}"
# 字符串的format()方法，输出为:Isn't that joke so funny?!False
# 也算是第5处把字符串hilarious放入joke_evaluation中
print(joke_evaluation.format(hilarious))

w = "This is the left side of..."
e = "a string with a right side."
# 运算符+：算数加法，列表、元组、字符串合并与拼接，正号
# +的列表、元组、字符串合并与拼接，因为两者的类型相同
print(w + e)

print("-------列表--------")
# 使用[]标识，其中的值可以切割，使用[头下标：尾下标]截取相应的列表
# 从左到右索引默认0开始，从右到左索引默认-1开始，下标为空表示取到头或尾
alist = ['runoob', 786, 2.23, 'john', 70.2]
tinylist = [123, 'john']
# 输出完整列表
print(alist)
# 输出列表的第一个元素
print(alist[0])
# 输出列表第二个至第三个元素
print(alist[1:3])
# 输出从第三个开始至列表末尾的所有元素
print(alist[2:])
# 输出列表两次
print(tinylist * 2)
# 打印组合的列表
print(alist + tinylist)

print("附加练习：")
# 列表相关知识
# 1、列表是包含若干元素的有序连续内存空间，
# 当列表增加或删除元素时，列表对象自动进行内存的扩展与收缩
# 在非尾部插入和删除元素会引起列表中大量元素的移动，严重影响效率，
# 因此应尽量从列表尾部进行元素的追加与删除。
# 2、列表中元素的数据类型可以各不相同，这是因为python采用基于值的自动内存管理模式，
# 变量值并不直接储存值，而是储存值的引用或者内存地址。
# 3、其他重要操作
# （1）list():将其他可迭代对象转换为列表
# 注意：变量list和函数list不能重名，重名的话函数在使用list()时，
# 发现list是一个定义好的列表，而列表是不能被调用的，因此会抛出一个类型错误
l1 = list((3, 4, 5, 6))
l2 = list(range(1, 10, 2))
# 将字典的“键”转换为列表
l3 = list({'a': 3, 'b': 9, 'c': 78})
# 将字典的“键值对”转换为列表
l4 = list({'a': 3, 'b': 9, 'c': 78}.items())
# 创建空列表
l5 = []
l6 = list()
print(l1)
print(l2)
print(l3)
print(l4)
print(l5)
print(l6)

# (2)列表常用方法
print("添加元素")
# append():向列表尾部追加一个元素
# insert():向列表任意指定位置插入一个元素
# extend():将另一个列表的所有元素追加到当前列表的尾部
blist = [1, 2, 3]
blist.append(4)
blist.insert(0, 0)
blist.extend([5, 6, 7])
# 应输出[0,1,2,3,4,5,6,7]
print(blist)

print("删除元素")
# pop():删除并返回指定位置上的元素，默认为最后一个
# remove():删除列表中第一个值与指定值相等的元素
# clear():清空列表中的所有元素
blist.pop()
blist.pop(0)
# 应为[1,2,3,4,5,6]
print(blist)
blist.insert(4, 6)
print(blist)
blist.remove(6)
print(blist)
blist.clear()
print(blist)

print("返回出现次数及元素索引")
# count():返回列表中指定元素出现的次数
# index():返回指定元素在列表中首次出现的索引
blist = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
# 3
print(blist.count(3))
# 1
print(blist.index(2))

print("排序及翻转")
# sort():对所有元素进行排序，默认升序
# reverse()：将类别所有元素逆转或者翻转
# 以上时对列表进行原地排序和逆转，即处理后的数据替换原来的数据，
# 原数据的顺序丢失
clist = list(range(11))
print(clist)
# 随机打乱
random.shuffle(clist)
print(clist)
clist.sort()
print(clist)
clist.reverse()
print(clist)