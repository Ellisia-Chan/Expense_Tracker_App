# Customized GUI made from figma, credits to the Tkinter Designer by Parth Jadhav to generate the file
# https://github.com/ParthJadhav/Tkinter-Designer


import tkinter as tk
# import db
from pathlib import Path
from tkinter import Canvas, Button, PhotoImage, ttk, messagebox
from datetime import datetime, timedelta



# Seperate file for the app functions
from build.function_list import add_button
from currency_conv import CurrencyConverter
from calc import Calculator


# Loading screen class
class LoadingScreen(tk.Tk):
    def __init__(self):
        super().__init__()
        self.overrideredirect(True)

        # Center LoadingScreen Window
        self.update_idletasks()
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        window_width = self.winfo_reqwidth()
        window_height = self.winfo_reqheight()
        x = (screen_width - window_width) // 2
        y = (screen_height - window_height) // 2
        self.geometry("+{}+{}".format(x, y))

        # Call methods
        self.loading_screen()
        self.loading(0)



    # Loading screen of the app 
    def loading_screen(self):
        # Frame
        self.frame = tk.Frame(self, width=500, height=200, bd=10, relief=tk.GROOVE, bg="#102C57")
        
        # Lbl
        lbl_title = tk.Label(self.frame, text="Pera Ko", font=("kuashan script", 40, "bold"), bg="#102C57", fg="#fff")
        self.lbl_loading = tk.Label(self.frame, text="0 %", font=("kuashan script", 18, "bold"), bg="#102C57", fg="#fff")
        
        # Widget Pos
        # Frame
        self.frame.pack()
        
        # Lbl        
        lbl_title.place(x=150, y=50)
        self.lbl_loading.place(x=230, y=120)
        
    # Loading Progress Counter
    def loading(self, progress):
        if progress <= 100:
            self.lbl_loading.config(text=f"{progress} %")
            progress += 1
            self.after(10, self.loading, progress)
        else:
            self.destroy()
            window = MyApp()
            window.mainloop()






