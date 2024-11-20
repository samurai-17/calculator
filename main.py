import re
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox


def kv():
    a = float(e.get())
    e.delete(0, tk.END)
    b = a**2
    e.insert(0, b)


def delel():
    a = e.get()
    e.delete(0, tk.END)
    m = [a[i:i+1] for i in range(0, len(a), 1)]
    m.pop()
    b = ""
    for i in range(len(a) - 1):
        b += m[i]
    e.insert(0, b)


def dele():
    e.delete(0, tk.END)


def add_digit(digit):
    value = (e.get() + str(digit))
    e.delete(0, tk.END)
    e.insert(0, value)


def add_let(let):
    value = e.get() + str(let)
    e.delete(0, tk.END)
    e.insert(0, value)


def res():
    value = e.get()
    try:
        if '+' in value:
            result = value.split('+')
            er = float(result[0]) + float(result[1])
            e.delete(0, tk.END)
            e.insert(0, er)
        elif '*' in value:
            result = value.split('*')
            er = float(result[0]) * float(result[1])
            e.delete(0, tk.END)
            e.insert(0, er)
        elif '-' in value:
            result = value.split('-')
            er = float(result[0]) - float(result[1])
            e.delete(0, tk.END)
            e.insert(0, er)
        elif '/' in value:
            result = value.split('/')
            er = float(result[0]) / float(result[1])
            e.delete(0, tk.END)
            e.insert(0, er)
    except ValueError:
        messagebox.showerror("Ошибка", "Недостаточно аргументов")
    except ZeroDivisionError:
        messagebox.showerror("Ошибка", "Деление на ноль")



root = tk.Tk()
root.title("Калькулятор")
x = (root.winfo_screenwidth() - root.winfo_reqwidth()) / 2
y = (root.winfo_screenheight() - root.winfo_reqheight()) / 2
root.wm_geometry("+%d+%d" % (x, y))

e = tk.Entry(root, justify=tk.RIGHT)
e.grid(row=0, column=0, columnspan=6, stick='we')

tk.Button(text="1", bd=5, command=lambda : add_digit(1)).grid(row=1, column=0, stick='wens', padx='5', pady='5')
tk.Button(text="2", bd=5, command=lambda : add_digit(2)).grid(row=1, column=1, stick='wens', padx='5', pady='5')
tk.Button(text="3", bd=5, command=lambda : add_digit(3)).grid(row=1, column=2, stick='wens', padx='5', pady='5')
tk.Button(text="4", bd=5, command=lambda : add_digit(4)).grid(row=2, column=0, stick='wens', padx='5', pady='5')
tk.Button(text="5", bd=5, command=lambda : add_digit(5)).grid(row=2, column=1, stick='wens', padx='5', pady='5')
tk.Button(text="6", bd=5, command=lambda : add_digit(6)).grid(row=2, column=2, stick='wens', padx='5', pady='5')
tk.Button(text="7", bd=5, command=lambda : add_digit(7)).grid(row=3, column=0, stick='wens', padx='5', pady='5')
tk.Button(text="8", bd=5, command=lambda : add_digit(8)).grid(row=3, column=1, stick='wens', padx='5', pady='5')
tk.Button(text="9", bd=5, command=lambda : add_digit(9)).grid(row=3, column=2, stick='wens', padx='5', pady='5')
tk.Button(text="0", bd=5, command=lambda : add_digit(0)).grid(row=4, column=0, stick='wens', padx='5', pady='5')
tk.Button(text="=", bd=5, command=lambda : res()).grid(row=4, column=1, columnspan=2, stick='wens', padx='5', pady='5')
tk.Button(text="+", bd=5, command=lambda : add_let("+")).grid(row=1, column=3, stick='wens', padx='5', pady='5')
tk.Button(text="-", bd=5, command=lambda : add_let("-")).grid(row=2, column=3, stick='wens', padx='5', pady='5')
tk.Button(text="*", bd=5, command=lambda : add_let("*")).grid(row=3, column=3, stick='wens', padx='5', pady='5')
tk.Button(text="/", bd=5, command=lambda : add_let("/")).grid(row=4, column=3, stick='wens', padx='5', pady='5')
tk.Button(text="AC", bd=5, command=lambda : dele()).grid(row=1, column=4, stick='wens', padx='5', pady='5')
tk.Button(text=".", bd=5, command=lambda : add_let(".")).grid(row=2, column=4, stick='wens', padx='5', pady='5')
tk.Button(text="<--", bd=5, command=lambda : delel()).grid(row=3, column=4, stick='wens', padx='5', pady='5')
tk.Button(text="^", bd=5, command=lambda : kv()).grid(row=4, column=4, stick='wens', padx='5', pady='5')

root.grid_columnconfigure(0,minsize=60)
root.grid_columnconfigure(1,minsize=60)
root.grid_columnconfigure(2,minsize=60)
root.grid_columnconfigure(3,minsize=60)
root.grid_columnconfigure(4,minsize=60)

root.grid_rowconfigure(1,minsize=60)
root.grid_rowconfigure(2,minsize=60)
root.grid_rowconfigure(3,minsize=60)
root.grid_rowconfigure(4,minsize=60)

root.mainloop()