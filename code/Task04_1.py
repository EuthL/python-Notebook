from sys import argv

script, input_file = argv


# 读f文件
def print_all(f):
    print(f.read())


# 把文件指针移动到新的位置，0为从文件头开始
def rewind(f):
    f.seek(0)


# 打印行数和该行信息
def print_a_line(line_count, f):
    # readline() 是怎么知道每一行在哪儿的？
    #  readline() 里面的代码能够扫描文件的每个字节，
    #  当它发现一个 \n 字符，它就会停止扫描这个文件，然后回到它发现的地方。
    print(line_count, f.readline())


# 将从命令行读的文件传递到当前文件
current_file = open(input_file)
print("First let's print the whole file:\n")
# 调用print_all()函数，传入当前文件
print_all(current_file)
print("Now let's rewind ,kind of like a tape.")
# 调用rewind()函数，传入当前文件
rewind(current_file)
print("Let's print three line:")
# 当前行为第一行
current_line = 1
# 打印当前文件的第一行
print_a_line(current_line, current_file)
# 第二行
current_line = current_line + 1
print_a_line(current_line, current_file)
# 第三行
current_line = current_line + 1
print_a_line(current_line, current_file)
