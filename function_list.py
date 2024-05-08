import tkinter as tk
import db
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
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
    btn_add = tk.Button(frame, text="Add", font=("katibeh", 16), width=9, command=add_to_db)
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
    



# App Functions Sections
# Date Functions
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






def load_entries(self):
    # Get current date
    current_date = self.current_date.get()

    # Load entries from the database for the current date
    self.entries = db.load_entries(current_date)

    # Clear existing entries in the Treeview
    for record in self.tv_tree_view.get_children():
        self.tv_tree_view.delete(record)

    # Insert loaded entries into the Treeview
    if self.entries:
        for entry in self.entries:
            # Extract entry details
            category = entry[2]
            amount = entry[4]

            # Format amount based on category
            if category == "Expense":
                formatted_amount = "-₱{:.2f}".format(abs(amount))  # Display negative amount
                text_color = "#FF0000"  # Red for expenses
            elif category == "Income":
                formatted_amount = "+₱{:.2f}".format(abs(amount))  # Display positive amount
                text_color = "#006400"  # Green for income
            else:
                formatted_amount = "₱{:.2f}".format(amount)  # Default format
                text_color = "#000000"  # Default color

            # Insert the entry into the Treeview with appropriate color and tag
            formatted_entry = (entry[1], entry[3], formatted_amount)  # Update amount in entry
            self.tv_tree_view.insert('', 'end', values=formatted_entry, tags=(category,))
            # Apply the color to the entire row
            self.tv_tree_view.tag_configure(category, foreground=text_color)

    self.update_amount_label()




# Update Income/Expense Amount label
def update_amount_label(self):
    total_expenses = 0
    total_income = 0
    if self.entries:
        for entry in self.entries:
            category = entry[2]
            amount = entry[4]

            if category == "Expense":
                total_expenses += amount
            elif category == "Income":
                total_income += amount

        # Update the expenses and income labels with the calculated totals
        self.lbl_expenses_amount.config(text="-₱{:.2f}".format(total_expenses))
        self.lbl_income_amount.config(text="+₱{:.2f}".format(total_income))
        self.update_total_balance()

    else:
        self.lbl_expenses_amount.config(text="-₱{:.2f}".format(total_expenses))
        self.lbl_income_amount.config(text="+₱{:.2f}".format(total_income))

# Get Total Balance
def update_total_balance(self):
        total_balance = db.total_amount()
        if total_balance is not None:  # Check if total_balance is not None
            self.lbl_balance_amount.config(text="₱{:.2f}".format(total_balance))
        else:
            self.lbl_balance_amount.config(text="₱0.00")


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
        
    self.option_num = 0
# Update Data to Database
def update_data_to_db(self):
    current_date = self.current_date.get()
    id = self.ent_update_id.get()
    name = self.ent_update_name.get()
    category = self.ent_update_category.get()
    amount = self.ent_update_amount.get()
    
    if id and name and category and amount:
        try:
            amount = float(amount)
            id_not_exist = db.update_data_in_table(id, name, category, amount, current_date)
            
            if id_not_exist:
                messagebox.showerror("Error", "Oopss, ID Does not Exist in Current Date")
            else:
                self.edit_entries_win.destroy()
                self.load_entries()
                self.update_total_balance()
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid values")
    else:
        messagebox.showerror("Error", "Please fill in all fields")
    
    self.option_num = 0    
# Delete Data       
def remove_data_from_db(self):
    current_date = self.current_date.get()
    id = self.ent_remove_id.get()
    
    id_not_exist = db.delete_data_in_table(id, current_date)
    
    if id:
        if id_not_exist:
            messagebox.showerror("Error", "Oops, ID Does Not Exist In Current Date")
        else:
            self.edit_entries_win.destroy()
            self.load_entries()
            self.update_total_balance()
    else:
        messagebox.showerror("Error", "Please fill in all fields")   
    
    self.option_num = 0                 
