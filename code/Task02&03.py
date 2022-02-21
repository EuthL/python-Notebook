print("-------数据类型转换-------")
# str->int
X = int('ABCD', 16)
print(X)
type(X)
# int->float
a = 520
b = float(a)
type(b)
# float->str
a = 5.99
b = str(a)
type(b)
# str->float
a = '520'
b = float(a)
type(b)
print("-------字符串的切片操作-------")
a_string = "Hello" + ' ' + "Women Who Code!"
print(a_string)
print("str[0]:" + a_string[0])
print("str[2:5]:" + a_string[2:5])
print("str[2:]:" + a_string[2:])
print("-------列表操作-------")
lis = ["WWCode",786,2.23,'singapore',70.2]
print(lis[0:3])
type(lis)
# 得到Code
print(lis[0][2:])
# 得到sing
print(lis[3][:4])
# 将lis最后一个元素改为50
lis[-1] =50
print(lis[-1])
# list comprehension操作
symbols = '$¢£¥€¤'
# 列表推导式语法
codes = [ord(symbol) for symbol in symbols]
print(codes)
print("-------元组操作-------")
# 创建元组
t1 = ("WWCode",100000,0.5)
t2 = 'Singapore',1160.5
t_singleton = ('We',)
t_empty = ()
print(type(t1))
print(type(t2))
print(t_singleton)
print(type(t_empty))
# 字典操作与Task03中一致
print("-------Sets集合-------")
# 使用{,}创建集合
wwcode_asia_networks={'Bangalore','Hong Kong','Shanghai','Tokyo'}
print(wwcode_asia_networks)
# 该位置报错错，因为set对象不支持下标应用和切片
# print(wwcode_asia_networks[1])
# 运算和布尔运算
x = 1+2
y = 3-4
z = 5*6
a=z/y
b=z%x
c=y**x
d=c//x
print("x:"+str(x)+" y:"+str(y)+" z:"+str(z)+" a:"+str(a)+" b:"+str(b)+" c"+str(c)+" d:"+str(d))
# c+=a  c=c+a
# c-=a  c=c-a
# c*=a  c=c*a
# c/=a  c=c/a
# c%=a  c=c%a
# c**=a  c=c**a
# c//=a  c=c//a
# is和is not运算符与==以及！=的区别
# is用于判断两个变量引用对象是否为同一个，==用于判断引用变量的值是否相等
#整数比较，一致
m = 5
n = 5
print(m == n)
print(m is n)
print(id(m))
print(id(n))
# 字符串比较，一致
x1 = "abcabcabcabcabcabcabcabcabcabc"
y1 = "abcabcabcabcabcabcabcabcabcabc"
print(x1 == y1)
print(x1 is y1)
print(id(x1))
print(id(y1))
# 数组比较，不一致
x2 = [1, 2, 3]
y2 = [1, 2, 3]
print(x2 == y2)
print(x2 is y2)
print(id(x2))
print(id(y2))
# 元组比较，一致
x3 = (1, 2, 3)
y3 = (1, 2, 3)
print(x3 == y3)
print(x3 is y3)
print(id(x3))
print(id(y3))
# 字典比较，不一致
x4 = {"id": 1, "name": "Tom", "age": 18}
y4 = {"id": 1, "name": "Tom", "age": 18}
print(x4 == y4)
print(x4 is y4)
print(id(x4))
print(id(y4))
# 集合比较，不一致
x5 = set([1, 2, 3])
y5 = set([1, 2, 3])
print(x5 == y5)
print(x5 is y5)
print(id(x5))
print(id(y5))
# 赋值后比较，一致
x6 = [1, 2, 3]
y6 = x6
print(x6 == y6)
print(x6 is y6)
print(id(x6))
print(id(y6))
# 空值比较,一致
none_type = None
print(none_type is None)
print(none_type == None)