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

