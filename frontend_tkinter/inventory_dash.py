from tkinter import *
# from tkinter.ttk import *
from PIL import Image, ImageTk
from all_prod_list import AllProdDash
from addprod import AddProdDash
from main_win import BillDash

class InventoryDash:
    def __init__(self, window):
        self.window = window
        self.window.geometry("1366x720+70+50")
        self.main_black_color = '#0f0f0f'
        self.main_white_color = '#f8f8f8'
        self.window['bg'] = self.main_black_color
        self.window.title("Inventory Dashboard")
        # self.window.iconbitmap("")
        self.window.resizable(False, False)

        # Inventory Dashboard Text 
        self.login_dash_text = Label(window, text='Inventory Dashboard',font=("Roboto Regular", 36), fg=self.main_white_color,bg=self.main_black_color)
        self.login_dash_text.place(x=0,y=0)

        # Main Window Btn 
        main_win_btn = Button(self.window, text='Main Window',
                                cursor='hand2',fg=self.main_black_color,
                                command=self.main_win_fun,                   
                                bg='white', font=('Roboto Regular', 14, "bold"),width=14)
        main_win_btn.place(x=1160, y=16)

        # All Prod List BUTTON
        self.all_product_image_open = Image.open('images/allprlisttxt.png')
        self.all_product_image_open = self.all_product_image_open.resize((380, 100), Image.ANTIALIAS)
        self.all_product_img = ImageTk.PhotoImage(self.all_product_image_open)

        self.all_product_btn = Button(window, image=self.all_product_img,
                                        cursor='hand2',command=self.all_prod_new_win,
                                        borderwidth=0,border=0,bg=self.main_black_color)

        self.all_product_btn.image = self.all_product_img
        self.all_product_btn.place(x=490, y=180)

        # Add Prod BUTTON
        self.add_prod_image_open = Image.open('images/addproducttxt.png')
        self.add_prod_image_open = self.add_prod_image_open.resize((380, 100), Image.ANTIALIAS)
        self.add_prod_img = ImageTk.PhotoImage(self.add_prod_image_open)

        self.add_prod_btn = Button(window, image=self.add_prod_img,
                                    cursor='hand2',command=self.add_prod_new_win,
                                    borderwidth=0,border=0,bg=self.main_black_color)
        self.add_prod_btn.image = self.add_prod_img
        self.add_prod_btn.place(x=490, y=340)

    def all_prod_new_win(self):
        self.newWindow = Toplevel(self.window)
        self.app = AllProdDash(self.newWindow)

    def add_prod_new_win(self):
        self.newWindow = Toplevel(self.window)
        self.app = AddProdDash(self.newWindow)

    def main_win_fun(self):
        self.newWindow = Toplevel(self.window)
        self.app = BillDash(self.newWindow)

def run_func():
    window = Tk()
    InventoryDash(window)
    window.mainloop()
        
if __name__ == '__main__':
    run_func()