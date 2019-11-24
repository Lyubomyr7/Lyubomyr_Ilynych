# 1.  Створити клас машина з атрибутами name,
# make, model та методами start та stop,
# які виводять інформацію про те що автомобіль стартував чи зупинився відповідно.
# class Car:
#     def __init__(self, name, make, model):
#         self.name = name
#         self.make = make
#         self.model = model
#
#     def start(self):
#         print("Car start")
#     def stop(self):
#         print("Car stop")
#
# car1= Car("My car","Mercedes","GLS550 AMG")
# car1.start()
# car1.stop()



# 2.  Створити клас особа,  в якому конструктор встановлює ім’я,
# а метод info виводить повідомлення “Hello, my name is {ім’я конкретного екземпляра класу}”,
# а також створити клас автомобіль,  в якому конструктор встановлює ім’я, а метод move виводить повідомлення
# {ім’я конкретного екземпляра класу}  moves at the speed {speed(цей параметр метод moveотримує як вхідний)} km / h

# class Person:
#     def __init__(self,name):
#         self.name = name
#     def info(self):
#         print ("Hello, my name is {}".format(self.name))
#
# class Car:
#     def __init__(self,name):
#         self.car_name = name
#     def move(self,speed):
#         print("{} moves at the speed {} km/h".format(self.car_name,speed) )
#
# Lyubomyr = Person("Lyub")
# Lyubomyr.info()
#
# car1 = Car("BMW X5M")
# car1.move("310")



# 3.  Створити клас особа,  в якому конструктор встановлює ім’я, вік.
# Використати в цьому класі геттери та сеттери, а також створити метод info, який виводить
# інформацію про ім’я та вік особи. А тоді створити клас працівник, який наслідується від класу особи і містить метод details,
# який на вхід отримує параметр про компанію, в якій працює працівник і цей метод виводить інформацію про те,
# що працівник з таким то іменем працює в такій то компанії.

# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     @property
#     def get_name(self):
#         return self.name
#
#     @property
#     def get_age(self):
#         return self.age
#
#     @get_name.setter
#     def set_name(self,name):
#         self.name = name
#
#     @get_age.setter
#     def set_age(self,age):
#         self.age = age
#
#     def info(self):
#         print("{} is {} years old".format(self.name,self.age))
#
#
#
# class Worker(Person):
#     def __init__(self,name,age):
#         Person.__init__(self,name,age)
#
#     def details(self,company):
#         print("Worker {}  work in {}".format(self.name,company))
#
#
# worker1= Worker("Lyubomyr",20)
# worker1.details("Softserve")
# worker1.info()



# 4.  Створити батьківський клас Figure з методами
# init: ініціалізується колір,
# get_color: повертає колір фігури,
# info: надає інформацію про фігуру та колір,
# від якого наслідуються такі класи як Rectangle,
# Square, які мають інформацію про ширину, висоту фігури, метод square, який знаходить площу фігури.

class Figure:
    def __init__(self,color,width,height):
        self.color = color
        self.width = width
        self.height = height
    def get_color(self):
        return self.color
    def info(self):
        print("height-{},width-{},color-{}".format(self.height,self.width,self.color))

class Rectangle(Figure):
    def __init__(self,color,width,height):
        Figure.__init__(self,color,width,height)

    def square(self):
        print("Square rectangle = {}".format(self.width*self.height))


class Square(Figure):
    def __init__(self,color,width,height):
        Figure.__init__(self,color,width,height)

    def square(self):
        print("Square rectangle = {}".format(self.width*self.height))

rectngle1= Rectangle("Black",3,4)
rectngle1.square()
print(rectngle1.get_color())
rectngle1.info()

square1= Square("Red",4,4)
square1.square()
square1.info()



