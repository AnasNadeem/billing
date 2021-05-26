from tkinter import *
# from tkinter.ttk import *
from PIL import Image, ImageTk

class AdminDash:
    def __init__(self, window):
        self.window = window
        self.window.geometry("1366x720+70+50")
        self.main_black_color = '#0f0f0f'
        self.main_white_color = '#f8f8f8'
        self.window['bg'] = self.main_black_color
        self.window.title("Admin Dashboard")
        # self.window.iconbitmap("")
        self.window.resizable(False, False)

        # Login Dashboard Text 
        self.admin_dash_text = Label(window, text='Admin Dashboard',font=("Roboto Regular", 36), fg=self.main_white_color,bg=self.main_black_color)
        self.admin_dash_text.place(x=0,y=0)

        # Inventory  BUTTON
        self.inventory_image_open = Image.open('images/inventorytxtbtn.png')
        self.inventory_image_open = self.inventory_image_open.resize((380, 100), Image.ANTIALIAS)
        self.inventory_login_img = ImageTk.PhotoImage(self.inventory_image_open)

        self.inventory_login_btn = Button(window, image=self.inventory_login_img, borderwidth=0,border=0,bg=self.main_black_color)
        self.inventory_login_btn.image = self.inventory_login_img
        self.inventory_login_btn.place(x=490, y=100)

        # Transactions  BUTTON
        self.transaction_image_open = Image.open('images/inventorytxtbtn.png')
        self.transaction_image_open = self.transaction_image_open.resize((380, 100), Image.ANTIALIAS)
        self.transaction_txt_img = ImageTk.PhotoImage(self.transaction_image_open)

        self.transaction_txt_btn = Button(window, image=self.transaction_txt_img, borderwidth=0,border=0,bg=self.main_black_color)
        self.transaction_txt_btn.image = self.transaction_txt_img
        self.transaction_txt_btn.place(x=490, y=240)

        # USER BUTTON
        self.user_image_open = Image.open('images/usertxtbtn.png')
        self.user_image_open = self.user_image_open.resize((380, 100), Image.ANTIALIAS)
        self.user_login_img = ImageTk.PhotoImage(self.user_image_open)

        self.user_login_btn = Button(window, image=self.user_login_img, borderwidth=0,border=0,bg=self.main_black_color)
        self.user_login_btn.image = self.user_login_img
        self.user_login_btn.place(x=490, y=380)
        
        # About BUTTON
        self.about_image_open = Image.open('images/aboutsoft.png')
        self.about_image_open = self.about_image_open.resize((380, 100), Image.ANTIALIAS)
        self.about_soft_img = ImageTk.PhotoImage(self.about_image_open)

        self.about_soft_btn = Button(window, image=self.about_soft_img, borderwidth=0,border=0,bg=self.main_black_color)
        self.about_soft_btn.image = self.about_soft_img
        self.about_soft_btn.place(x=490, y=520)


def run_func():
    window = Tk()
    AdminDash(window)
    window.mainloop()
        
if __name__ == '__main__':
    run_func()