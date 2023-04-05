import tkinter as tk
import math


class Calculator:
    def __init__(self, master):
        self.master = master
        master.title("klakaliator")

        self.display = tk.Entry(master, width=20)
        self.display.grid(row=0, columnspan=4)

        self.bind_keys()

        self.create_button("7", 2, 0)
        self.create_button("8", 2, 1)
        self.create_button("9", 2, 2)
        self.create_button("/", 1, 3)

        self.create_button("4", 3, 0)
        self.create_button("5", 3, 1)
        self.create_button("6", 3, 2)
        self.create_button("*", 2, 3)

        self.create_button("1", 4, 0)
        self.create_button("2", 4, 1)
        self.create_button("3", 4, 2)
        self.create_button("-", 3, 3)

        self.create_button("0", 5, 1)
        self.create_button(".", 5, 0)
        self.create_button("+", 4, 3)

        self.create_button("C", 1, 0)
        self.create_button("(", 5, 2)
        self.create_button(")", 5, 3)

        self.create_equals_button("=")

        self.create_square_button("x\u00b2", 1, 1)
        self.create_sqrt_button("\u221ax", 1, 2)

    def add_to_field(self, sth):
        global field_text
        field_text = field_text+str(sth)

    def create_button(self, text, row, col):
        if text in '0123456789.':
            button = tk.Button(self.master, text=text, width=5, height=3, command=lambda: self.on_click(text))
            button.grid(row=row, column=col)
        else:
            button = tk.Button(self.master, text=text, width=5, height=3, command=lambda: self.on_click(text), bg='orange')
            button.grid(row=row, column=col)

    def bind_keys(self):

        self.master.bind('<Return>', lambda event: self.on_click('='))

        for i in range(10):
            self.master.bind(str(i), lambda event, i=str(i): self.on_click(i))

        for op in ['+', '-', '*', '/', '.']:
            self.master.bind(str(op), lambda event, i=str(op): self.on_click(i))



    def create_sqrt_button(self,text, row, col):
        button = tk.Button(self.master, text=text, width=5, height=3, command=lambda: self.sqrt(), bg='orange')
        button.grid(row=row, column=col)

    def create_square_button(self, text, row, col):
        button = tk.Button(self.master, text=text, width=5, height=3, command=lambda: self.square(), bg='orange')
        button.grid(row=row, column=col)

    def sqrt(self):
        result = math.sqrt(eval(self.display.get()))
        self.display.delete(0, tk.END)
        self.display.insert(tk.END, str(result))



    def square(self):
        result = eval(self.display.get())**2
        self.display.delete(0, tk.END)
        self.display.insert(tk.END, result)

    def create_equals_button(self,text):
        button = tk.Button(self.master, text=text, width=5, height=20, command=lambda: self.on_click(text), bg='orange')
        button.grid(row=1, rowspan=5, column=4, columnspan=4, sticky=tk.N)

    def on_click(self, text):
        if text == "=":
            try:
                result = eval(self.display.get())
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, str(result))
            except ZeroDivisionError:
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, "Error")

        elif text == "C":
            self.display.delete(0, tk.END)
        else:
            self.display.insert(tk.END, text)


root = tk.Tk()
master = Calculator(root)
root.mainloop()
