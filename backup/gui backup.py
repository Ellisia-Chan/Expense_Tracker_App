from pathlib import Path
from tkinter import Tk, Canvas, Button, PhotoImage

class StartUp:
    def __init__(self):
        self.window = Tk()
        self.window.geometry("700x600")
        self.window.configure(bg="#FFFFFF")
        
        # Path directory to access assets
        OUTPUT_PATH = Path(__file__).parent
        ASSETS_PATH = OUTPUT_PATH / "assets"  # Adjust this path according to your project structure

        def relative_to_assets(path: str) -> Path:
            return ASSETS_PATH / Path(path)
        
        # Canvas
        self.canvas = Canvas(self.window, bg="#FFFFFF", height=600, width=700, bd=0, highlightthickness=0, relief="ridge")
        self.canvas.place(x=0, y=0)
        
        # Background color
        bg_color_img = PhotoImage(file=relative_to_assets("bg_color.png"))
        self.bg_color = self.canvas.create_image(350.0, 310.0, image=bg_color_img)
        
        # Flower background
        bg_flower_img = PhotoImage(file=relative_to_assets("bg_flower.png"))
        self.bg_flower = self.canvas.create_image(255.99999999999994, 285.99999874472445, image=bg_flower_img)
        
        # Bottom background w/ shadow
        bg_bottom_frame_img = PhotoImage(file=relative_to_assets("bg_bottom_frame.png"))
        self.bg_bottom_frame = self.canvas.create_image(350.0, 559.5, image=bg_bottom_frame_img)
        
        # Top background w/ shadow
        bg_top_frame_img = PhotoImage(file=relative_to_assets("bg_top_frame.png"))
        self.bg_top_frame = self.canvas.create_image(350.0, 39.0, image=bg_top_frame_img)

        # -------------------------------------Top widgets-------------------------------------#

        # Date Label
        lbl_date_img = PhotoImage(file=relative_to_assets("lbl_date.png"))
        self.lbl_date = self.canvas.create_image(126.0, 41.0, image=lbl_date_img)

        # Date button left (<)
        btn_date_left_img = PhotoImage(file=relative_to_assets("btn_date_left.png"))
        self.btn_date_left = Button(image=btn_date_left_img, borderwidth=0, highlightthickness=0, command=lambda: print("btn_date_left clicked"), relief="flat")
        self.btn_date_left.place(x=15.0, y=26.0, width=26.0, height=26.0)

        # Date button right (>)
        btn_date_right_img = PhotoImage(file=relative_to_assets("btn_date_right.png"))
        self.btn_date_right = Button(image=btn_date_right_img, borderwidth=0, highlightthickness=0, command=lambda: print("btn_date_right clicked"), relief="flat")
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
        btn_menu_img = PhotoImage(file=relative_to_assets("btn_menu.png"))
        self.btn_menu = Button(image=btn_menu_img, borderwidth=0, highlightthickness=0, command=lambda: print("btn_menu clicked"), relief="flat")
        self.btn_menu.place(x=7.0, y=525.0, width=70.0, height=70.0)

        # Analysis button
        btn_analysis_img = PhotoImage(file=relative_to_assets("btn_analysis.png"))
        self.btn_analysis = Button(image=btn_analysis_img, borderwidth=0, highlightthickness=0, command=lambda: print("btn_analysis clicked"), relief="flat")
        self.btn_analysis.place(x=175.0, y=525.0, width=70.0, height=70.0)

        # Accounts button
        btn_accounts_img = PhotoImage(file=relative_to_assets("btn_accounts.png"))
        self.btn_accounts = Button(image=btn_accounts_img, borderwidth=0, highlightthickness=0, command=lambda: print("btn_accounts clicked"), relief="flat")
        self.btn_accounts.place(x=315.0, y=525.0, width=70.0, height=70.0)

        # Records button
        btn_records_img = PhotoImage(file=relative_to_assets("btn_records.png"))
        self.btn_records = Button(image=btn_records_img, borderwidth=0, highlightthickness=0, command=lambda: print("btn_records clicked"), relief="flat")
        self.btn_records.place(x=455.0, y=525.0, width=70.0, height=70.0)

        # Search button
        btn_search_img = PhotoImage(file=relative_to_assets("btn_search.png"))
        self.btn_search = Button(image=btn_search_img, borderwidth=0, highlightthickness=0, command=lambda: print("btn_search clicked"), relief="flat")
        self.btn_search.place(x=617.0, y=525.0, width=70.0, height=70.0)

        # Add button
        btn_add_item_img = PhotoImage(file=relative_to_assets("btn_add_item.png"))
        self.btn_add_item = Button(image=btn_add_item_img, borderwidth=0, highlightthickness=0, command=lambda: print("btn_add_item clicked"), relief="flat")
        self.btn_add_item.place(x=569.0, y=379.0, width=129.0, height=129.0)

        self.window.resizable(False, False)
        self.window.mainloop()

if __name__ == "__main__":
    StartUp()
