from tkinter import * 
import tkinter.ttk as ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import sqlite3
from main_win import BillDash
from all_prod_list import AllProdDash

class AddProdDash:
    def __init__(self, window):
        self.window = window
        self.window.geometry("1366x720+70+50")
        self.main_black_color = '#0f0f0f'
        self.main_white_color = '#f8f8f8'
        self.window.title("Add Product Dashboard")

        self.add_prod_frame_img = Image.open('images\\add_prod_multi_frame.png')
        self.add_prod_frame = ImageTk.PhotoImage(self.add_prod_frame_img)

        self.image_panel = Label(self.window, image=self.add_prod_frame)
        self.image_panel.image = self.add_prod_frame
        self.image_panel.pack(fill='both')

        # self.window.iconbitmap("")
        self.window.resizable(False, False)

        # Defining Variable
        self.var_pr_name = StringVar()
        self.var_stocks = IntVar()
        self.var_cost_price= DoubleVar()
        self.var_sell_price = DoubleVar()
        self.var_gst = DoubleVar()
        self.var_ven_name = StringVar()
        self.var_ven_num = StringVar()

        # Login Dashboard Text 
        login_dash_text = Label(window, text='Add Product', 
                                    font=("Roboto Regular", 36),
                                    fg=self.main_white_color, bg=self.main_black_color)
        login_dash_text.place(x=0,y=0)

        # Main Window Btn 
        main_win_btn = Button(self.window, text='Main Window',
                                cursor='hand2',fg=self.main_black_color,
                                command=self.main_win_fun,                   
                                bg='white', font=('Roboto Regular', 14, "bold"),width=14)
        main_win_btn.place(x=1160, y=16)

        # ========================================================================
        # ============================Product Name====================================
        # ========================================================================

        prod_name_label = Label(self.window, text="Product Name ", bg="white", fg="#4f4e4d",
                                    font=("yu gothic ui", 13, "bold"))
        prod_name_label.place(x=495, y=60)

        self.prod_name_entry = Entry(self.window, highlightthickness=0,
                                    relief=FLAT, bg="white", fg="#6b6a69",
                                    textvariable=self.var_pr_name,
                                    font=("yu gothic ui semibold", 12))
        self.prod_name_entry.place(x=530, y=105, width=380)

        # ========================================================================
        # ============================Product Stocks====================================
        # ========================================================================

        prod_stock_label = Label(self.window, text="Product Stock ", bg="white", fg="#4f4e4d",
                                    font=("yu gothic ui", 13, "bold"))
        prod_stock_label.place(x=495, y=160)

        self.prod_stock_entry = Entry(self.window, highlightthickness=0, 
                                    relief=FLAT, bg="white", fg="#6b6a69",
                                    textvariable=self.var_stocks,
                                    font=("yu gothic ui semibold", 12))
        self.prod_stock_entry.place(x=530, y=205, width=150)

        # ========================================================================
        # ============================GST====================================
        # ========================================================================

        gst_price_label = Label(self.window, text="GST ", bg="white", fg="#4f4e4d",
                                    font=("yu gothic ui", 13, "bold"))
        gst_price_label.place(x=730, y=160)

        self.gst_price_entry = Entry(self.window, highlightthickness=0, 
                                    relief=FLAT, bg="white", fg="#6b6a69",
                                    textvariable=self.var_gst,
                                    font=("yu gothic ui semibold", 12))
        self.gst_price_entry.place(x=750, y=205, width=150)

        # ========================================================================
        # ============================Cost Price====================================
        # ========================================================================

        cost_price_label = Label(self.window, text="Cost Price ", bg="white", fg="#4f4e4d",
                                    font=("yu gothic ui", 13, "bold"))
        cost_price_label.place(x=495, y=260)

        self.cost_price_entry = Entry(self.window, highlightthickness=0,
                                    relief=FLAT, bg="white", fg="#6b6a69",
                                    textvariable=self.var_cost_price,
                                    font=("yu gothic ui semibold", 12))
        self.cost_price_entry.place(x=530, y=305, width=150)

        # ========================================================================
        # ============================Selling Price====================================
        # ========================================================================

        sell_price_label = Label(self.window, text="Selling Price ", bg="white", fg="#4f4e4d",
                                    font=("yu gothic ui", 13, "bold"))
        sell_price_label.place(x=730, y=260)

        self.sell_price_entry = Entry(self.window, highlightthickness=0,
                                    relief=FLAT, bg="white", fg="#6b6a69",
                                    textvariable=self.var_sell_price,
                                    font=("yu gothic ui semibold", 12))
        self.sell_price_entry.place(x=750, y=303, width=150)

        # ========================================================================
        # ============================Vendor Name====================================
        # ========================================================================

        ven_name_label = Label(self.window, text="Vendor Name ", bg="white", fg="#4f4e4d",
                                    font=("yu gothic ui", 13, "bold"))
        ven_name_label.place(x=495, y=355)

        self.ven_name_entry = Entry(self.window, highlightthickness=0, 
                                    relief=FLAT, bg="white", fg="#6b6a69",
                                    textvariable=self.var_ven_name,
                                    font=("yu gothic ui semibold", 12))
        self.ven_name_entry.place(x=530, y=405, width=380)

        # ========================================================================
        # ============================Vendor Number====================================
        # ========================================================================

        ven_num_label = Label(self.window, text="Vendor Number ", bg="white", fg="#4f4e4d",
                                    font=("yu gothic ui", 13, "bold"))
        ven_num_label.place(x=495, y=450)

        self.ven_num_entry = Entry(self.window, highlightthickness=0, 
                                    relief=FLAT, bg="white", fg="#6b6a69",
                                    textvariable=self.var_ven_num,
                                    font=("yu gothic ui semibold", 12))
        self.ven_num_entry.place(x=530, y=502, width=380)

        self.add_prod_btn = Button(self.window, text='Add Product',
                                cursor='hand2',fg=self.main_white_color,
                                command=self.add_prod_fun,                   
                                bg=self.main_black_color, font=('Roboto Regular', 14),width=14)
        self.add_prod_btn.place(x=610, y=560)

        self.check_prod_list_btn = Button(self.window, text='Check Product List',
                                cursor='hand2',fg=self.main_white_color,
                                command=self.check_prod_list_fun,                   
                                bg=self.main_black_color, font=('Roboto Regular', 14),width=18)
        self.check_prod_list_btn.place(x=590, y=620)
        
    def add_prod_fun(self):
        con = sqlite3.connect(r'bs.db')
        cur = con.cursor()
        try:
            if  self.var_pr_name.get() == '':
                messagebox.showerror('Empty Value', "Value could not be empty", parent=self.window)
            else:
                cur.execute('SELECT * FROM inventory where pr_name=? and sell_price=?', (self.var_pr_name.get(),self.var_sell_price.get()))
                row_db = cur.fetchone()
                if row_db != None:
                    messagebox.showerror('Error', f'This Product is already added.', parent=self.window)
                else:
                    cur.execute("""
                    INSERT INTO inventory (pr_name, stocks,cost_price, sell_price, gst, ven_name, ven_num)
                    VALUES (?,?,?,?,?,?,?)
                    """, (
                        self.var_pr_name.get(),
                        self.var_stocks.get(),
                        self.var_cost_price.get(),
                        self.var_sell_price.get(),
                        self.var_gst.get(),
                        self.var_ven_name.get(),
                        self.var_ven_num.get()
                        )
                    )
                    con.commit()
                    messagebox.showinfo('Success', f'{self.var_pr_name.get()} has been added', parent=self.window)

        except Exception as ex:
            messagebox.showerror('Error', f'Error due to {str(ex)}', parent=self.window)

    def main_win_fun(self):
        self.newWindow = Toplevel(self.window)
        self.app = BillDash(self.newWindow)

    def check_prod_list_fun(self):
        self.newWindow = Toplevel(self.window)
        self.app = AllProdDash(self.newWindow)

def run_func():
    window = Tk()
    AddProdDash(window)
    window.mainloop()
        
if __name__ == '__main__':
    run_func()