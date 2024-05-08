import tkinter as tk
from tkinter import ttk, Toplevel, messagebox
from datetime import datetime, timedelta


# Function to create a new window for add button
def add_button(window):
    new_window = Toplevel(window)
    new_window.title("Add Items")
    new_window.geometry("400x300")
    new_window.config(bg="#102C57")

    # Frames
    frame = ttk.Frame(new_window, style="New.TFrame", width=340, height=230)

    frame.place(x=30, y=30)

    # Lbl
    ttk.Label(frame, text="Category:", font=("katibeh", 16, "bold"), background="#EADBC8").place(x=10, y=20)
    ttk.Label(frame, text="Name:", font=("katibeh", 16, "bold"), background="#EADBC8").place(x=10, y=60)
    ttk.Label(frame, text="Amount:", font=("katibeh", 16, "bold"), background="#EADBC8").place(x=10, y=100)

    # Category ComboBox
    ent_category = ttk.Combobox(frame, values=["Income", "Expense"], font=("katibeh", 16), width=12)

    ent_category.set("Expense")

    # Entry
    ent_name = ttk.Entry(frame, font=("katibeh", 16), width=16)

    ent_amount = ttk.Entry( frame, font=("katibeh", 16), width=14)

    ent_category.place(x=130, y=20)
    ent_name.place(x=90, y=60)
    ent_amount.place(x=110, y=100)

    # Add Button
    btn_add = tk.Button(frame, text="Add", font=("katibeh", 16), width=9, command=self.add_to_db)
    
    btn_add.place(x=110, y=170)
    
    
    
    
    
    
    
    
    
    
    
    
    
# App Window PopUps
def add_entry_win(self):
    self.add_window = tk.Toplevel(self)
    self.add_window.title("Add Items")
    self.add_window.geometry("400x300")
    self.add_window.config(bg="#102C57")
    self.add_window.resizable(False, False)
    self.add_window.grab_set()

    # Frames
    frame = tk.Frame(
        self.add_window,
        bg="#EADBC8",
        width=340,
        height=230
        )
    
    frame.place(x=30, y=30)

    # Lbl
    ttk.Label(frame, text="Category:", font=("katibeh", 16, "bold"), background="#EADBC8").place(x=10, y=20)
    ttk.Label(frame, text="Name:", font=("katibeh", 16, "bold"), background="#EADBC8").place(x=10, y=60)
    ttk.Label(frame, text="Amount:", font=("katibeh", 16, "bold"), background="#EADBC8").place(x=10, y=100)

    # Category ComboBox
    self.ent_category = ttk.Combobox(
        frame,
        values=["Income", "Expense"],
        font=("katibeh", 16),
        width=12,
        state="readonly"
    )
    
    self.ent_category.set("Expense")
    self.ent_category['validate'] = 'key'
    self.ent_category['validatecommand'] = (self.register(lambda text: text.isdigit() and text.isalpha() or text == ""), '%S')
    
    # Entry
    self.ent_name = ttk.Entry(
        frame,
        font=("katibeh", 16),
        width=16
        )
    
    self.ent_amount = ttk.Entry(
        frame,
        font=("katibeh", 16),
        width=14
        )
    
    self.ent_name.config(validate="key", validatecommand=(self.ent_name.register(lambda char: char.isalpha() or char == " "), "%S"))
    self.ent_amount.config(validate="key", validatecommand=(self.ent_amount.register(lambda char: char.isdigit() or char == ""), '%S'))

    self.ent_category.place(x=130, y=20)
    self.ent_name.place(x=90, y=60)
    self.ent_amount.place(x=110, y=100)

    # Add Button
    btn_add = tk.Button(
        frame,
        text="Add",
        font=("katibeh", 16),
        width=9,
        cursor="hand2",
        command=self.add_to_db
        )
    
    # Cance Add Button
    btn_cancel_add = tk.Button(
        frame,
        text="Cancel",
        font=("katibeh", 16),
        width=9,
        cursor="hand2",
        command=self.add_window.destroy
        )
    
    btn_add.place(x=40, y=170)
    btn_cancel_add.place(x=170, y=170)
    











# App Window PopUp Functions
# Add data to Database
def add_to_db(self):
    date = self.current_date.get()
    category = self.ent_category.get()
    name = self.ent_name.get()         
    amount = self.ent_amount.get() 

    if date and category and amount:
        try:
            amount = float(amount)               
            db.add_data_to_table(date, category, name, amount)
            
            self.add_window.destroy()
            self.load_entries()
            self.update_total_balance()
            
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid amount")
    else:
        messagebox.showerror("Error", "Please fill in all fields")















def previous_date(self):
    # Get current date displayed and minus one day to get previous date
    current = datetime.strptime(self.current_date.get(), "%B %d, %Y")
    new_date = current - timedelta(days=1)
    self.current_date.set(new_date.strftime("%B %d, %Y"))
    
    # Enable the "Next" button if it was disabled before
    self.btn_date_next.config(state="normal")
    self.load_entries()
    self.update_amount_label()

def next_date(self):
    # Get current date displayed and add one day to get next date
    current = datetime.strptime(self.current_date.get(), "%B %d, %Y")
    new_date = current + timedelta(days=1)
    self.current_date.set(new_date.strftime("%B %d, %Y"))
    
    # Check if the current date is today, if yes, disable the "Next" button
    today = datetime.now().strftime("%B %d, %Y")
    if self.current_date.get() == today:
        self.btn_date_next.config(state="disabled")
    self.load_entries()
    self.update_amount_label()
