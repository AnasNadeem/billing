from tkinter import *
# from tkinter.ttk import *
from PIL import Image, ImageTk

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

        # Login Dashboard Text 
        self.login_dash_text = Label(window, text='Inventory Dashboard',font=("Roboto Regular", 36), fg=self.main_white_color,bg=self.main_black_color)
        self.login_dash_text.place(x=0,y=0)

        # ADMIN LOGIN BUTTON
        self.all_product_image_open = Image.open('images/allprlisttxt.png')
        self.all_product_image_open = self.all_product_image_open.resize((380, 100), Image.ANTIALIAS)
        self.all_product_img = ImageTk.PhotoImage(self.all_product_image_open)

        self.all_product_btn = Button(window, image=self.all_product_img, borderwidth=0,border=0,bg=self.main_black_color)
        self.all_product_btn.image = self.all_product_img
        self.all_product_btn.place(x=490, y=180)

        # USER LOGIN BUTTON
        self.add_prod_image_open = Image.open('images/addproducttxt.png')
        self.add_prod_image_open = self.add_prod_image_open.resize((380, 100), Image.ANTIALIAS)
        self.add_prod_img = ImageTk.PhotoImage(self.add_prod_image_open)

        self.add_prod_btn = Button(window, image=self.add_prod_img, borderwidth=0,border=0,bg=self.main_black_color)
        self.add_prod_btn.image = self.add_prod_img
        self.add_prod_btn.place(x=490, y=340)


def run_func():
    window = Tk()
    InventoryDash(window)
    window.mainloop()
        
if __name__ == '__main__':
    run_func()