import pygame
from pygame import mixer
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk

pygame.mixer.init()
root = Tk()

pygame.mixer.music.load("cof.mp3")

root.config(bg="silver")

image = Image.open('details.gif')
photo_image5 = ImageTk.PhotoImage(image)
image = Image.open('espresso.png')
photo_image1 = ImageTk.PhotoImage(image)
image = Image.open('amerikano.png')
photo_image2 = ImageTk.PhotoImage(image)
image = Image.open('capucino.png')
photo_image3 = ImageTk.PhotoImage(image)
image = Image.open('latte.png')
photo_image4 = ImageTk.PhotoImage(image)

# створюємо вікно
root.title("Coffe maker")
root.geometry("800x700+350+50")


label1 = Label(root,text="Внесіть кошти і зробіть свій вибір", fg="#eee", bg="#111",font="30" )
label1.pack()

EntryA=Entry(root,width=10,font='Arial 16')
EntryA.pack()

def proizv():
    global cash
    cash = EntryA.get() # берем текст из первого поля
    cash = int(cash) # преобразуем в число целого типа
    EntryA.delete(0,END)

but = Button(root, text='Кошти внесено', command=proizv,width="20",height="2",bg="blue")
but.pack()


coffee = {
    "espresso": {
        "coffee": 5,
        "water": 50,
        "milk": 0,
        "sugar": 2,
        "cup": 1,
        "price": 10
    },

    "americano": {
        "coffee": 5,
        "water": 100,
        "milk": 10,
        "sugar": 3,
        "cup": 1,
        "price": 15
    },

    "capycino": {
        "coffee": 5,
        "water": 100,
        "milk": 50,
        "sugar": 4,
        "cup": 1,
        "price": 20
    },

    "latte": {
        "coffee": 5,
        "water": 20,
        "milk": 100,
        "sugar": 4,
        "cup": 1,
        "price": 20
    }
}
cofmac = {
    "name": "Python Coffee Machine",
    "money": 1000,
    "ingredients": {
        "coffee": 1000,
        "water": 5000,
        "milk": 2000,
        "sugar": 1000,
        "cup": 20
    }
}


def check_ingredients(coffee_name):
    for ingr in cofmac["ingredients"]:
        if cofmac["ingredients"][ingr] - coffee[coffee_name][ingr] < 0:
            return False
    return True

def make_coffee(coffee_name):


    if check_ingredients(coffee_name):
        if put_money(cash, coffee_name):
            for ingr in cofmac["ingredients"]:
                cofmac["ingredients"][ingr] -= coffee[coffee_name][ingr]
            pygame.mixer.music.play()
            messagebox.showinfo("Coffe maker","Bon apetit {}".format(coffee_name))
        else:
                messagebox.showinfo("Coffe maker", "Not enough money  ")
    else:
            messagebox.showinfo("Coffe maker", "Not enough ingredients!")


def put_money(cash, coffee_name):
    if coffee[coffee_name]["price"] <= cash:
        cofmac["money"] += coffee[coffee_name]["price"]
        change1=cash - coffee[coffee_name]["price"]
        if change1 >=1:
            messagebox.showinfo("Coffe maker","Your remainder:{}₴".format(change1))
        return True
    return False

def click_button():
    make_coffee("espresso")

def click_button2():
    make_coffee("americano")

def click_button3():
    make_coffee("capycino")

def click_button4():
    make_coffee("latte")

def click_button5():
    messagebox.showinfo("Coffe maker", "{}".format(cofmac))



espr_button = Button(root,text="Espresso - 10грн", # текст кнопки
             background="#555",     # фоновый цвет кнопки
             foreground="#ccc",     # цвет текста
             font="16",              # высота шрифта
            command= click_button,
            image = photo_image1
             )

espr_button.pack()



amer_button = Button(root,text="Americano - 15грн", # текст кнопки
             background="#555",     # фоновый цвет кнопки
             foreground="#ccc",     # цвет текста
             font="16",              # высота шрифта
            command= click_button2,
            image = photo_image2

             )
amer_button.pack()


cap_button = Button(root,text="Capycino - 20грн", # текст кнопки
             background="#555",     # фоновый цвет кнопки
             foreground="#ccc",     # цвет текста
             font="16",              # высота шрифта
            command= click_button3,
            image = photo_image3


             )
cap_button.pack()
latte_button = Button(root,text="Latte - 20грн", # текст кнопки
             background="#555",     # фоновый цвет кнопки
             foreground="#ccc",     # цвет текста
             font="16",              # высота шрифта
            command= click_button4,
            image = photo_image4
             )
latte_button.pack()
details_button = Button(root,text="Show details", # текст кнопки
             background="#555",     # фоновый цвет кнопки
             foreground="#ccc",     # цвет текста
             font="16",              # высота шрифта
            command= click_button5,
            image = photo_image5
             )
details_button.pack(side = BOTTOM)

mainloop()