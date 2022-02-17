# Task02：数学运算、字符串和文本、列表
## 数学运算
- 计算顺序为：先乘除后加减。
- “/”真除法、“%”求余数、“//”求整除，如果操作数中有实数，结果为实数形式的整数。
- “//”、“%”的运算级等同于乘除。
 ## 字符串和文本
 ### 字符串引用方法
 - 格式化的字符串常量进行引用
``` python 
 my_name = 'EuthL'
 print(f"Let's talk about {my_name}.")
```
 输出：
``` python
Let's talk about EuthL.
```
 - 使用format()方法进行引用
``` python 
# 第五处把字符串hilarious放入joke_evaluation中
hilarious = False 
joke_evaluation = "Isn't that joke so funny?! {}"
print(joke_evaluation.format(hilarious))
```
 - 把字符串放在字符串里面的引用（前四处）

``` python
# 定义人种类数
types_of_people = 10
# 第1把字符串types_of_people放到字符串x中
x = f"There are {types_of_people} types of people."
# 定义一个字符串变量
binary = "binary"
# 再定义一个字符串变量
do_not = "don't"
#第 2把字符串binary和do_not放到字符串y中
y = f"Those who know {binary} and those who {do_not}."
# 输出
print(x)
print(y)
# 第3把字符串x放字符串中并输出
print(f"I said:{x}")
# 第4把字符串y放字符串中并输出
print(f"I also said:'{y}'")
```
输出

``` python
here are 10 types of people.
Those who know binary and those who don't.
I said:There are 10 types of people.
I also said:'Those who know binary and those who don't.'
```

  ### 其他
 -  运算符+：算数加法，**列表、元组、字符串合并与拼接**，正号三种功能
 -  编程习惯：字符串常用双引号
 - **format()方法**功能很强大，而格式化的字符串常量是从python3.6开始支持的一致新的字符串格式化方式，其形式更简洁。
  [format()方法的数字格式化的应用](https://www.runoob.com/python/att-string-format.html)
  ## 列表
  基础：使用[]标识，其中的值可以切割，使用[头下标：尾下标]截取相应的列表，从左到右索引默认0开始，从右到左索引默认-1开始，下标为空表示取到头或尾。
  **附加练习**：
  **列表相关知识**
  1、列表是包含若干元素的有序连续内存空间，当列表增加或删除元素时，列表对象自动进行内存的扩展与收缩。在非尾部插入和删除元素会引起列表中大量元素的移动，严重影响效率，因此应尽量从列表尾部进行元素的追加与删除。
  2、列表中元素的数据类型可以各不相同，这是因为python采用基于值的自动内存管理模式，变量值并不直接储存值，而是储存值的引用或者内存地址。
  3、其他重要操作
  - list():将其他可迭代对象转换为列表。
    **注意**：变量list和函数list不能重名，重名的话函数在使用list()时，编译器会发现list是一个定义好的列表，而列表是不能被调用的，因此会抛出一个类型错误。
	特别的，关于字典的list()
``` python
# 将字典的“键”转换为列表
l3 = list({'a': 3, 'b': 9, 'c': 78})
# 将字典的“键值对”转换为列表
l4 = list({'a': 3, 'b': 9, 'c': 78}.items())
```
输出

``` python
['a', 'b', 'c']
[('a', 3), ('b', 9), ('c', 78)]
```
- 添加元素
  append():向列表尾部追加一个元素
  insert():向列表任意指定位置插入一个元素
  extend():将另一个列表的所有元素追加到当前列表的尾部
 - 删除元素
   pop():删除并返回指定位置上的元素，默认为最后一个
   remove():删除列表中第一个值与指定值相等的元素
   clear():清空列表中的所有元素
  - 返回出现次数及元素索引
   count():返回列表中指定元素出现的次数
  index():返回指定元素在列表中首次出现的索引
 - 排序及翻转
   sort():对所有元素进行排序，默认升序
  reverse()：将类别所有元素逆转或者翻转
  **注意**：以上时对列表进行原地排序和逆转，即处理后的数据替换原来的数据，原数据的顺序丢失。