# python语言基础题目
# 题目：从键盘输入两个正整数a和b,计算并输出a/b的商和余数
def countOfab(a, b):
    print("a/b:", a / b)
    print("a%b:", a % b)


# 题目：从键盘输入一个3位整数，请编写程序计算三位整数的各位数字之和，
# 并输出到屏幕上，要求占4列，右对齐。
def decomposition(num):
    B = num // 100
    S = (num - B * 100) // 10
    G = num - B * 100 - S * 10
    sum = B + S + G
    print("%4d" % sum)


if __name__ == '__main__':
    print("题目1：从键盘输入两个正整数a和b,计算并输出a/b的商和余数")
    a = int(input("输入a："))
    b = int(input("输入b："))
    countOfab(a, b)
    print("题目2：从键盘输入一个3位整数，请编写程序计算三位整数的各位数字之和，\n"
          "并输出到屏幕上，要求占4列，右对齐。")
    num = int(input("输入一个三位数："))
    decomposition(num)
