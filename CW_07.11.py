# 1.  Написати функцію, яка знаходить середнє арифметичне значення довільної кількості чисел.

# def ser_a(*args):
#     for a in args:
#         a += a
#     su= a/len(args)
#     print(int(su))
#
# ser_a(2,4,6)

# 2.  Написати функцію, яка повертає абсолютне значення числа

# def absol(a):
#     """ the function returns an absolute value"""
#     return abs(a)
# print(absol(-5))


# 3.  Написати функцію, яка знаходить максимальне число з двох чисел, а також в функції використати рядки документації DocStrings.


# def max_number(a,b):
#     """ The function finds the maximum number of two numbers"""
#     if a>b:
#         print("max:",a)
#     else:
#         print("min",b)
# max_number(7,3)

# 4.  Написати програму, яка обчислює площу прямокутника,
# трикутника та кола (написати три функції для обчислення площі,
# і викликати їх в головній програмі в залежності від вибору користувача)
# import math
# print("To find the rectangle area,enter 1")
# print("To find the triangle area,enter 2")
# print("To find the circle area,enter 3")
# num = int(input("Enter number:"))
# def rectangle():
#     """This function calculates the area of a rectangle"""
#     a = int(input("Enter a length:"))
#     b = int(input("Enter a width:"))
#     return print("S=",a*b)
#
# def triangle():
#     """This function calculates the area of a rectangle"""
#     a = int(input("Enter the side of the triangle:"))
#     h = int(input("Enter height:"))
#     return print("S=",0.5*a*h)
#
# def circle():
#     """This function calculates the area of a rectangle"""
#     r= int(input("Enter radius:"))
#     return print("S=",(math.pi *(r**2)))
#
# if num==1:
#     rectangle()
# elif num==2:
#     triangle()
# elif num==3:
#     circle()

# 5.  Написати функцію, яка обчислює суму цифр введеного числа.
# def sum_num():
#     """ This function calculates the sum of the numbers entered"""
#     a=input("Enter number")
#     s=0
#     for i in a:
#         s += int(i)
#     print(s)
# sum_num()

# 6.  Написати програму калькулятор, яка складається з наступних функцій:
# головної, яка пропонує вибрати дію та додаткових, які реалізовують вибрані дії,
# калькулятор працює доти, поки ми не виберемо дію вийти з калькулятора, після виходу,
# користувач отримує повідомлення з подякою за вибір нашого програмного продукту!!!

# def add_numbers(a,b):
#     """This function of adding two number"""
#     print("{}+{}= {}".format(a,b,a+b))
# def subtraction_numbers(a,b):
#     """This function of subtracting two number"""
#     print("{}-{}= {}".format(a, b, a - b))
# def multiplication_numbers(a,b):
#     """This function of multiplication two number"""
#     print("{}*{}= {}".format(a, b, a * b))
# def division_numbers(a,b):
#     """This function of dividing two number"""
#     print("{}/{}= {}".format(a,b,a/b))
#
# def cal():
#     a = int(input("enter first number"))
#     b = int(input("enter second number"))
#     n = ""
#     while n!= "exit":
#         n= input("enter sign")
#         if n == "+":\
#             add_numbers(a,b)
#         elif n == "-":
#             subtraction_numbers(a,b)
#         elif n == "*":
#             multiplication_numbers(a,b)
#         elif n == "/":
#             division_numbers(a,b)
#     print("Thank you for choosing our product")
# cal()

# 7.  Побудувати рекурсивну функцію обчислення чисел Фібоначі до числа введеного користувачем.

def fibo():
    """ function not recurse"""
    a = 0
    b = 1
    l= int(input("Enter number"))
    for i in range(0,l-1):
        fib = a+b
        print(fib)
        a=b
        b=fib
fibo()
