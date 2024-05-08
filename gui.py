# GROUP 4
# 2nd Sem, Final project


# Customized GUI made using figma, credits to the Tkinter Designer by Parth Jadhav to generate the file
# https://github.com/ParthJadhav/Tkinter-Designer

import db
import tkinter as tk
import datetime
from pathlib import Path

from datetime import datetime
from PIL import Image, ImageTk
from idlelib.tooltip import Hovertip
from tkinter import Button, PhotoImage, ttk, messagebox


import function_list as function
import chart as chart
from currency_conv import CurrencyConverter
from calc import Calculator
from image_data import image_data


# Class of the loading screen
class LoadingScreen(tk.Tk):
    def __init__(self):
        super().__init__()
        

        # Path directory to access assets
        self.OUTPUT_PATH = Path(__file__).parent
        self.ASSETS_PATH = self.OUTPUT_PATH / "assets" / "loading"


        # Store PhotoImage objects
        self.photo_images = []

        # Call methods
        self.loading_screen()
        self.loading(0)

    # Get access to the asset files from directory path
    def relative_to_assets(self, path: str) -> Path:
        return self.ASSETS_PATH / Path(path)

    # Loading screen of the app
    def loading_screen(self):
        self.geometry("700x600")
        self.configure(bg="#FFFFFF")
        self.resizable(False, False)

        self.loading_canvas = tk.Canvas(
            self,
            bg="#FFFFFF",
            height=600,
            width=700,
            bd=0,
            highlightthickness=0,
            relief="ridge"
        )
        self.loading_canvas.place(x=0, y=0)


        for image_name, coordinates in image_data:
            image_path = self.relative_to_assets(image_name)
            image_obj = tk.PhotoImage(file=image_path)
            self.photo_images.append(image_obj)  # Store PhotoImage objects
            self.loading_canvas.create_image(coordinates, image=image_obj)

        self.lbl_loading = tk.Label(self.loading_canvas, text="0 %", font=(
            "kuashan script", 30, "bold"), fg="#0065FF")
        self.lbl_loading.place(x=330, y=400)

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


