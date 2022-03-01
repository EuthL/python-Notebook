print("-------（一）IF语句 -------")
# IF是判断语句
people = 20
cats = 30
dogs = 15
trucks = 15
if people < cats:
    print("好多猫猫!")
if people > cats:
    print("呜呜呜，没那么多猫猫了。")
if people < dogs:
    print("哇塞，很多狗狗")
if people > dogs:
    print("狗不如人呐")

dogs += 5
if people >= dogs:
    print("人比狗多，或者人和狗一样多。")
if people <= dogs:
    print("人不如狗多。")
if people == dogs:
    print("人和狗一样多。")

# if-elif-else:三组及三组以上的多级级联选择关系。
# 如果猫和人数量的三种关系
if cats > people:
    print("我们应该抓走猫。")
elif cats < people:
    print("我们不应该抓走猫。")
else:
    print("不能下决定抓住谁？")
# 卡车和猫的数量关系
if trucks > cats:
    print("卡车比猫猫多。")
elif trucks < cats:
    print("卡车不如猫猫多。")
else:
    print("我们不能下决定。")

print("-------（二）FOR语句 -------")
the_count = [1, 2, 3, 4, 5]
fruits = ['apple', 'orange', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

for number in the_count:
    print(f"This is count {number}")
for fruit in fruits:
    print(f"A fruit of type: {fruit}")
for i in change:
    print(f"I got {i}")
elements = []
for i in range(0, 6):
    print(f"Adding {i} to the list.")
    elements.append(i)
for i in elements:
    print(f"Element was: {i}")

print("-------（三）while语句 -------")
i = 0
numbers = []
# 保守使用while-loop，通常用 for-loop 更好一些。
# 检查 while 语句，确保布尔测试最终会在某个点结果为 False。
# 当遇到问题的时候，可以将
while i < 6:
    print(f"At the top i is {i}")
    numbers.append(i)

    i = i + 1
    print("Numbers now: ", numbers)
    print(f"At the bottom i is {i}")
print("The numbers: ")