# Class for the main application
class MyApp(tk.Tk):
    def __init__(self):
        super().__init__()
                
                
        # Path directory to access assets
        self.OUTPUT_PATH = Path(__file__).parent
        self.ASSETS_PATH = self.OUTPUT_PATH / "assets"  # Adjust this path according to your project structure
        
        
        # Initiate tkinter base frame of the app
        self.geometry("700x600")
        self.configure(bg="#FFFFFF")
        

        self.canvas()
        self.load_entries()
        self.update_total_balance()
        
        
    # Canvas to create the base frame of the app        
    def canvas(self):
        self.canvas = Canvas(self, bg="#FFFFFF", height=600, width=700, bd=0, highlightthickness=0, relief="ridge")
        self.canvas.place(x=0, y=0)

        # Background color
        self.bg_color_img = PhotoImage(file=self.relative_to_assets("bg_color.png"))
        self.bg_color = self.canvas.create_image(350.0, 310.0, image=self.bg_color_img)

        # Flower background
        self.bg_flower_img = PhotoImage(file=self.relative_to_assets("bg_flower.png"))
        self.bg_flower = self.canvas.create_image(255.99999999999994, 285.99999874472445, image=self.bg_flower_img)

        # Bottom background w/ shadow
        self.bg_bottom_frame_img = PhotoImage(file=self.relative_to_assets("bg_bottom_frame.png"))
        self.bg_bottom_frame = self.canvas.create_image(350.0, 559.5, image=self.bg_bottom_frame_img)

        # Top background w/ shadow
        self.bg_top_frame_img = PhotoImage(file=self.relative_to_assets("bg_top_frame.png"))
        self.bg_top_frame = self.canvas.create_image(350.0, 39.0, image=self.bg_top_frame_img)

        # -------------------------------------Top widgets-------------------------------------#

        # Date Label
        self.lbl_date_img = PhotoImage(file=self.relative_to_assets("lbl_date.png"))
        self.lbl_date = self.canvas.create_image(126.0, 41.0, image=self.lbl_date_img)

        # Date button left (<)
        self.btn_date_left_img = PhotoImage(file=self.relative_to_assets("btn_date_left.png"))
        self.btn_date_left = Button(image=self.btn_date_left_img, borderwidth=0, highlightthickness=0,
                                    command=lambda: print("btn_date_left clicked"), relief="flat")
        self.btn_date_left.place(x=15.0, y=26.0, width=26.0, height=26.0)

        # Date button right (>)
        self.btn_date_right_img = PhotoImage(file=self.relative_to_assets("btn_date_right.png"))
        self.btn_date_right = Button(image=self.btn_date_right_img, borderwidth=0, highlightthickness=0,
                                     command=lambda: print("btn_date_right clicked"), relief="flat")
        self.btn_date_right.place(x=211.0, y=26.0, width=26.0, height=26.0)

        # Expense Label
        self.lbl_expense_amount_img = PhotoImage(file=self.relative_to_assets("lbl_expense_amount.png"))
        self.lbl_expense_amount = self.canvas.create_image(324.0, 26.0, image=self.lbl_expense_amount_img)
        self.canvas.create_text(287.0, 49.0, anchor="nw", text="₱6,000.00", fill="#CA0000", font=("AbrilFatface Regular", 15 * -1))

        # Income Label
        self.lbl_income_amount_img = PhotoImage(file=self.relative_to_assets("lbl_income_amount.png"))
        self.lbl_income_amount = self.canvas.create_image(467.0, 26.0, image=self.lbl_income_amount_img)
        self.canvas.create_text(430.0, 49.0, anchor="nw", text="₱6,000.00", fill="#005D0B", font=("AbrilFatface Regular", 15 * -1))

        # Balance Label
        self.lbl_balance_amount_img = PhotoImage(file=self.relative_to_assets("lbl_balance_amount.png"))
        self.lbl_balance_amount = self.canvas.create_image(611.0, 26.0, image=self.lbl_balance_amount_img)
        self.canvas.create_text(573.0, 49.0, anchor="nw", text="₱6,000.00", fill="#CA0000", font=("AbrilFatface Regular", 15 * -1))

        # -------------------------------------Bottom widgets-------------------------------------#

        # Menu button
        self.btn_menu_img = PhotoImage(file=self.relative_to_assets("btn_menu.png"))
        self.btn_menu = Button(image=self.btn_menu_img, borderwidth=0, highlightthickness=0,
                               command=lambda: print("btn_menu clicked"), relief="flat")
        self.btn_menu.place(x=7.0, y=525.0, width=70.0, height=70.0)

        # Analysis button
        self.btn_analysis_img = PhotoImage(file=self.relative_to_assets("btn_analysis.png"))
        self.btn_analysis = Button(image=self.btn_analysis_img, borderwidth=0, highlightthickness=0,
                                   command=lambda: print("btn_analysis clicked"), relief="flat")
        self.btn_analysis.place(x=175.0, y=525.0, width=70.0, height=70.0)

        # Accounts button
        self.btn_accounts_img = PhotoImage(file=self.relative_to_assets("btn_accounts.png"))
        self.btn_accounts = Button(image=self.btn_accounts_img, borderwidth=0, highlightthickness=0,
                                   command=lambda: print("btn_accounts clicked"), relief="flat")
        self.btn_accounts.place(x=315.0, y=525.0, width=70.0, height=70.0)

        # Records button
        self.btn_records_img = PhotoImage(file=self.relative_to_assets("btn_records.png"))
        self.btn_records = Button(image=self.btn_records_img, borderwidth=0, highlightthickness=0,
                                  command=lambda: print("btn_records clicked"), relief="flat")
        self.btn_records.place(x=455.0, y=525.0, width=70.0, height=70.0)

        # Search button
        self.btn_search_img = PhotoImage(file=self.relative_to_assets("btn_search.png"))
        self.btn_search = Button(image=self.btn_search_img, borderwidth=0, highlightthickness=0,
                                 command=lambda: print("btn_search clicked"), relief="flat")
        self.btn_search.place(x=617.0, y=525.0, width=70.0, height=70.0)

        # Add button
        self.btn_add_item_img = PhotoImage(file=self.relative_to_assets("btn_add_item.png"))
        self.btn_add_item = Button(image=self.btn_add_item_img, borderwidth=0, highlightthickness=0,
                                   command=self.add_button, relief="flat")
        self.btn_add_item.place(x=569.0, y=379.0, width=129.0, height=129.0)
    
    




        # Mid Frame widgets
        
        # TreeView
        self.tv_tree_view = ttk.Treeview( self.mid_frame, columns=(1, 2, 3), show="headings", height=12, tyle="Custom.Treeview")
        
        self.tv_tree_view.column(1, anchor="center", stretch="No", width=200)
        self.tv_tree_view.column(2, anchor="center", stretch="No", width=340)
        self.tv_tree_view.column(3, anchor="center", stretch="No", width=340)
        self.tv_tree_view.heading(1, text="ID")
        self.tv_tree_view.heading(2, text="Name")
        self.tv_tree_view.heading(3, text="Amount")

        # TreeView pos
        self.tv_tree_view.pack(side="left")

        # Config TreeView Style
        style = ttk.Style()
        style.theme_use("clam")
        style.configure("Custom.Treeview.Heading", font=("katibeh", 18))
        style.configure("Custom.Treeview", font=("katibeh", 16), background="#EADBC8", fieldbackground="#EADBC8")
        style.configure("Custom.Treeview", rowheight=30)

        # Disable TreeView Heading Resizing
        self.tv_tree_view.bind('<Button-1>', 'break')

        # TreeView Vertical ScrollBar
        scrollbar = ttk.Scrollbar(
            self.mid_frame,
            orient="vertical",
            command=self.tv_tree_view.yview
            )
        
        scrollbar.pack(side="right", fill="y")










    # Get access to the asset files from directory path
    def relative_to_assets(self, path: str) -> Path:
        return self.ASSETS_PATH / Path(path)

    # Wrapper functions to call imported functions from function_list.py
    def add_button(self):
        add_button(self)


if __name__ == "__main__":
    app = LoadingScreen()
    app.mainloop()
