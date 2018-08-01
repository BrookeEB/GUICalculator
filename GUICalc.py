from tkinter import *
# tkinter is the TK GUI toolkit. In order for the GUI of this program to work, tkinter
# must be imported into the program.

# Design of the GUI. This portion determines the layout of the calculator. This includes:
# the title (color, font, size, etc.) and the size of the window for the calculator.
me = Tk()
me.geometry("354x460")
me.title("Python GUI Calculator")
melabel = Label(me, text="Calculator", fg="White", bg="Black", font=("Times", 25, 'bold'))
melabel.pack(side=TOP)
me.config(background='Black')

textin = StringVar()
operator = ""

# Functions for buttons on the calculator. These determine what the buttons will be doing and are connected
# to the math function buttons at the bottom of this code.

def clickbut(numbers):
    global operator
    operator = operator + str(numbers)
    textin.set(operator)


def equlbut():
    global operator
    add = str(eval(operator))
    textin.set(add)
    operator = ''


def equlbut():
    global operator
    sub = str(eval(operator))
    textin.set(sub)
    operator = ''


def equlbut():
    global operator
    mul = str(eval(operator))
    textin.set(mul)
    operator = ''


def equlbut():
    global operator
    div = str(eval(operator))
    textin.set(div)
    operator = ''


def clrbut():
    textin.set('')

