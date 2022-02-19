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
# 创建州的缩写及其缩写的映射
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
# 输出一些城市
print('_' * 10)
print("NY State has:", cities['NY'])
print("OR State has:", cities["OR"])
