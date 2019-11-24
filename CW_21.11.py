# 1.  Напишіть програму, яка пропонує користувачу ввести ціле число
# і визначає чи це число парне чи непарне, чи введені дані коректні.

# while True:
#     try:
#         num = int(input("Enter number:"))
#         if num%2 ==0:
#             print("Введене число є парне")
#         else:
#             print("непарне")
#
#
#     except ValueError:
#         print("введіть число")

# 2.  Напишіть програму, яка пропонує користувачу ввести свій вік,
# після чого виводить повідомлення про те чи вік є парним чи непарним числом.
# Необхідно передбачити можливість введення від’ємного числа, в цьому випадку згенерувати власну виняткову ситуацію.
# Головний код має викликати функцію, яка обробляє введену інформацію.
#
# while True:
#     try:
#         age = int(input("Enter number:"))
#         if age<=0:
#             raise TypeError("Вік не може бути відємним")
#         elif age%2 ==0:
#             print("Число парне")
#         elif age%2 !=0:
#             print("Число непарне")
#     except TypeError as e :
#         print(e)
#     except ValueError:
#         print("Необхідно ввести число")
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

# class CustomError(Exception):
#     def __init__(self,data):
#         self.data = data
#     def __str__(self):
#         return repr(self.data)
#
# try:
#     age = int(input("Enter number"))
#     if age<=0:
#         raise CustomError("Вік не може бути відємним")
#     elif age % 2 == 0:
#         print("Число парне")
#     elif age % 2 != 0:
#         print("Число непарне")
#
# except CustomError as e:
#     print(e.data)
# except ValueError:
#     print("Введіть число")


# 3.  Напишіть програму для обчислення частки двох чисел, які вводяться користувачем послідовно через кому,
# передбачити випадок ділення на нуль, випадки синтаксичних помилок та випадки інших виняткових ситуацій.
# Використати блоки else та finaly.

# def div(a,b):
#         try:
#             # a=int(input("Enter number 1:"))
#             # b = int(input("Enter number 2:"))
#             res=a/b
#             print(res)
#
#         except ZeroDivisionError:
#             print("Division by zero is inadmissible")
#         except ValueError:
#             print("The value must be a namber")
#         else:
#             print("No exeption")
#         finally:
#             print("Program code finished")
# div(6,2)


# 4.  Написати  програму, яка аналізує введене число та в залежності від числа видає день тижня,
# який відповідає цьому числу (1 це Понеділок, 2 це Вівторок і т.д.) .
# Врахувати випадки введення чисел від 8 і більше, а також випадки введення не числових даних.

while True:
    try:

        day = {1:"Понеділок",2:"Вівторок",3:"Середа",4:"Четвер",5:"П'ятниця",6:"Субота",7:"Неділя"}
        num = int(input("enter number:"))
        if num<=0 or num>7 :
            raise TypeError("Числа повинні бути в діапазоні [1:7]")
        for i in day:
            if num ==i:
                print(day[i])
    except TypeError as e:
        print(e)
    except ValueError:
        print("Потрібно ввести число")