def clear_data(self):
    result = messagebox.askyesno("Clear Data", "Do you want to Delete All Data? Data cannot be recovered after deletion")
    
    if result:
        db.delete_all_data_in_table()
        self.load_entries()
        self.update_total_balance()
        self.menu_frame.place_forget()
        self.filter_treeview()
        self.create_chart_and_add_entries()
        messagebox.showinfo("Success", "Successfully Cleared Data")


# Update Entry Window Enable/Disable Displayed Widgets
def update_window(self):
    self.remove_frame.place_forget()
    self.update_frame.place(x=10, y=10)
    
    
# Remove Entry Window Enable/Disable Displayed Widgets
def remove_window(self):
    self.update_frame.place_forget()
    self.remove_frame.place(x=10, y=10)



def edit_entries_window(self):
    self.edit_entries_win = tk.Toplevel()
    self.edit_entries_win.title("Options")
    self.edit_entries_win.geometry("400x400")
    self.edit_entries_win.resizable(False, False)
    self.edit_entries_win.grab_set()

    # Frames
    frame1 = tk.Frame(self.edit_entries_win, height=100, width=400, bg="#102C57")
    frame2 = tk.Frame(self.edit_entries_win, height=300, width=400, bg="#EADBC8")
    self.update_frame = tk.Frame(frame2, height=280, width=380, bg="#102C57", bd=3, relief=tk.GROOVE)
    self.remove_frame = tk.Frame(frame2, height=280, width=380, bg="#102C57", bd=3, relief=tk.GROOVE)

    # Frame pos
    frame1.place(x=0, y=0)
    frame2.place(x=0, y=100)

    # Frame 1 Widgets
    # Btn
    btn_update = tk.Button(
        frame1,
        text="Update",
        font=("katibeh", 16),
        cursor="hand2",
        command=self.update_window
        )
    
    btn_remove = tk.Button(
        frame1,
        text="Remove",
        font=("katibeh", 16),
        cursor="hand2",
        command=self.remove_window
        )

    # Btn Pos
    btn_update.place(x=100, y=30)
    btn_remove.place(x=200, y=30)

    # Update Frame Widgets
    # Label Update Frame
    lbl_update_id = tk.Label(
        self.update_frame,
        text="ID:",
        font=("katibeh", 18),
        bg="#102C57",
        fg="#fff"
        )
    
    lbl_update_name = tk.Label(
        self.update_frame,
        text="Name:",
        font=("katibeh", 18),
        bg="#102C57",
        fg="#fff"
        )
    
    lbl_update_category = tk.Label(
        self.update_frame,
        text="Category:",
        font=("katibeh", 18),
        bg="#102C57",
        fg="#fff"
        )
    
    lbl_update_amount = tk.Label(
        self.update_frame,
        text="Amount:",
        font=("katibeh", 18),
        bg="#102C57",
        fg="#fff"
        )

    # Label Update Frame pos
    lbl_update_id.place(x=50, y=20)
    lbl_update_name.place(x=50, y=50)
    lbl_update_category.place(x=50, y=80)
    lbl_update_amount.place(x=50, y=110)

    # Ent Update Frame
    self.ent_update_id = tk.Entry(
        self.update_frame,
        font=("katibeh", 14),
        width=23
        )
    
    self.ent_update_name = tk.Entry(
        self.update_frame,
        font=("katibeh", 14)
        )
    
    self.ent_update_id.config(validate="key", validatecommand=(self.ent_update_id.register(lambda char: char.isdigit() or char == ""), "%S")) 
    self.ent_update_name.config(validate="key", validatecommand=(self.ent_update_id.register(lambda char: char.isalpha() or char == ""), "%S"))

    # ComboBox Entry Update Frame
    self.ent_update_category = ttk.Combobox(
        self.update_frame,
        values=["Income", "Expense"],
        font=("katibeh", 14),
        width=15,
        state="readonly"
        )
    
    self.ent_update_category.set("Expense")
    self.ent_update_category.config(validate="key", validatecommand=(self.ent_update_category.register(lambda char: char.isdigit() and char.isalpha() or char == ""), "%S"))

    self.ent_update_amount = tk.Entry(
        self.update_frame,
        font=("katibeh", 14),
        width=18
        )
    
    self.ent_update_amount.config(validate="key", validatecommand=(self.ent_update_amount.register(lambda char: char.isdigit() or char == ""), "%S"))

    # Ent Update Frame pos
    self.ent_update_id.place(x=100, y=22)
    self.ent_update_name.place(x=130, y=53)
    self.ent_update_category.place(x=170, y=83)
    self.ent_update_amount.place(x=150, y=114)

    # Btn Update Frame
    btn_update_frame = tk.Button(
        self.update_frame,
        text="Update",
        font=("katibeh", 16),
        width=10,
        cursor="hand2", 
        command=self.update_data_to_db
        )
    
    btn_update_cancel_frame = tk.Button(
        self.update_frame,
        text="Cancel",
        font=("katibeh", 16),
        width=8,
        cursor="hand2",
        command=self.edit_entries_win.destroy
        )

    # Btn Update Frame pos
    btn_update_frame.place(x=120, y=170)
    btn_update_cancel_frame.place(x=130, y=220)

    # Remove Frame Widgets
    # Lbl Remove Frame
    lbl_remove_id = tk.Label(
        self.remove_frame,
        text="ID:",
        font=("katibeh", 18),
        bg="#102C57",
        fg="#fff"
        )

    # Lbl Remove Frame pos
    lbl_remove_id.place(x=50, y=80)

    # Ent Remove Frame
    self.ent_remove_id = tk.Entry(
        self.remove_frame,
        font=("katibeh", 14),
        width=18
        )
    
    self.ent_remove_id.config(validate="key", validatecommand=(self.ent_remove_id.register(lambda char: char.isdigit() or char == ""), "%S"))

    # Ent Remove Frame pos
    self.ent_remove_id.place(x=120, y=83)

    # Btn Remove Frame
    btn_remove_frame = tk.Button(
        self.remove_frame,
        text="Remove",
        font=("katibeh", 16),
        width=10,
        cursor="hand2",
        command=self.remove_data_from_db
        )
    
    btn_remove_cancel_frame = tk.Button(
        self.remove_frame,
        text="Cancel",
        font=("katibeh", 16),
        width=8,
        cursor="hand2",
        command=self.edit_entries_win.destroy
        )

    # Btn Remove Frame pos
    btn_remove_frame.place(x=120, y=170)
    btn_remove_cancel_frame.place(x=130, y=220)

