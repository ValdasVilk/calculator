import customtkinter
import math
import pickle


customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")


class Calculator(customtkinter.CTk):

    def __init__(self):
        super().__init__()

        self.title("Kalkaliatorius")
        self.geometry("500x500")
        self.resizable(True, True)

        self.display = customtkinter.CTkEntry(master=self, width=200, height=25)
        self.display.grid(row=0, column=0, columnspan=4)

        self.output_label = customtkinter.CTkLabel(master=self, text="result", width=120, height=25,
                                                   fg_color=("white", "gray75"),
                                                   corner_radius=8)
        self.output_label.grid(row=7, column=0, columnspan=5)

        self.history = customtkinter.CTkTextbox(master=self, wrap=None)
        self.history.grid(row=8, column=0, columnspan=5)

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

        self.create_button("DEL", 6, 0)

        self.bind_keys()

        self.clear_history_button = customtkinter.CTkButton(master=self, text="Clear History", width=120, height=25,
                                                            command=self.clear_history)
        self.clear_history_button.grid(row=9, column=0, columnspan=5)

    def create_button(self, text, row, col):

        if text in '0123456789':
            button = customtkinter.CTkButton(master=self, text=text,  width=50, height=25,
                                             command=lambda: self.on_click(text))
            button.grid(row=row, column=col)
        elif text == "=":
            button = customtkinter.CTkButton(master=self, text=text, width=150, height=25,
                                             command=lambda: self.on_click(text))
            button.grid(row=row, column=col, columnspan=5)
        elif text == "\u221ax":
            button = customtkinter.CTkButton(master=self, text=text, width=50, height=25,
                                             command=lambda: self.sqrt())
            button.grid(row=row, column=col)
        elif text == "x\u00b2":
            button = customtkinter.CTkButton(master=self, text=text, width=50, height=25,
                                             command=lambda: self.square())
            button.grid(row=row, column=col)
        else:
            button = customtkinter.CTkButton(master=self, text=text,  width=50, height=25,
                                             command=lambda: self.on_click(text))
            button.grid(row=row, column=col)

    def square(self):
        result = eval(self.display.get()) ** 2
        self.save_entry(entry_text=str(result))
        self.add_entry()
        self.load_history()

        self.display.delete(0, customtkinter.END)
        self.output_label.configure(text=result)

    def sqrt(self):
        result = math.sqrt(eval(self.display.get()))
        self.save_entry(entry_text=str(result))
        self.add_entry()
        self.load_history()
        self.display.delete(0, customtkinter.END)
        self.output_label.configure(text=result)

    def add_entry(self):
        entry_text = f"{self.display.get()} = "
        self.history.delete('1.0', 'end')
        self.history.insert('end', entry_text)
        self.save_entry(entry_text)

        self.display.delete(0, customtkinter.END)

    def save_entry(self, entry_text):
        with open('history.pickle', 'ab') as f:
            pickle.dump(entry_text, f)

    def load_history(self):
        self.history.delete('1.0', 'end')
        try:
            with open('history.pickle', 'rb') as f:
                while True:
                    try:
                        entry = pickle.load(f)
                        if isinstance(entry, str):
                            if '=' in entry:  # check if entry has an equals sign
                                operation, result = entry.split('=')
                                formatted_entry = f"{result.strip()} = {operation.strip()}"
                                self.history.insert(customtkinter.END, f"{formatted_entry}\n")
                            else:
                                self.history.insert(customtkinter.END, f"{entry}")
                    except EOFError:
                        break
        except FileNotFoundError:
            pass

    def clear_history(self):
        self.history.delete('1.0', 'end')
        with open('history.pickle', 'wb') as f:
            pass

    def on_click(self, text):
        if text == "=":
            try:
                result = eval(self.display.get())

                self.save_entry(entry_text=str(result))
                self.add_entry()
                self.load_history()

                self.display.delete(0, customtkinter.END)

            except ZeroDivisionError:
                self.display.delete(0, customtkinter.END)
                self.display.insert(customtkinter.END, "Error")
        elif text == "DEL":
            self.display.delete(len(self.display.get()[:-1]))
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