# Class of the main program
class MyApp(tk.Tk):
    def __init__(self):
        super().__init__()

        # Path directory to access assets
        self.OUTPUT_PATH = Path(__file__).parent
        self.ASSETS_PATH = self.OUTPUT_PATH / "assets"  # Adjust this path according to your project structure

        # Initiate tkinter base frame of the app
        self.geometry("700x600")
        self.configure(bg="#FFFFFF")
        self.title("Pera ko, a money tracker app made by Group 4")
        self.resizable(False, False)
        self.protocol("WM_DELETE_WINDOW", self.exit_confirmation)
        
        self.chart_open = False
        self.option_num = 0

        self.canvas()
        self.load_entries()
        self.update_total_balance()
        
        # Disable Record Button Due to Record is Default Window
        self.btn_records.config(state="disabled")
        
        # Global variable to store the sidebar frame
        self.menu_frame = None
        
        # Check if Database exist, if not, create database file where the py file is located.
        db.create_database()



    # Canvas to create the base frame of the app        
    def canvas(self):
        self.canvas = tk.Canvas(self, bg="#FFFFFF", height=600, width=700, bd=0, highlightthickness=0, relief="ridge")
        self.canvas.place(x=0, y=0)

        # Background color
        self.bg_color_img = PhotoImage(file=self.relative_to_assets("bg_color.png"))
        self.bg_color = self.canvas.create_image(350.0, 310.0, image=self.bg_color_img)

        # Flower background
        self.bg_flower1_img = PhotoImage(file=self.relative_to_assets("bg_flower1.png"))
        self.bg_flower1 = self.canvas.create_image(277, 291, image=self.bg_flower1_img)

        # Bottom background frame w/ shadow
        self.bg_bottom_frame_img = PhotoImage(file=self.relative_to_assets("bg_bottom_frame.png"))
        self.bg_bottom_frame = self.canvas.create_image(350.0, 559.5, image=self.bg_bottom_frame_img)

        # Mid frame for treeview
        self.mid_frame = tk.Frame(self, width=550, height=630)
        self.mid_frame.place(x=10, y=85)

        # Top background frame w/ shadow
        self.bg_top_frame_img = PhotoImage(file=self.relative_to_assets("bg_top_frame.png"))
        self.bg_top_frame = self.canvas.create_image(350.0, 39.0, image=self.bg_top_frame_img)

        # Flower background (design on top of top & bottom background frame)
        self.bg_flower2_img = PhotoImage(file=self.relative_to_assets("bg_flower2.png"))
        self.bg_flower2 = self.canvas.create_image(533, 36, image=self.bg_flower2_img)

        self.bg_flower3_img = PhotoImage(file=self.relative_to_assets("bg_flower3.png"))
        self.bg_flower3 = self.canvas.create_image(120, 577, image=self.bg_flower3_img)

        self.bg_flower4_img = PhotoImage(file=self.relative_to_assets("bg_flower4.png"))
        self.bg_flower4 = self.canvas.create_image(573, 551, image=self.bg_flower4_img)

        self.bg_flower5_img = PhotoImage(file=self.relative_to_assets("bg_flower5.png"))
        self.bg_flower5 = self.canvas.create_image(357, 51, image=self.bg_flower5_img)

        self.bg_flower6_img = PhotoImage(file=self.relative_to_assets("bg_flower6.png"))
        self.bg_flower6 = self.canvas.create_image(677, 48, image=self.bg_flower6_img)


        # -------------------------------------Top widgets-------------------------------------#


        # Date Label
        self.current_date = tk.StringVar()
        self.current_date.set(datetime.now().strftime("%B %d, %Y"))

        self.lbl_date = tk.Label(self.canvas, textvariable=self.current_date, font=("katibeh", 17, "bold"), fg="#1E1F1E")
        self.lbl_date.place(x=53, y=19)
        
        
        # Date button previous (<)
        self.btn_date_previous_img = PhotoImage(file=self.relative_to_assets("btn_date_left.png"))
        self.btn_date_previous = Button(image=self.btn_date_previous_img, borderwidth=0, highlightthickness=0,
                                    command=self.previous_date, relief="flat", cursor="hand2")
        self.btn_date_previous.place(x=14, y=26.0, width=26.0, height=26.0)

        # Date button next (>)
        self.btn_date_next_img = PhotoImage(file=self.relative_to_assets("btn_date_right.png"))
        self.btn_date_next = Button(image=self.btn_date_next_img, borderwidth=0, highlightthickness=0,
                                     command=self.next_date, relief="flat", cursor="hand2")
        self.btn_date_next.place(x=211.0, y=26.0, width=26.0, height=26.0)

        # Expense Label
        self.lbl_expenses_img = PhotoImage(file=self.relative_to_assets("lbl_expense_amount.png"))
        self.lbl_expenses = self.canvas.create_image(324.0, 26.0, image=self.lbl_expenses_img)
        self.lbl_expenses_amount = tk.Label(self.canvas, anchor="nw", text="₱0", fg="red", font=("katibeh", 12, "bold"))
        self.lbl_expenses_amount.place(x=275, y=40)


        # Income Label
        self.lbl_income_img = PhotoImage(file=self.relative_to_assets("lbl_income_amount.png"))
        self.lbl_income = self.canvas.create_image(467.0, 26.0, image=self.lbl_income_img)
        self.lbl_income_amount = tk.Label(self.canvas, anchor="nw", text="₱0", fg="green", font=("katibeh", 12, "bold"))
        self.lbl_income_amount.place(x=425, y=40)
        
        # Balance Label
        self.lbl_balance_img = PhotoImage(file=self.relative_to_assets("lbl_balance_amount.png"))
        self.lbl_balance = self.canvas.create_image(611.0, 26.0, image=self.lbl_balance_img)
        self.lbl_balance_amount = tk.Label(self.canvas, anchor="nw", text="₱0", font=("katibeh", 12, "bold"))
        self.lbl_balance_amount.place(x=562, y=40)
        
        # -------------------------------------Mid widgets-------------------------------------#

        # Display tree view frame
        self.tv_tree_view = ttk.Treeview(self.mid_frame, columns=(1, 2, 3), show="headings", height=12,
                                         style="Custom.Treeview")

        # TreeView columns and headings
        self.tv_tree_view.column(1, anchor="center", stretch="No", width=120)
        self.tv_tree_view.column(2, anchor="center", stretch="No", width=250)
        self.tv_tree_view.column(3, anchor="center", stretch="No", width=150)
        self.tv_tree_view.heading(1, text="ID")
        self.tv_tree_view.heading(2, text="Name")
        self.tv_tree_view.heading(3, text="Amount")

        # TreeView position
        self.tv_tree_view.pack(side="left")

        # Configure TreeView Style
        style = ttk.Style()
        style.theme_use("clam")
        style.configure("Custom.Treeview.Heading", font=("katibeh", 18))
        style.configure("Custom.Treeview", font=("katibeh", 16), background="#EADBC8", fieldbackground="#EADBC8")
        style.configure("Custom.Treeview", rowheight=30)

        # Disable TreeView Heading Resizing and selection
        self.tv_tree_view.bind('<B1-Motion>', lambda event: 'break')
        self.tv_tree_view.bind("<ButtonRelease-1>",
                               lambda event: self.tv_tree_view.selection_remove(self.tv_tree_view.selection()))

        # TreeView Vertical ScrollBar
        scrollbar = ttk.Scrollbar(self.mid_frame, orient="vertical", command=self.tv_tree_view.yview)
        scrollbar.pack(side="right", fill="y")


        # -------------------------------------Bottom widgets-------------------------------------#

        # Menu button
        self.btn_menu_img = PhotoImage(file=self.relative_to_assets("btn_menu.png"))
        self.btn_menu = Button(image=self.btn_menu_img, borderwidth=0, highlightthickness=0,
                               command=self.toggle_menu, relief="flat", cursor="hand2")
        self.btn_menu.place(x=7.0, y=525.0, width=70.0, height=70.0)

        # Analysis button
        self.btn_analysis_img = PhotoImage(file=self.relative_to_assets("btn_analysis.png"))
        self.btn_analysis = Button(image=self.btn_analysis_img, borderwidth=0, highlightthickness=0,
                                   command=self.show_chart, relief="flat", cursor="hand2")
        self.btn_analysis.place(x=175.0, y=525.0, width=70.0, height=70.0)

        # # Accounts button
        # self.btn_accounts_img = PhotoImage(file=self.relative_to_assets("btn_accounts.png"))
        # self.btn_accounts = Button(image=self.btn_accounts_img, borderwidth=0, highlightthickness=0,
        #                            command=lambda: print("btn_accounts clicked"), relief="flat")
        # self.btn_accounts.place(x=315.0, y=525.0, width=70.0, height=70.0)

        # Records button
        self.btn_records_img = PhotoImage(file=self.relative_to_assets("btn_records.png"))
        self.btn_records = Button(image=self.btn_records_img, borderwidth=0, highlightthickness=0,
                                  command=self.show_record, relief="flat", cursor="hand2")
        self.btn_records.place(x=455.0, y=525.0, width=70.0, height=70.0)

        # # Search button
        # self.btn_search_img = PhotoImage(file=self.relative_to_assets("btn_search.png"))
        # self.btn_search = Button(image=self.btn_search_img, borderwidth=0, highlightthickness=0,
        #                          command=lambda: print("btn_search clicked"), relief="flat")
        # self.btn_search.place(x=617.0, y=525.0, width=70.0, height=70.0)
        
        # Filter button
        self.btn_filter_img = PhotoImage(file=self.relative_to_assets("btn_filter.png"))
        self.btn_filter = Button(image=self.btn_filter_img, borderwidth=0, highlightthickness=0,
                                 command=self.filter_treeview, relief="flat", cursor="hand2")
        self.btn_filter.place(x=617.0, y=525.0, width=70.0, height=70.0)



        # -------------------------------------Right widgets-------------------------------------#


        # Currency exchange button
        self.btn_currency_img = PhotoImage(file=self.relative_to_assets("btn_currency.png"))
        self.btn_currency = Button(image=self.btn_currency_img, borderwidth=0, highlightthickness=0,
                                   command=self.open_currency_converter, relief="flat", cursor="hand2")
        self.btn_currency.place(x=584.0, y=95.0, width=102.0, height=103.)
        self.btn_currency_tip = Hovertip(self.btn_currency,'Change currency of your choice') # Tool tip :>


        # Calculator button
        self.btn_calculator_img = PhotoImage(file=self.relative_to_assets("btn_calculator.png"))
        self.btn_calculator = Button(image=self.btn_calculator_img, borderwidth=0, highlightthickness=0,
                                     command=self.open_calculator, relief="flat", cursor="hand2")
        self.btn_calculator.place(x=585.0, y=198.0, width=102.0, height=102.0)
        self.btn_calculator_tip = Hovertip(self.btn_calculator,'Calculator') # Tool tip :>


        # Update button
        self.btn_edit_img = PhotoImage(file=self.relative_to_assets("btn_edit.png"))
        self.btn_edit = Button(image=self.btn_edit_img, borderwidth=0, highlightthickness=0,
                               command=self.edit_entries_window, relief="flat", cursor="hand2")
        self.btn_edit.place(x=584.0, y=300.0, width=102.0, height=103.)
        self.btn_edit_tip = Hovertip(self.btn_edit,'Edit item on your treeview') # Tool tip :>


        # Add button
        self.btn_add_item_img = PhotoImage(file=self.relative_to_assets("btn_add_item.png"))
        self.btn_add_item = Button(image=self.btn_add_item_img, borderwidth=0, highlightthickness=0,
                                command=self.add_entry_win, relief="flat", cursor="hand2")
        self.btn_add_item.place(x=585.0, y=403.0, width=102.0, height=102.0)

        # Create and attach tooltip to the button
        self.btn_add_item_tip = Hovertip(self.btn_add_item, 'Add item on your treeview') # Tool tip :>




    #------------------Date previous and next button function------------------#
    
        # Disable Next button if Date is Current
        today = datetime.now().strftime("%B %d, %Y")
        if self.current_date.get() == today:
            self.btn_date_next.config(state="disabled")
        


    # Get access to the asset files from directory path
    def relative_to_assets(self, path: str) -> Path:
        return self.ASSETS_PATH / Path(path)



    # -------------------------------------Menu sidebar-------------------------------------#

    # Function to toggle menu visibility
    
    def create_menu(self):
        self.menu_frame = tk.Frame(self, bg="#EADBC8", width=200, bd=15, relief=tk.RIDGE)
        self.menu_frame.place(x=0, y=0, relheight=1)  # Adjust the position as needed

        # Create buttons inside the menu frame
        self.button_frame = tk.Frame(self.menu_frame, bg="#EADBC8", width=100, padx=20, pady=20)

        btn_project_team = tk.Button(self.button_frame, text="Project Team", font=("katibeh", 18, "bold"), cursor="hand2",
                                    width=10, bg="#0065FF", fg="#F0F0F0", borderwidth=0, anchor="w", relief="flat",
                                    padx=10,
                                    command=self.project_team)
        btn_project_team.pack(fill="x", pady=5)

        btn_clear_data = tk.Button(self.button_frame, text="Clear Data", font=("katibeh", 18, "bold"), cursor="hand2",
                                width=10, bg="#0065FF", fg="#F0F0F0", borderwidth=0, anchor="w", relief="flat", padx=10,
                                command=self.clear_data)
        btn_clear_data.pack(fill="x", pady=5)

        btn_about = tk.Button(self.button_frame, text="About", font=("katibeh", 18, "bold"), cursor="hand2",
                            width=10, bg="#0065FF", fg="#F0F0F0", borderwidth=0, anchor="w", relief="flat", padx=10,
                            command=self.show_about)
        btn_about.pack(fill="x", pady=5)

        btn_exit = tk.Button(self.button_frame, text="Exit", font=("katibeh", 18, "bold"), cursor="hand2",
                            width=10, bg="#0065FF", fg="#F0F0F0", borderwidth=0, anchor="w", relief="flat", padx=10,
                            command=self.exit_confirmation)
        btn_exit.pack(fill="x", pady=5)

        # Pack the button frame after creating all buttons
        self.button_frame.pack()

        # Menu Sidebar widgets
        btn_sidebar_menu_back = tk.Button(self.menu_frame, text="<", font=("impact", 25, "bold"), cursor="hand2",
                                        width=2, fg="#1E1F1E", bg="#EADBC8", borderwidth=0, anchor="w", relief="flat",
                                        command=lambda: self.menu_frame.place_forget())
        btn_sidebar_menu_back.place(x=20, y=500)

        # Bindings to close menu sidebar   
        self.bind("<Button-1>", self.close_menu)
    
    # Function to toggle menu visibility
    def toggle_menu(self):
        if self.menu_frame:
            self.menu_frame.place_forget()
            self.menu_frame = None
        else:
            self.create_menu()

    # Function to close menu sidebar when clicked outside
    def close_menu(self, event):
        if self.menu_frame:
            x, y = event.x_root, event.y_root
            menu_x, menu_y, menu_width, menu_height = self.menu_frame.winfo_rootx(), self.menu_frame.winfo_rooty(), self.menu_frame.winfo_width(), self.menu_frame.winfo_height()
            if not (menu_x <= x <= menu_x + menu_width and menu_y <= y <= menu_y + menu_height):
                self.menu_frame.place_forget()
                self.menu_frame = None


    # Show the image of the project team together with their role to the gruop
    def project_team(self):
        # Create a new window
        self.proj_team_win = tk.Toplevel(self)
        self.proj_team_win.title("Project Team: Thank you for using our app!")
        self.proj_team_win.resizable(False, False)
        self.proj_team_win.configure(bd=20, relief=tk.RIDGE)
        self.proj_team_win.grab_set()

        # Load and display the image on a canvas
        proj_team_img = Image.open(self.relative_to_assets("project_team.png"))  # Open image using PIL
        img_width, img_height = proj_team_img.size  # Get dimensions of the image

        # Resize canvas and window based on image dimensions
        canvas = tk.Canvas(self.proj_team_win, bg="#FFFFFF", width=img_width, height=img_height, bd=0, highlightthickness=0, relief="ridge")
        canvas.pack(fill=tk.BOTH, expand=True)  # Expand canvas to fill window
        bg_proj_team = ImageTk.PhotoImage(proj_team_img)  # Convert image to Tkinter PhotoImage
        canvas.create_image(0, 0, anchor=tk.NW, image=bg_proj_team)  # Display image on canvas

        # Retain reference to the image to prevent it from being garbage collected
        canvas.image = bg_proj_team

        # Add frame for additional information
        info_frame = tk.Frame(self.proj_team_win, bg="white", bd=0, relief="ridge")
        info_frame.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

        # Divide frame into 5 columns and 3 rows
        for i in range(3):
            info_frame.grid_rowconfigure(i, weight=1)
        for i in range(5):
            info_frame.grid_columnconfigure(i, weight=1)

        # Add "Group 4" label in the first row
        group_label = tk.Label(info_frame, text="Group 4", bg="white", font=("times new roman", 20, "bold"))
        group_label.grid(row=0, column=0, columnspan=5, sticky="nsew")

        # Names in the second row
        names = [
            "Sean Matthew Lee P. Narvaez",
            "Prince Harvey M. Casula",
            "Sherwin P. Limosnero",
            "Christian Jude N. Villaber",
            "Adrian V. Cagampang"
        ]
        for i, name in enumerate(names):
            name_label = tk.Label(info_frame, text=name, bg="white")
            name_label.grid(row=1, column=i, sticky="nsew")

        # Roles in the third row
        roles = [
            "Documentation Lead",
            "Technical Writer",
            "Designer (UI/UX) & Project Manager",
            "Chief Developer",
            "Asst. Tech. Writer"
        ]
        for i, role in enumerate(roles):
            role_label = tk.Label(info_frame, text=role, bg="white")
            role_label.grid(row=2, column=i, sticky="nsew")

    



    # Ask for confirmation when exit (x) clicked
    def exit_confirmation(self):
        if messagebox.askokcancel("Exit", "Do you really want to exit?"):
            self.close_chart()
            self.destroy()
            



    #About Menu
    def show_about(self):
        # Message to display
        about_message = """
        Pera Ko
        
  Expense tracker App
    v1.0 (ALPHA ver)

    Chief Developer:
Christian Jude N. Villaber

    Designer (UI/UX):
  Sherwin P. Limosnero
        """



        # Display the message box centered on the screen
        messagebox.showinfo("About", about_message)

    # For Changing Window Records/Analysis
    def show_record(self):
        self.mid_frame.place(x=10, y=85)
        self.btn_currency.place(x=584.0, y=95.0, width=102.0, height=103.)
        self.btn_calculator.place(x=585.0, y=198.0, width=102.0, height=102.0)
        self.btn_edit.place(x=584.0, y=300.0, width=102.0, height=103.)
        self.btn_add_item.place(x=585.0, y=403.0, width=102.0, height=102.0)
        self.btn_filter.place(x=617.0, y=525.0, width=70.0, height=70.0)
        
        self.chart_frame.place_forget()
        self.btn_analysis.config(state="normal")
        self.btn_records.config(state="disabled")
        
        # Configure TreeView Style
        style = ttk.Style()
        style.theme_use("clam")
        style.configure("Custom.Treeview.Heading", font=("katibeh", 18))
        style.configure("Custom.Treeview", font=("katibeh", 16), background="#EADBC8", fieldbackground="#EADBC8")
        style.configure("Custom.Treeview", rowheight=30)
        
        self.close_chart()
        
    def show_chart(self):
        self.mid_frame.place_forget()
        self.btn_analysis.config(state="disabled")
        self.btn_records.config(state="normal")
        
        for button, tooltip in [
        (self.btn_currency, self.btn_currency_tip),
        (self.btn_calculator, self.btn_calculator_tip),
        (self.btn_edit, self.btn_edit_tip),
        (self.btn_add_item, self.btn_add_item_tip),
        (self.btn_filter, None),
        ]:
            button.place_forget()

        # Chart Widgets
        self.chart_frame = tk.Frame(self, background="#FFFAF0", width=700, height=520)
        self.chart_frame.place(x=0, y=0)
        
        year = []
        months = [
            'January',
            'February',
            'March',
            'April',
            'May',
            'June',
            'July',
            'August',
            'September',
            'October',
            'November',
            'December'
        ]
        
        current_month_name = datetime.now().strftime('%B')
        current_year = datetime.now().year
        current_year_str = str(current_year)
        
        # Add year to the list for Combobox selection
        year.append(current_year_str) if current_year_str not in year else None
        
        self.chart_month = ttk.Combobox(
            self.chart_frame,
            values=months,
            font=("katibeh", 16),
            width=10,
            state="readonly"
        )
        self.chart_month.set(current_month_name)
        self.chart_month.bind("<<ComboboxSelected>>", lambda event: self.create_chart_and_add_entries())
        
        self.chart_year = ttk.Combobox(
            self.chart_frame,
            values=year,
            font=("katibeh", 16),
            width=8,
            state="readonly"
        )
        self.chart_year.set(current_year_str)
        self.chart_year.bind("<<ComboboxSelected>>", lambda event: self.create_chart_and_add_entries())
        
         # Chart Frame Widgets pos
        self.chart_month.place(x=20, y=20)
        self.chart_year.place(x=170, y=20)
        
        # Treeview Expense
        lbl_expense = tk.Label(
            self.chart_frame,
            text="Expenses",
            font=("katibeh", 18),
            bg="#FFFAF0"
        ).place(x=450, y=10)
        
        self.tv_chart_expense = ttk.Treeview(
            self.chart_frame,
            columns=(1, 2),
            show="headings",
            height=4,
            style="Custom.Treeview"
        )
        
        self.tv_chart_expense.column(1, anchor="w", stretch="No", width=160)
        self.tv_chart_expense.column(2, anchor="w", stretch="No", width=160)
        self.tv_chart_expense.heading(1, text="Name")
        self.tv_chart_expense.heading(2, text="Amount")
        
        # Disable TreeView Heading Resizing and selection
        self.tv_chart_expense.bind('<B1-Motion>', lambda event: 'break')
        self.tv_chart_expense.bind("<ButtonRelease-1>", lambda event: self.tv_tree_view.selection_remove(self.tv_tree_view.selection()))

        # TreeView Expense pos
        self.tv_chart_expense.place(x=350, y=50)
        
        # Treeview Income
        lbl_chart_income = tk.Label(
            self.chart_frame,
            text="Income",
            font=("katibeh", 18),
            bg="#FFFAF0"
        ).place(x=460, y=250)
        
        self.tv_chart_income = ttk.Treeview(
            self.chart_frame,
            columns=(1, 2),
            show="headings",
            height=4,
            style="Custom.Treeview"
        )
        
        self.tv_chart_income.column(1, anchor="w", stretch="No", width=160)
        self.tv_chart_income.column(2, anchor="w", stretch="No", width=160)
        self.tv_chart_income.heading(1, text="Name")
        self.tv_chart_income.heading(2, text="Amount")
        
        # Disable TreeView Heading Resizing and selection
        self.tv_chart_income.bind('<B1-Motion>', lambda event: 'break')
        self.tv_chart_income.bind("<ButtonRelease-1>", lambda event: self.tv_tree_view.selection_remove(self.tv_tree_view.selection()))
        
        # TreeView Income pos
        self.tv_chart_income.place(x=350, y=290)
        
        # Config TreeView Style
        style = ttk.Style()
        style.theme_use("clam")
        style.configure("Custom.Treeview.Heading", font=("katibeh", 12))
        style.configure("Custom.Treeview", font=("katibeh", 12, "bold"), background="#FFFAF0", fieldbackground="#FFFAF0")
        style.configure("Custom.Treeview", rowheight=35)
        
        lbl_month_total_expense_title = tk.Label(
            self.chart_frame,
            text="Total Expense:",
            font=("katibeh", 16),
            bg="#FFFAF0"
            ).place(x=20, y=380)
        
        self.lbl_month_total_expense_amount = tk.Label(
            self.chart_frame,
            text="-₱0.00",
            font=("katibeh", 16),
            bg="#FFFAF0",
            fg="red"
        )
        self.lbl_month_total_expense_amount.place(x=170, y=380)
        
        lbl_month_total_income_title = tk.Label(
            self.chart_frame,
            text="Total Income:",
            font=("katibeh", 16),
            bg="#FFFAF0"
            ).place(x=20, y=410)
        
        self.lbl_month_total_income_amount = tk.Label(
            self.chart_frame,
            text="+₱0.00",
            font=("katibeh", 16),
            bg="#FFFAF0",
            fg="green"
        )
        self.lbl_month_total_income_amount.place(x=170, y=410)
    
        # Create Chart and add List of Income and Expenses
        self.create_chart_and_add_entries()
        
    # Wrapper functions to call imported functions from function_list.py
    # def add_button(self):
    #     function.add_button(self)

    def open_calculator(self):
        Calculator(self)    
    
    def open_currency_converter(self):
        CurrencyConverter(self)
        
    def add_entry_win(self):
        function.add_entry_win(self)
        
    def add_to_db(self):
        function.add_to_db(self)        
    
    def next_date(self):
        function.next_date(self)        
    
    def previous_date(self):
        function.previous_date(self) 
    
    def edit_entries_window(self):
        function.edit_entries_window(self)
    
    def update_data_to_db(self):
        function.update_data_to_db(self)
        
    def remove_data_from_db(self):
        function.remove_data_from_db(self)
        
    def remove_window(self):
        function.remove_window(self)  
        
    def update_window(self):
        function.update_window(self) 
        
    def update_amount_label(self):
        function.update_amount_label(self)
        
    def update_total_balance(self):
        function.update_total_balance(self)   
        
    def load_entries(self):
        function.load_entries(self)  
        
    def clear_data(self):
        function.clear_data(self)  
    
    def create_chart_and_add_entries(self):
        function.create_chart_and_add_entries(self)
    
    def close_chart(self):
        function.close_chart(self)
    
    def filter_treeview(self):
        function.filter_treeview(self)
        
        
    
                
# Start the program
if __name__ == "__main__":
    app = LoadingScreen()
    app.mainloop()
    
    # app = MyApp()
    # app.mainloop()

