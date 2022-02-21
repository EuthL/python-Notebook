# 写一个类似于上个练习的脚本，使用 read 和 argv 来读取你刚刚创建的文件。
from sys import argv
script,filename = argv
with open(filename,'r') as fp :
    print(fp.read())
