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

对字典对象进行迭代时，默认为遍历字典的“键”，如果想要遍历的是字典的“值”，需要使用values()方法说明；如果想要遍历整个字典对象需要用items()方法说明。

``` python
# 遍历键
for state in states:
    print(f"{state}")
# 遍历值
for abbrev in states.values():
    print(f"{abbrev}")
# 遍历字典元素
for state, abbrev in states.items():
    print(f"{state} is abbreviated {abbrev}")
```

输出

``` python
# 遍历键
Oregon
Florida
California
New York
Michigan
# 遍历值
OR
FL
CA
NY
MI
# 遍历元素
Oregon is abbreviated OR
Florida is abbreviated FL
California is abbreviated CA
New York is abbreviated NY
Michigan is abbreviated MI
```
使用get()安全访问字典的值，之所以被称为安全，是因为如果字典中不存在这个“键”会抛出异常，get()方法用来返回指定“键”对应的“值”，默认为None，也允许指定该键不存在的时候返回特定的“值”。比如访问city字典的“TX”键，但“TX”并不存在。可以使用如下方式访问：

``` python
city = cities.get('TX', 'Does Not Exist')
print(f"The city for the state 'TX' is:{city}")

```
输出

``` python
The city for the state 'TX' is:Does Not Exist
```
# 布尔类型
• and
• or
• not
• != （不等于）
• == （等于）
• >= （大于等于）
• <= （小于等于）
• True
• False
特别地，python地布尔运算中存在着惰性求值的问题。

``` python
# 5.True,在进行判断时具有惰性求值或者逻辑短路的特点,不计算2！=1
print(1 == 1 or 2 != 1)
# 7.False,此时也有惰性求值，不再求0!=0
print(False and 0 != 0)
# 8.True,惰性求值
print(True or 1 == 1)
```
# 读写文件