# Update Data to Database
def update_data_to_db(self):
    current_date = self.current_date.get()
    id = self.ent_update_id.get()
    name = self.ent_update_name.get()
    category = self.ent_update_category.get()
    amount = self.ent_update_amount.get()
    
    if id and name and category and amount:
        try:
            amount = float(amount)
            id_not_exist = db.update_data_in_table(id, name, category, amount, current_date)
            
            if id_not_exist:
                messagebox.showerror("Error", "Oopss, ID Does not Exist in Current Date")
            else:
                self.edit_entries_win.destroy()
                self.load_entries()
                self.update_total_balance()
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid values")
    else:
        messagebox.showerror("Error", "Please fill in all fields") 
            
def remove_data_from_db(self):
        current_date = self.current_date.get()
        id = self.ent_remove_id.get()
        
        id_not_exist = db.delete_data_in_table(id, current_date)
        
        if id:
            if id_not_exist:
                messagebox.showerror("Error", "Oops, ID Does Not Exist In Current Date")
            else:
                self.edit_entries_win.destroy()
                self.load_entries()
                self.update_total_balance()
        else:
            messagebox.showerror("Error", "Please fill in all fields") 


def create_chart_and_add_entries(self, event=None):
    total_income, total_expenses = db.get_income_expense_total(self.chart_month.get(), self.chart_year.get())
    
    if self.chart_open:
        self.ax.clear()
    else:
        # Create a new figure and axis if the chart is not open
        self.fig, self.ax = plt.subplots(figsize=(3, 3))  # Adjust the figsize to make the chart smaller
        self.chart_open = True

    # Get Data and Set to No data if None
    if total_income != 0 or total_expenses != 0:
        expenses_percentage = (total_expenses / (total_expenses + total_income)) * 100
        income_percentage = (total_income / (total_expenses + total_income)) * 100

        # Create pie chart
        labels = ['Expenses', 'Income']
        sizes = [expenses_percentage, income_percentage]
        colors = ['#ff9999', '#66b3ff']

        self.ax.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140, textprops={'fontsize': 9})
        self.ax.axis('equal')
        self.ax.set_title(f'Percentage of Expenses and Income in\n {self.chart_month.get()} {self.chart_year.get()}', fontsize=9)
        self.fig.subplots_adjust(left=0.2, right=0.8, top=0.8, bottom=0.2)

    # Create a canvas to display the Matplotlib chart
    canvas = FigureCanvasTkAgg(self.fig, master=self.chart_frame)
    canvas.get_tk_widget().place(x=10, y=60) # Position the chart 
    canvas.draw()
    
    # Insert Entries in the Expense/Income TreeView
    income_list = db.get_income_list(self.chart_month.get(), self.chart_year.get())
    expense_list = db.get_expense_list(self.chart_month.get(), self.chart_year.get())
    
    for record in self.tv_chart_income.get_children():
        self.tv_chart_income.delete(record)
        
    for record in self.tv_chart_expense.get_children():
        self.tv_chart_expense.delete(record)
        
    month_total_income = 0.00 
    if income_list:
        for income in income_list:
            name = income[3]
            amount = income[4]
            month_total_income += income[4]
            
            formatted_amount = "+₱{:.2f}".format(abs(amount))
            
            formatted_entry = (name, formatted_amount)
            self.tv_chart_income.insert('', 'end', values=formatted_entry, tags=(name))
            self.tv_chart_income.tag_configure(name, foreground="#006400")
            
    month_total_expense = 0.00 
    if expense_list:
        for expenses in expense_list:
            name = expenses[3]
            amount = expenses[4]
            month_total_expense += expenses[4]
            
            formatted_amount = "-₱{:.2f}".format(abs(amount))
            
            formatted_entry = (name, formatted_amount)
            self.tv_chart_expense.insert('', 'end', values=formatted_entry, tags=(name))
            self.tv_chart_expense.tag_configure(name, foreground="#FF0000")
    
    if month_total_expense:
        self.lbl_month_total_expense_amount.config(text=f"-₱{month_total_expense}")
    else:
        month_total_expense = 0.00 
        self.lbl_month_total_expense_amount.config(text="-₱0.00")
        
    
    if month_total_income:
        self.lbl_month_total_income_amount.config(text=f"+₱{month_total_income}")
    else:
        month_total_income = 0.00
        self.lbl_month_total_income_amount.config(text="+₱0.00")     
    
 
                
