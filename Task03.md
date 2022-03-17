# Task03:字典、元组、布尔类型、读写文件
# 字典
字典：能够把一个东西与另一个东西关联起来

``` python
stuff = {'name': 'Zed', 'age': 39, 'height': 6 * 12 + 2}
```
在字典中添加和删除东西

``` python
# 添加东西的两种方法
stuff['city'] = "SF"
stuff[1] = "Who"
# 删除东西
del stuff['city']
```
字典的映射概念核心在于使用“键”进行映射，可嵌套使用。如下例子，可以发现，先州字典后通过城市字典输出和直接通过城市字典输出是一样的，这说明可以这样嵌套使用。

``` python
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

```

