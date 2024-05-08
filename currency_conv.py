import tkinter as tk
from tkinter import ttk

class CurrencyConverter:
    def __init__(self, root):
        self.app = root
        self.win = tk.Toplevel(self.app)
        self.win.grab_set()
        self.win.geometry("500x500")
        self.win.title('Currency Converter')
        self.win.resizable(False, False)
        self.win.protocol("WM_DELETE_WINDOW", self.back_to_main)
               
        # Conversion Rates
        self.exchange_rate = {
            'US dollar (USD)': 1.0,
            'Euro (EUR)': 0.93,
            'Japanese yen (JPY)': 153.06,
            'Pound sterling (GBP)': 0.79,
            'Australian dollar (AUD)': 1.51,
            'Canadian dollar (CAD)': 1.37,
            'Philippine peso (PHP)': 57.06,
            'Chinese Yuan (CNY)': 7.24,
            'Hong Kong dollar (HKD)': 7.81,
            'New Zealand dollar (NZD)': 1.66  
        }
        
        
        
        self.create_widgets()
        self.bind_number_buttons()
               
    def create_widgets(self):
        # Frame
        parent_frame = tk.Frame(self.win, width=500, height=500, bg="#102C57", bd=20, relief=tk.RIDGE)
        child_frame = tk.Frame(self.win, width=460, height=460, bg="#0065FF")
        
        # lbl
        lbl_exchange_rate_date = tk.Label(
            child_frame,
            text="Exchange Rate Date: May 10, 2024",
            font=("katibeh", 12),
            bg="#FFF"
        )
        
        # ComboBox
        self.from_currency = ttk.Combobox(
            child_frame,
            values=list(self.exchange_rate.keys()),
            font=("katibeh", 18),
            width=26,
            state="readonly"
        )
        self.from_currency.set(list(self.exchange_rate.keys())[0])
        self.from_currency.bind("<<ComboboxSelected>>", self.calculate_rate_from)
        
   
        self.to_currency = ttk.Combobox(
            child_frame,
            values=list(self.exchange_rate.keys()),
            font=("katibeh", 18),
            width=26,
            state="readonly"
        )
        self.to_currency.set(list(self.exchange_rate.keys())[6])
        self.to_currency.bind("<<ComboboxSelected>>", self.calculate_rate_from)

        # Ent
        self.ent_from_currency = tk.Entry(
            child_frame,
            font=("katibeh", 18),
            width=26
        )
        self.ent_from_currency.config(validate="key", validatecommand=(self.ent_from_currency.register(lambda char: char.isdigit() or char == "" or char in "."), "%S"))
        self.ent_from_currency.bind("<KeyRelease>", self.calculate_rate_from)
        self.ent_to_currency = tk.Entry(
            child_frame,
            font=("katibeh", 18),
            width=26,
        )
        self.ent_to_currency.config(validate="key", validatecommand=(self.ent_to_currency.register(lambda char: char.isdigit() or char == "" or char in "."), "%S"))
        self.ent_to_currency.bind("<KeyRelease>", self.calculate_rate_to)
        # Btn
        # Back Btn
        btn_back = tk.Button(
            child_frame,
            text="<",
            font=("katibeh", 14, "bold"),
            bg="#102C57",
            fg="#fff",
            cursor="hand2",
            width=5,
            command=self.back_to_main
        )
        
        # Btn row 1
        self.btn_7 = tk.Button(
            child_frame,
            text=7,
            font=("katibeh", 16),
            width=5,
        )
        
        self.btn_8 = tk.Button(
            child_frame,
            text=8,
            font=("katibeh", 16),
            width=5,
        )
        
        self.btn_9 = tk.Button(
            child_frame,
            text=9,
            font=("katibeh", 16),
            width=5,
        )
        
        self.btn_c = tk.Button(
            child_frame,
            text="C",
            font=("katibeh", 16),
            width=5,
        )
        
        # Btn row 2
        self.btn_4 = tk.Button(
            child_frame,
            text=4,
            font=("katibeh", 16),
            width=5,
        )
        
        self.btn_5 = tk.Button(
            child_frame,
            text=5,
            font=("katibeh", 16),
            width=5,
        )
        
        self.btn_6 = tk.Button(
            child_frame,
            text=6,
            font=("katibeh", 16),
            width=5,
        )
        
        self.btn_del = tk.Button(
            child_frame,
            text="Del",
            font=("katibeh", 16),
            width=5,
        )
        
        # Btn row 3
        self.btn_1 = tk.Button(
            child_frame,
            text=1,
            font=("katibeh", 16),
            width=5,
        )
        
        self.btn_2 = tk.Button(
            child_frame,
            text=2,
            font=("katibeh", 16),
            width=5,
        )
        
        self.btn_3 = tk.Button(
            child_frame,
            text=3,
            font=("katibeh", 16),
            width=5,
        )
        
        # Btn Row 4
        self.btn_00 = tk.Button(
            child_frame,
            text="00",
            font=("katibeh", 16),
            width=5,
        )
        
        self.btn_0 = tk.Button(
            child_frame,
            text=0,
            font=("katibeh", 16),
            width=5,
        )
        
        self.btn_decimal = tk.Button(
            child_frame,
            text=".",
            font=("katibeh", 16),
            width=5,
        )
    
        # Widgets Pos
        # Frame pos
        parent_frame.place(x=0, y=0)
        child_frame.place(x=20, y=20)
        
        # lbl pos
        lbl_exchange_rate_date.place(x=10, y=50)
        
        # ComboBox pos
        self.from_currency.place(x=10, y=80)
        self.to_currency.place(x=10, y=160)
        
        # Ent pos
        self.ent_from_currency.place(x=10, y=120)
        self.ent_to_currency.place(x=10, y=200)
        
        # Btn pos
        btn_back.place(x=10, y=5)
        
        self.btn_7.place(x=70, y=250)
        self.btn_8.place(x=150, y=250)
        self.btn_9.place(x=230, y=250)
        self.btn_c.place(x=310, y=250)
        
        self.btn_4.place(x=70, y=300)
        self.btn_5.place(x=150, y=300)
        self.btn_6.place(x=230, y=300)
        self.btn_del.place(x=310, y=300)
        
        self.btn_1.place(x=70, y=350)
        self.btn_2.place(x=150, y=350)
        self.btn_3.place(x=230, y=350)
        
        self.btn_00.place(x=70, y=400)
        self.btn_0.place(x=150, y=400)
        self.btn_decimal.place(x=230, y=400)
    
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
            self.btn_00,
            self.btn_decimal]:
            num_button.bind('<Button-1>', self.insert_number)
            
        self.btn_c.bind('<Button-1>', self.clear)
        self.btn_del.bind('<Button-1>', self.delete)       
        
    def insert_number(self, event):
        # Get the currently focused entry
        focused_widget = self.app.focus_get()

        # If it's an entry field, insert the corresponding number
        if isinstance(focused_widget, tk.Entry):
            cursor_pos = focused_widget.index(tk.INSERT)  # Get the cursor position
            focused_widget.insert(cursor_pos, event.widget["text"])  # Insert the number at the cursor position

            # Call the appropriate calculation method based on the focused entry field
            if focused_widget == self.ent_from_currency:
                self.calculate_rate_from()
            elif focused_widget == self.ent_to_currency:
                self.calculate_rate_to()
       
    def calculate_rate_from(self, event=None):
        from_currency = self.from_currency.get()
        to_currency = self.to_currency.get()
        from_currency_amount = self.ent_from_currency.get()
        
        if from_currency and to_currency and from_currency_amount.replace('.', '').isdigit():
            from_currency_amount = float(from_currency_amount)
            exchange_rate_from = self.exchange_rate[from_currency]
            exchange_rate_to = self.exchange_rate[to_currency]

            result = (from_currency_amount / exchange_rate_from) * exchange_rate_to
            
            self.ent_to_currency.config(validate="none")
            self.ent_to_currency.delete(0, tk.END)
            self.ent_to_currency.insert(tk.END, "{:.2f}".format(result))
            self.ent_to_currency.config(validate="key")
        else:
            self.ent_to_currency.config(validate="none")
            self.ent_to_currency.delete(0, tk.END)
            self.ent_to_currency.config(validate="key")
            
            
    def calculate_rate_to(self, event=None):
        from_currency = self.from_currency.get()
        to_currency = self.to_currency.get()
        to_currency_amount = self.ent_to_currency.get()
        
        if from_currency and to_currency and to_currency_amount.replace('.', '').isdigit():
            to_currency_amount = float(to_currency_amount)
            exchange_rate_from = self.exchange_rate[from_currency]
            exchange_rate_to = self.exchange_rate[to_currency]

            result = (to_currency_amount / exchange_rate_to) * exchange_rate_from
            
            self.ent_from_currency.config(validate="none")
            self.ent_from_currency.delete(0, tk.END)
            self.ent_from_currency.insert(tk.END, "{:.2f}".format(result))
            self.ent_from_currency.config(validate="key")
        else:
            self.ent_from_currency.config(validate="none")
            self.ent_from_currency.delete(0, tk.END)
            self.ent_from_currency.config(validate="key")
                          
    def clear(self, event=None):
        focused_widget = self.app.focus_get()

        # Check if the focused widget is the 'from' entry field
        if isinstance(focused_widget, tk.Entry) and focused_widget == self.ent_from_currency:
            self.ent_from_currency.config(validate="none")
            focused_widget.delete(0, tk.END)
            self.ent_from_currency.config(validate="key")
            self.calculate_rate_from()
            
        if isinstance(focused_widget, tk.Entry) and focused_widget == self.ent_to_currency:
            self.ent_to_currency.config(validate="none")
            focused_widget.delete(0, tk.END)
            self.ent_to_currency.config(validate="key")
            self.calculate_rate_to()
            
    def delete(self, event=None): 
        focused_widget = self.app.focus_get()
        
        if isinstance(focused_widget, tk.Entry) and focused_widget == self.ent_from_currency:
            cursor_pos = focused_widget.index(tk.INSERT)  # Get the cursor position
            if cursor_pos > 0:
                focused_widget.delete(cursor_pos - 1)  # Delete one character before the cursor position
                self.calculate_rate_from()
        
        if isinstance(focused_widget, tk.Entry) and focused_widget == self.ent_to_currency:
            cursor_pos = focused_widget.index(tk.INSERT)  # Get the cursor position
            if cursor_pos > 0:
                focused_widget.delete(cursor_pos - 1)  # Delete one character before the cursor position
                self.calculate_rate_to()
                                     
    def back_to_main(self):
        self.win.destroy()   