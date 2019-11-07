
# 1.  Створити список цілих чисел, які вводяться з терміналу та визначити серед них максимальне та мінімальне число.

# sp = []
# cou = int(input("enter count"))
# for i in range(cou):
#     n=int(input("enter number"))
#     sp.append(n)
# print(sp)
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# cou = int(input("enter count"))
# sp = [int(input("enter number")) for x in range(cou) ]
# print(sp)
# print("max:",max(sp))
# print("min:",min(sp))


#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# sp = []
# n = int(input("enter count:"))
# a = 0
# while a<n:
#     number  =  int(input("enter number:"))
#     sp.append(number)
#     a+=1
# print(sp)
# print("MAX number:",max(sp))
# print("MIN number:",min(sp))

# 2.  В інтервалі від 1 до 10 визначити числа
# •  парні, які діляться на 2,
# •  непарні, які діляться на 3,
# •  числа, які не діляться на 2 та 3.


# sp1 = [x for x in range(1,11) if x%2==0]
# print("Парні які діляться на 2",sp1)
# sp2 = [x for x in range(1,11) if x%3==0]
# print("непарні які діляться на 3",sp2)
# sp3 = [x for x in range(1,11) if x%3!=0 and x%2!=0]
# print("числа, які не діляться на 2 та 3",sp3)


# 3.  Написати програму, яка обчислює факторіал числа, яке користувач вводить.(не використовувати рекурсивного виклику функції)


# num_f = int(input("enter facktorial:"))
# factorial= 1
# for nu in range(1,num_f):
#     factorial=factorial*(nu+1)
# print("Факторіал числа {} :".format(num_f),factorial)



# 4.  Напишіть скрипт, який перевіряє логін, який вводить користувач.
# Якщо логін вірний (First), то привітайте користувача.
# Якщо ні, то виведіть повідомлення про помилку.
# (використайте цикл while)

# login = input("enter login")
# while True:
#     if login=="First":
#         True
#         print("Hello")
#         break
#     else:
#         False
#         print("Error")
#         break


# 5.  Перший випадок.
# Написати програму, яка буде зчитувати числа поки не зустріне від’ємне число.
# При появі від’ємного числа програма зупиняється (якщо зустрічається 0 програма теж зупиняється).

# import random
# n1 = [random.randint(-10,50) for i in range(10) ]
# print(n1)
# for i in n1:
#     if i>0:
#         print(i)
#     else:
#         break


# 6.  Другий випадок.
# На початку на вхід подається кількість елементів послідовності, а потім самі елементи.
# При появі від’ємного числа програма зупиняється (якщо зустрічається 0 програма теж зупиняється).

# import random
# count_number = int(input("enter count number:"))
# n1 = [random.randint(-10,50) for i in range(count_number) ]
# print(n1)
# for i in n1:
#     if i>0:
#         print(i)
#     else:
#         break

# 7.  Знайти прості числа від 10 до 30, а всі решта чисел представити у вигляді добутку чисел
# (наприклад 10 equals 2 * 5
#  11 is a prime number
#  12 equals 2 * 6
#  13 is a prime number
#  14 equals 2 * 7
#  ………………….)


# 8.  Відсортувати слова в реченні в порядку їх довжини (використати List Comprehensions)
# sentence = "Explicit is better than implicit."
# a= sentence.split()
# print(a)
# b= [a.sort(key=len) for x in a ]
# print(a)






