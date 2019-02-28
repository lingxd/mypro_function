# 测试形参，实参的基本用法

def printMax(a, b):
    '''比较两个数的最大值，并打印'''
    if a > b:
        print(a, "较大值")
    elif a == b:
        print("{0}={1}".format(a, b), "相等")
    else:
        print(a, "较大值")


printMax(10, 100)
printMax(10, 10)
printMax(100, 10)

help(printMax.__doc__)
