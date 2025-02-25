from tkinter import *

m = Tk()
m.geometry("500x600")  
m.option_add("font", "consolas 20")

Label_show_cal = StringVar()
Label_show_cal.set("0")
expresstion = ""

def clear():
    global expresstion
    expresstion = ""
    Label_show_cal.set("0")

def press(number):
    global expresstion
    if expresstion == "0" or Label_show_cal.get() == "Error":
        expresstion = str(number)
    else:
        expresstion += str(number)
    Label_show_cal.set(expresstion)

def equal():
    global expresstion
    try:
        result = str(eval(expresstion))
        Label_show_cal.set(result)
        expresstion = result
    except:
        Label_show_cal.set("Error")
        expresstion = "0"

for i in range(4):
    m.grid_columnconfigure(i, weight=1)

for i in range(6):
    m.grid_rowconfigure(i, weight=1)

Label(m, textvariable=Label_show_cal, height=2, font=("consolas", 40), anchor="e", bg="white").grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky="nsew")

Button(m, text="clear", command=clear).grid(row=1, column=2, columnspan=2, padx=5, pady=5, sticky="nsew")

buttons = [
    ("7", 2, 0), ("8", 2, 1), ("9", 2, 2), ("/", 2, 3),
    ("4", 3, 0), ("5", 3, 1), ("6", 3, 2), ("*", 3, 3),
    ("1", 4, 0), ("2", 4, 1), ("3", 4, 2), ("-", 4, 3),
    ("0", 5, 0), (".", 5, 1), ("=", 5, 2, equal), ("+", 5, 3)
]

for item in buttons:
    if len(item) == 3:
        text, row, col = item
        command = lambda t=text: press(t)
    else:
        text, row, col, command = item

    Button(m, text=text, command=command).grid(row=row, column=col, padx=5, pady=5, sticky="nsew")

m.mainloop()
