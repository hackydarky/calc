import tkinter as tk

LIGHT_GRAY = "#F5F5F5"
LABEL_COLOR = "#25265E"
WHITE = "#FFFFFF"
OFF_WHITE = "#F8FAFF"
LIGHT_BLUE = "#CCEDFF"

DEFAULT_FONT_STYLE = ("Arial", 20)
DIGITS_FONT_STYLE = ("Arial", 24, "bold")
SMALL_FONT_STYLE = ("Arial", 16)
LARGE_FONT_STYLE = ("Arial", 50, "bold")


class Calculator:
    def __init__(self):
        self.window = tk.Tk()
        self.window.geometry("375x500")
        # self.window.resizable(0, 0)
        self.window.title("calc")
        self.total_expression = ""
        self.current_expression = ""
        self.display_frame = self.create_display_frame()
        self.buttons_frame = self.create_buttons_frame()
        self.total_label, self.label = self.create_display_labels()
        self.digits = {
            7: (1, 2),
            8: (1, 3),
            9: (1, 4),
            4: (2, 2),
            5: (2, 3),
            6: (2, 4),
            1: (3, 2),
            2: (3, 3),
            3: (3, 4),
            ".": (4, 2),
            0: (4, 3)
        }
        self.create_digit_buttons()
        self.operations = {"/": "\u00F7", "*": "\u00D7", "+": "+", "-": "-"}
        self.create_operation_buttons()
        self.create_special_buttons()
        self.buttons_frame.rowconfigure(0, weight=1)
        for i in range(1, 5):
            self.buttons_frame.rowconfigure(i, weight=1)
            self.buttons_frame.columnconfigure(i, weight=1)

    def create_special_buttons(self):
        self.sqrt_button()
        self.dlt_button()
        self.sqre_button()
        self.cube_button()
        self.eqls_button()

    def sqrt_button(self):
        button = tk.Button(self.buttons_frame,
                           text="\u221ax",
                           bg=OFF_WHITE,
                           fg=LABEL_COLOR,
                           font=DEFAULT_FONT_STYLE,
                           borderwidth=0,
                           command=self.sqrt)
        button.grid(row=0, column=3, sticky=tk.NSEW)

    def dlt_button(self):
        button = tk.Button(self.buttons_frame,
                           text="\u232b",
                           bg=OFF_WHITE,
                           fg=LABEL_COLOR,
                           font=DEFAULT_FONT_STYLE,
                           borderwidth=0,
                           command=self.dlt)
        button.grid(row=0, column=4, sticky=tk.NSEW)

    def sqre_button(self):
        button = tk.Button(self.buttons_frame,
                           text="x\u00b2",
                           bg=OFF_WHITE,
                           fg=LABEL_COLOR,
                           font=DEFAULT_FONT_STYLE,
                           borderwidth=0,
                           command=self.sqre)
        button.grid(row=0, column=2, sticky=tk.NSEW)

    def cube_button(self):
        button = tk.Button(self.buttons_frame,
                           text="x\u00b3",
                           bg=OFF_WHITE,
                           fg=LABEL_COLOR,
                           font=DEFAULT_FONT_STYLE,
                           borderwidth=0,
                           command=self.cube)
        button.grid(row=0, column=1, sticky=tk.NSEW)

    def eqls_button(self):
        button = tk.Button(self.buttons_frame,
                           text="=",
                           bg=OFF_WHITE,
                           fg=LABEL_COLOR,
                           font=DEFAULT_FONT_STYLE,
                           borderwidth=0,
                           command=self.eqls)
        button.grid(row=4, column=4, sticky=tk.NSEW)

    def create_operation_buttons(self):
        i = 1
        for operator, symbol in self.operations.items():
            button = tk.Button(
                self.buttons_frame,
                text=symbol,
                bg=OFF_WHITE,
                fg=LABEL_COLOR,
                font=DEFAULT_FONT_STYLE,
                borderwidth=0,
                command=lambda x=operator: self.append_operator(x))
            button.grid(row=i, column=1, sticky=tk.NSEW)
            i += 1

    def create_digit_buttons(self):
        for digit, grid_value in self.digits.items():
            button = tk.Button(
                self.buttons_frame,
                text=str(digit),
                bg=OFF_WHITE,
                fg=LABEL_COLOR,
                font=DEFAULT_FONT_STYLE,
                borderwidth=0,
                command=lambda x=digit: self.add_to_expressions(x))
            button.grid(row=grid_value[0],
                        column=grid_value[1],
                        sticky=tk.NSEW)

    def create_display_labels(self):
        total_label = tk.Label(self.display_frame,
                               text=self.total_expression,
                               anchor=tk.E,
                               bg=LIGHT_GRAY,
                               fg=LABEL_COLOR,
                               padx=24,
                               font=SMALL_FONT_STYLE)
        total_label.pack(expand=True, fill='both')

        label = tk.Label(self.display_frame,
                         text=self.current_expression,
                         anchor=tk.E,
                         bg=LIGHT_GRAY,
                         fg=LABEL_COLOR,
                         padx=24,
                         font=LARGE_FONT_STYLE)
        label.pack(expand=True, fill='both')
        return total_label, label

    def create_display_frame(self):
        frame = tk.Frame(self.window, height=500, bg=LIGHT_GRAY)
        frame.pack(expand=True, fill="both")
        return frame

    def create_buttons_frame(self):
        frame = tk.Frame(self.window)
        frame.pack(expand=True, fill="both")
        return frame

    def sqrt(self):
        self.current_expression = str(eval(f"{self.current_expression}**0.5"))
        self.update_label()

    def sqre(self):
        self.current_expression = str(eval(f"{self.current_expression}**2"))
        self.update_label()

    def cube(self):
        self.current_expression = str(eval(f"{self.current_expression}**3"))
        self.update_label()

    def dlt(self):
        self.total_expression = ""
        self.current_expression = ""
        self.update_label()
        self.update_total_label()

    def eqls(self):
        self.total_expression += self.current_expression
        self.update_total_label()
        try:
            self.current_expression = str(eval(self.total_expression))
            self.total_expression = ""
        except ZeroDivisionError:
            self.current_expression = "error"
        finally:
            self.update_label()

    def append_operator(self, operator):
        self.current_expression += operator
        self.total_expression += self.current_expression
        self.current_expression = ""
        self.update_label()
        self.update_total_label()

    def add_to_expressions(self, value):
        self.current_expression += str(value)
        self.update_label()

    def update_label(self):
        self.label.config(text=self.current_expression)

    def update_total_label(self):
        self.total_label.config(text=self.total_expression)

    def run(self):
        self.window.mainloop()


if __name__ == "__main__":
    calc = Calculator()
    calc.run()
