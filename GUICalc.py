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

# Button function, design, and placement for the inputs: numbers 0 - 9.

metext = Entry(me, font=("Times", 12, 'bold'), textvar=textin, width=25, bd=5, bg='powder blue')
metext.pack()

but1 = Button(me, padx=14, pady=14, bd=4, bg='light yellow', command=lambda: clickbut(1), text="1",
              font=("Times", 14, 'bold'))
but1.place(x=10, y=100)

but2 = Button(me, padx=14, pady=14, bd=4, bg='light yellow', command=lambda: clickbut(2), text="2",
              font=("Times", 14, 'bold'))
but2.place(x=10, y=170)

but3 = Button(me, padx=14, pady=14, bd=4, bg='light yellow', command=lambda: clickbut(3), text="3",
              font=("Times", 14, 'bold'))
but3.place(x=10, y=240)

but4 = Button(me, padx=14, pady=14, bd=4, bg='light yellow', command=lambda: clickbut(4), text="4",
              font=("Times", 14, 'bold'))
but4.place(x=75, y=100)

but5 = Button(me, padx=14, pady=14, bd=4, bg='light yellow', command=lambda: clickbut(5), text="5",
              font=("Times", 14, 'bold'))
but5.place(x=75, y=170)

but6 = Button(me, padx=14, pady=14, bd=4, bg='light yellow', command=lambda: clickbut(6), text="6",
              font=("Times", 14, 'bold'))
but6.place(x=75, y=240)

but7 = Button(me, padx=14, pady=14, bd=4, bg='light yellow', command=lambda: clickbut(7), text="7",
              font=("Times", 14, 'bold'))
but7.place(x=140, y=100)

but8 = Button(me, padx=14, pady=14, bd=4, bg='light yellow', command=lambda: clickbut(8), text="8",
              font=("Times", 14, 'bold'))
but8.place(x=140, y=170)

but9 = Button(me, padx=14, pady=14, bd=4, bg='light yellow', command=lambda: clickbut(9), text="9",
              font=("Times", 14, 'bold'))
but9.place(x=140, y=240)

but0 = Button(me, padx=14, pady=14, bd=4, bg='light yellow', command=lambda: clickbut(0), text="0",
              font=("Times", 14, 'bold'))
but0.place(x=10, y=310)

# These buttons are the calculating buttons. This calculator does simple math. The lambda function is used
# to run the division, multiplication, addition, and subtraction functions. Each button is given a design
# and placement on the GUI.

butdot = Button(me, padx=48.5, pady=13, bd=4, bg='Dark gray', command=lambda: clickbut("."), text=".",
                font=("Times", 15, 'bold'))
butdot.place(x=75, y=310)

butpl = Button(me, padx=17, pady=16.5, bd=4, bg='Dark gray', text="+", command=lambda: clickbut("+"),
               font=("Times", 12, 'bold'))
butpl.place(x=205, y=100)

butsub = Button(me, padx=17, pady=14, bd=4, bg='Dark gray', text="-", command=lambda: clickbut("-"),
                font=("Times", 14, 'bold'))
butsub.place(x=205, y=170)

butml = Button(me, padx=17, pady=16, bd=4, bg='Dark gray', text="*", command=lambda: clickbut("*"),
               font=("Times", 12, 'bold'))
butml.place(x=205, y=241)

butdiv = Button(me, padx=17.5, pady=16.5, bd=4, bg='Dark gray', text="/", command=lambda: clickbut("/"),
                font=("Times", 12, 'bold'))
butdiv.place(x=205, y=310)

butclear = Button(me, padx=14, pady=117.4, bd=4, bg='red', text="CE", command=clrbut, font=("Times", 16, 'bold'))
butclear.place(x=270, y=100)

butequal = Button(me, padx=155.5, pady=14, bd=4, bg='gray', command=equlbut, text="=", font=("Times", 12, 'bold'))
butequal.place(x=10, y=380)
