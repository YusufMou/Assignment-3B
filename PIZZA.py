# Created by: Yusuf Moussa
# Created on: 22 Feb 2019
# Created for: ICS3U
# Assignment 3B
# This program Calculates the cost of a pizza


from tkinter import *


#Variables
root = Tk()
root.geometry("500x300")
integer = IntVar()
integer.set(0)
intejer = IntVar()
intejer.set(0)
Ex = 0
La = 0
p = 0
tax = 0.13
#Functions

def Pselec ():
    L = Label(root, text="Large Pizza").grid(row=1,column=1)
    E = Label(root, text="Extra large Pizza").grid(row=2,column=1)
    T = Label(root, text="Number of Toppings").grid(row=3, column=1)
                                                    
def add_one():
    x =  integer.get() + 1
    integer.set(x)

def take_one():
    x =  integer.get() - 1
    if x >= 0:
        integer.set(x)
    else:
        integer.set(0)

def plus_one():
    y = intejer.get() + 1
    intejer.set(y)
    
def minus_one():
    y = intejer.get() - 1
    if y >= 0:
        intejer.set(y) 
    else:
        intejer.set(0)

def top():
    t = int(topping.get())
    global p
    if t == 1:
        p = 1.00
        #global p
        Label(root, text="The price for toppings is $" + str(p)).grid(row=4, column=1)
    elif t == 2:
        p = 1.75
        #global p
        Label(root, text="The price for toppings is $" + str(p)).grid(row=4, column=1)
    elif t == 3:
        p = 2.50
        #global p
        Label(root, text="The price for toppings is $" + str(p)).grid(row=4, column=1)
    else:
        #global p
        p = 3.25
        Label(root, text="The price for toppings is $" + str(p)).grid(row=4, column=1)
        
def piz():
    global Ex
    Ex = int(intejer.get()) * 10.00
    global La
    La = int(integer.get()) * 6.00
    Label(root, text="The price for the pizza is $" + str(Ex + La)).grid(row=5, column=1)        
         
         
def total():
    total = Ex + La + p*tax 
    Label(root, text="The total is $" + str(total)).grid(row=7, column=1)                                         
#amount of content needed
entry1 = Entry(root, textvariable=str(integer), width=4)
entry1.grid(row=1, column=3)

entry2 = Entry(root, textvariable=str(intejer), width=4)
entry2.grid(row=2, column=3)

topping = Scale(root, orient=HORIZONTAL, from_=1, to=4)
topping.grid(row=3, column=3)

#add substract button
Button(root, text='+', command=add_one).grid(row=1, column=4)
Button(root, text='-', command=take_one).grid(row=1, column=5)

Button(root, text='+', command=plus_one).grid(row=2, column=4)
Button(root, text='-', command=minus_one).grid(row=2, column=5)

Button(root, text='Toppings', command=top).grid(row=3, column=4)

Button(root, text='Pizza', command=piz).grid(row=2, column=6)

Button(root, text='Total', command=total).grid(row=6, column=1)
Pselec()

root.mainloop()
