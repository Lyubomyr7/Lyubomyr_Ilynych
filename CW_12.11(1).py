
# 1.  Напишіть скрипт-гру, яка генерує випадковим чином число з діапазону чисел від 1 до 100
# і пропонує користувачу вгадати це число. Програма зчитує числа, які вводить користувач і
# видає користувачу підказки про те чи загадане число більше чи менше за введене користувачем.
# Гра має тривати до моменту поки користувач не введе число, яке загадане програмою, тоді друкує повідомлення привітання.
# (для виконання завдання необхідно імпортувати  модуль random, а з нього функцію randint())


# import random
# number = random.randint(1,100)
#
# def game_number():
#     n=0
#     while n!= number:
#         n = int(input("Enter number from 1 to 100:"))
#         if n<number:
#             print("The number entered is less")
#         elif n>number:
#             print("The number entered is greater")
#     return ("You win")
# print(game_number())



# 2.  Напишіть скрипт, який обчислює площу прямокутника a*b, площу трикутника 0.5*h*a, площу кола pi*r**2.
# (для виконання завдання необхідно імпортувати  модуль math, а з нього функцію pow() та значення змінної пі).

import math
def area_of_figure():
    print("Area of the rectangle -1")
    print("Area of the triangle -2")
    print("Area of the circle -3")
    f = int(input("enter:"))
    if f == 1:
        a = int(input("enter length"))
        b = int(input("enter width"))
        return a*b
    if f == 2:
        a = int(input("enter side"))
        h = int(input("enter height"))
        return 0.5*h*a
    if f == 3:
        r = int(input("enter radius"))
        return math.pi*math.pow(r,2)
print("Area =",area_of_figure())




