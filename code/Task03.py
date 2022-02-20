# 字典、元组、布尔类型、读写文件
print("-------字典-------")
# 列表和字典的区别：列表用数字索引，且只能通过数字取出列表中的元素
# 字典能够把一个东西与另一个东西关联起来
stuff = {'name': 'Zed', 'age': 39, 'height': 6 * 12 + 2}
print(stuff['name'])
print(stuff['age'])
print(stuff['height'])
# 字典中添加东西
stuff['city'] = "SF"
print(stuff['city'])
stuff[1] = "Who"
stuff[2] = "Neato"
print(stuff[1])
print(stuff[2])
# 字典中删除东西
del stuff['city']
del stuff[1]
del stuff[2]
print(stuff)
# 字典的映射概念的理解
# 创建州及其缩写的映射
states = {
    'Oregon': 'OR',
    'Florida': 'FL',
    'California': 'CA',
    'New York': 'NY',
    'Michigan': 'MI'
}
# 州的缩写与城市的映射
cities = {
    'CA': 'San Francisco',
    'MI': 'Detroit',
    'FL': 'Jacksonvile'
}
# 添加更多的城市
cities['NY'] = 'New York'
cities['OR'] = 'Portland'
# 使用cities输出一些城市
print('_' * 10)
print("NY State has:", cities['NY'])
print("OR State has:", cities["OR"])
# 使用states输出一些州
print('_' * 10)
print("Michigan's abbreviation is :", states['Michigan'])
print("Florida's abbreviation is:", states['Florida'])
# 先通过州字典，后通过城市字典输出
print("Michigan has:", cities[states['Michigan']])
print("Florida has:", cities[states['Florida']])
# 输出每个州的缩写
# 对字典对象直接进行迭代或者遍历时默认是遍历字典的“键”，
# 变量字典的元素需要使用字典对象的items方法说明，
# 遍历值时，必须使用字典对象的values()方法明确说明。
# 遍历键
print('-' * 10)
for state in states:
    print(f"{state}")
# 遍历元素
print('-' * 10)
# 这里的list()可以去掉
for state, abbrev in list(states.items()):
    print(f"{state} is abbreviated {abbrev}")
# 遍历值
print('-' * 10)
for abbrev in states.values():
    print(f"{abbrev}")
# 输出每个州对应的城市
print('-' * 10)
for abbrev, city in list(cities.items()):
    print(f"{abbrev} has the city {city}")
# 现在同时做以上两件事
for state, abbrev in list(states.items()):
    print(f"{state} state is abbreviated {abbrev}")
    print(f"and has the city {cities[abbrev]}")
print('_' * 10)
# 如何安全地通过州得到一个不存在的缩写
# 之所以称为安全地，是因为如果根据提供的“键”作为下标可以访问对应的“值”，
# 如果字典中不存在这个“键”会抛出异常。
# get()方法用来返回指定“键”对应的“值”，默认为None,
# 也允许指定该键不存在的时候返回特定的“值”。
state = states.get('Taxas')
print(state)
if not state:
    print("Sorry,no Texas")
# 用默认的值得到城市名
city = cities.get('TX', 'Does Not Exist')
print(f"The city for the state 'TX' is:{city}")

print("-------元组-------")
# 元组用 () 标识，内部元素用逗号隔开。
# 元组不能二次赋值，相当于只读列表。
tuple1 = ('runoob', 786, 2.23, 'john', 70.2)
tinytuple = (123, 'john')
# 输出完整元组
print(tuple1)
# 输出元组的第一个元素
print(tuple1[0])
# 输出第二个至第四个（不包括）的元素
print(tuple1[1:3])
# 输出从第三个开始至列表末尾的所有元素
print(tuple1[2:])
# 输出元组两次
print(tinytuple * 2)
print(tuple1 + tinytuple)
# 以下是元组无效的操作
#tuple1[2] = 1000
print(tuple1)

print("-------布尔类型-------")
# python的逻辑表
# 1.True
print(True and True)
# 2.False
print(False and True)
# 3.False
print(1 == 1 and 2 == 1)
# 4.True
print("test" == "test")
# 5.True,在进行判断时具有惰性求值或者逻辑短路的特点,不计算2！=1
print(1 == 1 or 2 != 1)
# 6.True
print(True and 1 == 1)
# 7.False,此时也有惰性求值，不再求0!=0
print(False and 0 != 0)
# 8.True,惰性求值
print(True or 1 == 1)
# 9.False
print("test" == "testing")
# 10. False
print(1 != 0 and 2 == 1)
# 11.True
print("test" != "testing")
# 12.False
print("test" == 1)
# 13. True
print(not (True and False))
# 14.False
print(not (1 == 1 and 0 != 1))
# 15.False
print(not (10 == 1 and 1000 == 1000))
# 16.False
print(not (1 != 10 or 3 == 4))
# 17.True
print(not("testing" == "testing" and "Zed" == "Cool Guy"))
# 18.True
print(1 == 1 and (not ("testing" == 1 or 1 == 0)))
# 19.False
print("chunky" == "bacon" and (not (3 == 4 or 3 == 3)))
# 20.False
print(3 == 3 and (not ("testing" == "testing" or "Python" == "Fun")))
