# 该文件需要在命令行下运行，使用python Task03_1.py test.txt
from sys import argv
# sys为python的内置模块，提供了很多函数和变量来处理Python运行时环境的不同部分
# argv为“参数变量”，是一个参数列表，且第一个参数为脚本名称,该值是从命令行读来的
# from sys import argv可以通过a,b,c,d……=argv来进行批量参数赋值，将argv中的参数依次赋值给左边的变量
# 在该例子中，script为Task03_1.py,filename为test.txt
script,filename = argv
# 删除名为filename的文件
print(f"We're going to erase {filename}.")
# 如果你不想删除，点击CTRL-C
print("If you don't want that,hit CTRL-C(^C).")
# 如果你想要删除，点击RETURN（回车键）
print("If you do want that,hit RETURN.")

# 输入“？”
input("?")
# 打开文件
print("Opening the file...")
# 以写模式打开，如果文件存在，先清空原有内容
target = open(filename,'w', encoding="utf-8")

# 截断这个文件，拜拜！
print("Truncating the file.Goodbye!")
target.truncate()

print("Now I'm going to ask you for three lines.")

line1 = input("line1:")
line2 = input("line2:")
line3 = input("line3:")

print("I'm going to write these to the file.")

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print("And finally, we close it.")
target.close()
