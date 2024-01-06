from tkinter import *

calculation = ""


def button_press(symbol):
    global equation_text

    equation_text = equation_text + str(symbol)
    equation_label.set(equation_text)


def evaluate_calculation():
    global equation_text

    try:
        total = str(eval(equation_text))
        equation_label.set(total)
        equation_text = total
    except SyntaxError:
        equation_label.set("Syntax Error")
        equation_text = ""
    except ZeroDivisionError:
        equation_label.set("Arithmetic Error")
        equation_text = ""


def clear():
    global equation_text

    equation_label.set("")
    equation_text = ""


window = Tk()
window.title("Calculator")
window.geometry("400x450")

equation_text = ""

equation_label = StringVar()

label = Label(window, textvariable=equation_label, font=('ariel', 20), bg="white", width=24, height=3)
label.pack()

btns = []
btns_nmbr = -1

frame = Frame(window)
frame.pack()

clear = Button(frame, text="C", height=4, width=9, font=35, command=clear)
clear.grid(row=0, column=0)

for x in range(0, 3):
    for y in range(0, 3):
        btns_nmbr += 1
        btns.append(Button(frame, text=9 - btns_nmbr, height=4, width=9, font=35,
                           command=lambda btns_nmbr=btns_nmbr: button_press(9 - btns_nmbr)))
        btns[btns_nmbr].grid(row=x+1, column=2 - y)

button0 = Button(frame, text=0, height=4, width=9, font=35, command=lambda: button_press(0))
button0.grid(row=4, column=1)

add = Button(frame, text="+", height=4, width=9, font=35, command=lambda: button_press("+"))
add.grid(row=3, column=3)

subtract = Button(frame, text="-", height=4, width=9, font=35, command=lambda: button_press("-"))
subtract.grid(row=2, column=3)

multiply = Button(frame, text="x", height=4, width=9, font=35, command=lambda: button_press("*"))
multiply.grid(row=1, column=3)

divide = Button(frame, text="/", height=4, width=9, font=35, command=lambda: button_press("/"))
divide.grid(row=0, column=3)

equals = Button(frame, text="=", height=4, width=9, font=35, command=evaluate_calculation)
equals.grid(row=4, column=3)

decimal_point = Button(frame, text=".", height=4, width=9, font=35, command=lambda: button_press("."))
decimal_point.grid(row=4, column=2)

negative_num = Button(frame, text="(-", height=4, width=9, font=35, command=lambda: button_press("(-"))
negative_num.grid(row=4, column=0)

close_parentheses = Button(frame, text=")", height=4, width=9, font=35, command=lambda: button_press(")"))
close_parentheses.grid(row=0, column=2)

open_parentheses = Button(frame, text="(", height=4, width=9, font=35, command=lambda: button_press("("))
open_parentheses.grid(row=0, column=1)

window.mainloop()
