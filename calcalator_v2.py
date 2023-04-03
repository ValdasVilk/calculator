import tkinter
import tkinter.messagebox
import customtkinter
import math

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")


class Calculator(customtkinter.CTk):

    def __init__(self):
        super().__init__()

        self.title("Kalkaliatorius")
        self.geometry("560x250")

        self.display = customtkinter.CTkEntry(master=self, width=200, height=25)
        self.display.grid(row=0, column=0, columnspan=4)

        self.output_label = customtkinter.CTkLabel(master=self,text=str(self.on_click()), width=200, height=25)
        self.output_label.grid(row=7, column=9, columnspan=4)

        self.total_expression = ""
        self.current_expression = ""

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
        self.create_button("=", 6, 0)
        self.create_button("\u221ax", 1, 1)
        self.create_button("x\u00b2", 1, 2)

        self.bind_keys()

        self.create_display_labels()
        self.create_display_labels()

    def create_display_frame(self):
        frame = customtkinter.CTkFrame(self, height=221)
        frame.grid()

    def create_display_labels(self):
        total_label = customtkinter.CTkLabel(self, text=self.total_expression, anchor=customtkinter.E,  padx=24)
        total_label.grid()

        label = customtkinter.CTkLabel(self, text=self.current_expression, anchor=customtkinter.E, padx=24)
        label.grid()

    def create_button(self, text, row, col):

        if text in '0123456789':
            button = customtkinter.CTkButton(master=self, text=text,  width=50, height=25, command=lambda: self.on_click(text))
            button.grid(row=row, column=col)
        elif text in "=":
            button = customtkinter.CTkButton(master=self, text=text, width=200, height=25, command=lambda: self.on_click(text))
            button.grid(row=row, column=col, columnspan=5)
        elif text in "\u221ax":
            button = customtkinter.CTkButton(master=self, text=text, width=50, height=25, command=lambda: self.sqrt())
            button.grid(row=row, column=col)
        elif text in "x\u00b2":
            button = customtkinter.CTkButton(master=self, text=text, width=50, height=25, command=lambda: self.square())
            button.grid(row=row, column=col)
        else:
            button = customtkinter.CTkButton(master=self, text=text,  width=50, height=25, command=lambda: self.on_click(text))
            button.grid(row=row, column=col)
    def square(self):
        result = eval(self.display.get()) ** 2

        self.display.delete(0, customtkinter.END)
        self.display.insert(customtkinter.END, result)

    def sqrt(self):
        result = math.sqrt(eval(self.display.get()))
        self.display.delete(0, customtkinter.END)
        self.display.insert(customtkinter.END, result)


    def on_click(self, text):
        if text == "=":
            try:
                result = eval(self.display.config())
                self.display.delete(0, customtkinter.END)
                self.display.insert(customtkinter.END, str(result))
            except ZeroDivisionError:
                self.display.delete(0, customtkinter.END)
                self.display.insert(customtkinter.END, "Error")

        elif text == "C":
            self.display.delete(0, customtkinter.END)
        else:
            self.display.insert(customtkinter.END, text)

    def bind_keys(self):

        self.bind('<Return>', lambda event: self.on_click('='))

        for i in range(10):
            self.bind(str(i), lambda event, i=str(i): self.on_click(i))

        for op in ['+', '-', '*', '/', '.']:
            self.bind(str(op), lambda event, i=str(op): self.on_click(i))



if __name__ == "__main__":
    app = Calculator()
    app.mainloop()

