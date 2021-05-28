from tkinter import * 
import tkinter.ttk as ttk
from PIL import Image, ImageTk

class AddProdDash:
    def __init__(self, window):
        self.window = window
        self.window.geometry("1366x720+70+50")
        self.main_black_color = '#0f0f0f'
        self.main_white_color = '#f8f8f8'
        self.window.title("Add Product Dashboard")

        self.add_prod_frame_img = Image.open('images\\add_prod_frame.png')
        self.add_prod_frame = ImageTk.PhotoImage(self.add_prod_frame_img)

        self.image_panel = Label(self.window, image=self.add_prod_frame)
        self.image_panel.image = self.add_prod_frame
        self.image_panel.pack(fill='both')

        # self.window.iconbitmap("")
        self.window.resizable(False, False)

        # Login Dashboard Text 
        self.login_dash_text = Label(window, text='Add Product', 
                                    font=("Roboto Regular", 36),
                                    fg=self.main_white_color, bg=self.main_black_color)
        self.login_dash_text.place(x=0,y=0)


        # ========================================================================
        # ============================Product Name====================================
        # ========================================================================

        self.prod_name_label = Label(self.window, text="Product Name ", bg="white", fg="#4f4e4d",
                                    font=("yu gothic ui", 13, "bold"))
        self.prod_name_label.place(x=495, y=60)

        self.prod_name_entry = Entry(self.window, highlightthickness=0, relief=FLAT, bg="white", fg="#6b6a69",
                                    font=("yu gothic ui semibold", 12))
        self.prod_name_entry.place(x=530, y=105, width=380)

        # ========================================================================
        # ============================Product Stocks====================================
        # ========================================================================

        self.prod_stock_label = Label(self.window, text="Product Stock ", bg="white", fg="#4f4e4d",
                                    font=("yu gothic ui", 13, "bold"))
        self.prod_stock_label.place(x=495, y=160)

        self.prod_stock_entry = Entry(self.window, highlightthickness=0, relief=FLAT, bg="white", fg="#6b6a69",
                                    font=("yu gothic ui semibold", 12))
        self.prod_stock_entry.place(x=530, y=205, width=380)

        # ========================================================================
        # ============================Cost Price====================================
        # ========================================================================

        self.cost_price_label = Label(self.window, text="Cost Price ", bg="white", fg="#4f4e4d",
                                    font=("yu gothic ui", 13, "bold"))
        self.cost_price_label.place(x=495, y=260)

        self.cost_price_entry = Entry(self.window, highlightthickness=0, relief=FLAT, bg="white", fg="#6b6a69",
                                    font=("yu gothic ui semibold", 12))
        self.cost_price_entry.place(x=530, y=305, width=150)

        # ========================================================================
        # ============================Selling Price====================================
        # ========================================================================

        self.sell_price_label = Label(self.window, text="Selling Price ", bg="white", fg="#4f4e4d",
                                    font=("yu gothic ui", 13, "bold"))
        self.sell_price_label.place(x=730, y=260)

        self.sell_price_entry = Entry(self.window, highlightthickness=0, relief=FLAT, bg="white", fg="#6b6a69",
                                    font=("yu gothic ui semibold", 12))
        self.sell_price_entry.place(x=750, y=303, width=150)

        # ========================================================================
        # ============================Vendor Name====================================
        # ========================================================================

        self.prod_stock_label = Label(self.window, text="Vendor Name ", bg="white", fg="#4f4e4d",
                                    font=("yu gothic ui", 13, "bold"))
        self.prod_stock_label.place(x=495, y=355)

        self.prod_stock_entry = Entry(self.window, highlightthickness=0, relief=FLAT, bg="white", fg="#6b6a69",
                                    font=("yu gothic ui semibold", 12))
        self.prod_stock_entry.place(x=530, y=405, width=380)

        # ========================================================================
        # ============================Vendor Number====================================
        # ========================================================================

        self.prod_stock_label = Label(self.window, text="Vendor Number ", bg="white", fg="#4f4e4d",
                                    font=("yu gothic ui", 13, "bold"))
        self.prod_stock_label.place(x=495, y=450)

        self.prod_stock_entry = Entry(self.window, highlightthickness=0, relief=FLAT, bg="white", fg="#6b6a69",
                                    font=("yu gothic ui semibold", 12))
        self.prod_stock_entry.place(x=530, y=502, width=380)

        

def run_func():
    window = Tk()
    AddProdDash(window)
    window.mainloop()
        
if __name__ == '__main__':
    run_func()