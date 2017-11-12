# coding=utf-8
# /usr/bin/env python3

import math


# 没有决策条件，可能导致抱错
def main1():
    print("This program finds the real solutions to the quadratic\n")
    a, b, c = eval(input("Please enter the coefficients (a, b, c): "))
    delta = b * b - 4 * a * c
    delta = math.sqrt(delta)
    root1 = (-b + delta) / (2 * a)
    root2 = (-b - delta) / (2 * a)
    print("\nThe solutions are: ", root1, root2)


# 加入决策条件，不过在delta小于0时，直接跳过计算
def main2():
    print("This program finds the real solutions to the quadratic\n")
    a, b, c = eval(input("Please enter the coefficients (a, b, c): "))
    delta = b * b - 4 * a * c
    if delta >= 0:
        delta = math.sqrt(delta)
        root1 = (-b + delta) / (2 * a)
        root2 = (-b - delta) / (2 * a)
        print("\nThe solutions are: ", root1, root2)


# 改进后的算法，但依然不完美
def main3():
    print("This program finds the real solutions to the quadratic\n")
    a, b, c = eval(input("Please enter the coefficients (a, b, c): "))
    delta = b * b - 4 * a * c
    if delta >= 0:
        delta = math.sqrt(delta)
        root1 = (-b + delta) / (2 * a)
        root2 = (-b - delta) / (2 * a)
        print("\nThe solutions are: ", root1, root2)
    else:
        print("The equation has no real roots!")


# 处理单解
def main4():
    print("This program finds the real solutions to the quadratic\n")
    a, b, c = eval(input("Please enter the coefficients (a, b, c): "))
    delta = b * b - 4 * a * c
    if delta > 0:
        delta = math.sqrt(delta)
        root1 = (-b + delta) / (2 * a)
        root2 = (-b - delta) / (2 * a)
        print("\nThe solutions are: ", root1, root2)
    elif delta == 0:
        root1 = -b / (2 * a)
        print("\nThe solution is ", root1)
    else:
        print("The equation has no real roots!")


# 添加a=0的情况
def main5():
    print("This program finds the real solutions to the quadratic\n")
    a, b, c = eval(input("Please enter the coefficients (a, b, c): "))
    delta = b * b - 4 * a * c
    if a == 0:
        root = -b / c
        print("\nThe solution is ", root)
    elif delta > 0:
        delta = math.sqrt(delta)
        root1 = (-b + delta) / (2 * a)
        root2 = (-b - delta) / (2 * a)
        print("\nThe solutions are: ", root1, root2)
    elif delta == 0:
        root1 = -b / (2 * a)
        print("\nThe solution is ", root1)
    else:
        print("The equation has no real roots!")


# 使用try语句进行异常捕捉
def main6():
    print("This program finds the real solutions to the quadratic\n")
    a, b, c = eval(input("Please enter the coefficients (a, b, c): "))
    try:
        delta = math.sqrt(b * b - 4 * a * c)
        root1 = (-b + delta) / (2 * a)
        root2 = (-b - delta) / (2 * a)
        print("\nThe solutions are: ", root1, root2)
    except ValueError:
        print("The equation has no real roots!")


# 使用try语句对所有异常进行捕捉
def main7():
    print("This program finds the real solutions to the quadratic\n")
    try:
        a, b, c = eval(input("Please enter the coefficients (a, b, c): "))
        delta = math.sqrt(b * b - 4 * a * c)
        root1 = (-b + delta) / (2 * a)
        root2 = (-b - delta) / (2 * a)
        print("\nThe solutions are: ", root1, root2)
    except ValueError as excObj:
        if str(excObj) == 'math domain error':
            print("The equation has no real roots!")
        else:
            print("You didn't give me the right number of coefficients.")
    except NameError:
        print("You didn't give me three numbers.")
    except TypeError:
        print("Your inputs are not all numbers.")
    except SyntaxError:
        print("Your input was not in the correct form, Missing comma?")
    except:  # had better no use bare except.
        print("Something wrong, I'm sorry.")


if __name__ == '__main__':
    main7()