def close_chart(self):
    if self.chart_open:
        plt.close(self.fig)
        self.chart_open = False   


def filter_treeview(self):
    current_date = self.current_date.get()
    
    self.option_num += 1
    
    if current_date:
        if self.option_num == 1 or self.option_num == 2:
            entries = db.filter_category(current_date, self.option_num)
            
            if entries:
                for record in self.tv_tree_view.get_children():
                    self.tv_tree_view.delete(record)
                for entry in entries:
                    # Extract entry details
                    category = entry[2]
                    amount = entry[4]

                    # Format amount based on category
                    if category == "Expense":
                        formatted_amount = "-₱{:.2f}".format(abs(amount))  # Display negative amount
                        text_color = "#FF0000"  # Red for expenses
                    elif category == "Income":
                        formatted_amount = "+₱{:.2f}".format(abs(amount))  # Display positive amount
                        text_color = "#006400"  # Green for income
                    else:
                        formatted_amount = "₱{:.2f}".format(amount)  # Default format
                        text_color = "#000000"  # Default color

                    # Insert the entry into the Treeview with appropriate color and tag
                    formatted_entry = (entry[1], entry[3], formatted_amount)  # Update amount in entry
                    self.tv_tree_view.insert('', 'end', values=formatted_entry, tags=(category,))
                    # Apply the color to the entire row
                    self.tv_tree_view.tag_configure(category, foreground=text_color)       
        else:
            self.option_num = 0
            self.load_entries()
            