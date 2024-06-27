import tkinter as tk

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")
        self.expression = ""

        self.input_text = tk.StringVar()
        self.input_frame = self.create_input_frame()
        self.buttons_frame = self.create_buttons_frame()

        self.input_frame.pack()
        self.buttons_frame.pack()

        self.create_buttons()

    def create_input_frame(self):
        frame = tk.Frame(self.root)
        input_field = tk.Entry(frame, textvariable=self.input_text, font=('Arial', 18), bd=5, insertwidth=4, width=14, borderwidth=4)
        input_field.grid(row=0, column=0)
        return frame

    def create_buttons_frame(self):
        frame = tk.Frame(self.root)
        return frame

    def create_buttons(self):
        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('C', 4, 0), ('0', 4, 1), ('=', 4, 2), ('+', 4, 3)
        ]

        for (text, row, col) in buttons:
            button = tk.Button(self.buttons_frame, text=text, font=('Arial', 18), fg='black', height=3, width=9, 
                               command=lambda txt=text: self.on_button_click(txt))
            button.grid(row=row, column=col)

    def on_button_click(self, character):
        if character == "C":
            self.expression = ""
        elif character == "=":
            try:
                self.expression = str(eval(self.expression))
                
            except:
                self.expression = "Error"
        else:
            self.expression += str(character)
        self.input_text.set(self.expression)

if __name__ == "__main__":
    root = tk.Tk()
    calculator = Calculator(root)
    root.mainloop()
