import re
import tkinter as tk
from tkinter import messagebox

class Calculator:
    def __init__(self, root):
        self.app = root
        self.win = tk.Toplevel(self.app)
        self.win.grab_set()
        self.win.geometry("500x500")
        self.win.title("Calculator")
        self.win.resizable(False, False)
        self.win.protocol("WM_DELETE_WINDOW", self.back_to_main)

        self.create_widgets()
        self.bind_number_buttons()
        
    def create_widgets(self):
        # Frame
        parent_frame = tk.Frame(self.win, width=500, height=500, bg="#102C57", bd=20, relief=tk.RIDGE)
        child_frame = tk.Frame(self.win, width=460, height=460, bg="#0065FF")
        
        # Ent
        self.ent_num_field = tk.Entry(
            child_frame,
            font=("katibeh", 26),
            width=22,
            justify="right"
        )
        
        self.ent_num_field.config(validate="key", validatecommand=(self.ent_num_field.register(lambda char: char.isdigit() or char == "" or char in "-+÷%.x(()"), "%S"))

        
        # Btn
        # Back Button
        self.btn_back = tk.Button(
            child_frame,
            text="<",
            font=("katibeh", 14, "bold"),
            bg="#102C57",
            fg="#fff",
            cursor="hand2",
            width=5,
            command=self.back_to_main
        )
        
        # Btn Row 1
        self.btn_open_parenthesis = tk.Button(
            child_frame,
            text="(",
            font=("katibeh", 18),
            width=5,
        )
        
        self.btn_close_parenthesis = tk.Button(
            child_frame,
            text=")",
            font=("katibeh", 18),
            width=5,
        )
        
        self.btn_ac = tk.Button(
            child_frame,
            text="AC",
            font=("katibeh", 18),
            width=5,
            command=self.clear
        )
        
        self.btn_del = tk.Button(
            child_frame,
            text="Del",
            font=("katibeh", 18),
            width=5,
            command=self.delete
        )
        
        # Btn Row 2       
        self.btn_7 = tk.Button(
            child_frame,
            text="7",
            font=("katibeh", 18),
            width=5,
        )
        
        self.btn_8 = tk.Button(
            child_frame,
            text="8"  ,
            font=("katibeh", 18),
            width=5,
        )
        
        self.btn_9 = tk.Button(
            child_frame,
            text=9,
            font=("katibeh", 18),
            width=5,
        )
        
        self.btn_divide = tk.Button(
            child_frame,
            text="÷",
            font=("katibeh", 18),
            width=5,
        )
        
        # Btn Row 3
        self.btn_4 = tk.Button(
            child_frame,
            text="4",
            font=("katibeh", 18),
            width=5,
        )
        
        self.btn_5 = tk.Button(
            child_frame,
            text="5",
            font=("katibeh", 18),
            width=5,
        )
        
        self.btn_6 = tk.Button(
            child_frame,
            text="6",
            font=("katibeh", 18),
            width=5,
        )
        
        self.btn_multiply = tk.Button(
            child_frame,
            text="x",
            font=("katibeh", 18),
            width=5,
        )
        
        # Btn Row 4
        self.btn_1 = tk.Button(
            child_frame,
            text="1",
            font=("katibeh", 18),
            width=5,
        )
        
        self.btn_2 = tk.Button(
            child_frame,
            text="2",
            font=("katibeh", 18),
            width=5,
        )
        
        self.btn_3 = tk.Button(
            child_frame,
            text="3",
            font=("katibeh", 18),
            width=5,
        )
        
        self.btn_subtract = tk.Button(
            child_frame,
            text="-",
            font=("katibeh", 18),
            width=5,
        )
        
        # Btn Row 5
        self.btn_0 = tk.Button(
            child_frame,
            text="0",
            font=("katibeh", 18),
            width=12,
        )        
        
        self.btn_equal = tk.Button(
            child_frame,
            text="=",
            font=("katibeh", 18),
            bg="#90EE90",
            width=5,
            command=self.calculate
        )
        
        self.btn_addition = tk.Button(
            child_frame,
            text="+",
            font=("katibeh", 18),
            width=5,
        )
        
        # Widgets Pos
        # Frame pos
        parent_frame.place(x=0, y=0)
        child_frame.place(x=20, y=20)
        
        # Ent pos
        self.ent_num_field.place(x=20, y=50)
        
        # Btn pos
        # Back Button
        self.btn_back.place(x=10, y=5)
        
        # Btn Row 1
        self.btn_open_parenthesis.place(x=40, y=120)
        self.btn_close_parenthesis.place(x=140, y=120)
        self.btn_ac.place(x=240, y=120)
        self.btn_del.place(x=340, y=120)
        
        
        # Btn Row 2
        self.btn_7.place(x=40, y=190)
        self.btn_8.place(x=140, y=190)
        self.btn_9.place(x=240, y=190)
        self.btn_divide.place(x=340, y=190)
        
        # Btn Row 3
        self.btn_4.place(x=40, y=260)
        self.btn_5.place(x=140, y=260)
        self.btn_6.place(x=240, y=260)
        self.btn_multiply.place(x=340, y=260)
        
        # Btn Row 4
        self.btn_1.place(x=40, y=330)
        self.btn_2.place(x=140, y=330)
        self.btn_3.place(x=240, y=330)
        self.btn_subtract.place(x=340, y=330)
        
        # Btn Row 5
        self.btn_0.place(x=40, y=400)
        self.btn_equal.place(x=240, y=400)
        self.btn_addition.place(x=340, y=400)
    
    def bind_number_buttons(self):
        # Bind number buttons to insert corresponding numbers
        for num_button in [
            self.btn_0,
            self.btn_1,
            self.btn_2,
            self.btn_3,
            self.btn_4,
            self.btn_5,
            self.btn_6,
            self.btn_7,
            self.btn_8,
            self.btn_9,
            self.btn_addition,
            self.btn_subtract,
            self.btn_divide,
            self.btn_multiply,
            self.btn_open_parenthesis,
            self.btn_close_parenthesis]:
            num_button.bind("<Button-1>", self.insert_number)
    
    def insert_number(self, event):
        # Get the currently focused entry
        focused_widget = self.app.focus_get()

        # If it's an entry field, insert the corresponding number
        if isinstance(focused_widget, tk.Entry):
            cursor_pos = focused_widget.index(tk.INSERT)  # Get the cursor position
            focused_widget.insert(cursor_pos, event.widget["text"])  # Insert the number at the cursor position           
                
    # Calculator Function
    def clear(self):
        # Temporarily disable validation
        self.ent_num_field.config(validate="none")
        # Delete Chars int Ent Field
        self.ent_num_field.delete(0, tk.END)
        # Re-enable validation
        self.ent_num_field.config(validate="key", validatecommand=(self.ent_num_field.register(lambda char: char.isdigit() or char in "-+÷%x()" or char == ""), "%S"))    
    
    
    def delete(self):
        focused_widget = self.app.focus_get()
        
        if isinstance(focused_widget, tk.Entry) and focused_widget == self.ent_num_field:
            cursor_pos = focused_widget.index(tk.INSERT)  # Get the cursor position
            if cursor_pos > 0:
                focused_widget.delete(cursor_pos - 1)  # Delete one character before the cursor position

        
        # expression = self.ent_num_field.get()
        # back = expression[:-1]
        # self.clear()
        # self.ent_num_field.config(validate="none")
        # self.ent_num_field.insert(0, back)
        # self.ent_num_field.config(validate="key", validatecommand=(self.ent_num_field.register(lambda char: char.isdigit() or char in "-+÷%x()" or char == ""), "%S")) 
        
    def calculate(self):
        try:
            expression = self.ent_num_field.get()
            if expression != "":
                expression = re.sub(r'(\d+)(\()', r'\1*\2', expression)
                expression = re.sub(r'(\))(\d+)', r'\1*\2', expression)
        
                expression = expression.replace("÷", "/")
                expression = expression.replace("x", "*")
                result = eval(expression)
                self.clear()
                self.ent_num_field.config(validate="none")               
                self.ent_num_field.insert(tk.END, str(result))
                self.ent_num_field.config(validate="key", validatecommand=(self.ent_num_field.register(lambda char: char.isdigit() or char in "-+÷%x()" or char == ""), "%S")) 
                

        except ZeroDivisionError:
            messagebox.showerror('Error', "Division by zero is not allowed.")
            self.clear()
        except SyntaxError:
            messagebox.showerror('Error', "Invalid Syntax")
            self.clear()
            
    def back_to_main(self):
        self.win.destroy()   
        
        