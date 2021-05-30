from tkinter import *
# from tkinter.ttk import *
from PIL import Image, ImageTk
from inventory_dash import InventoryDash
from transaction_list import TransDash
from about_soft import AboutDash
from main_win import BillDash

class UserDash:
    def __init__(self, window):
        self.window = window
        self.window.geometry("1366x720+70+50")
        self.main_black_color = '#0f0f0f'
        self.main_white_color = '#f8f8f8'
        self.window['bg'] = self.main_black_color
        self.window.title("User Dashboard")
        # self.window.iconbitmap("")
        self.window.resizable(False, False)

        # Login Dashboard Text 
        self.admin_dash_text = Label(window, text='User Dashboard',font=("Roboto Regular", 36), fg=self.main_white_color,bg=self.main_black_color)
        self.admin_dash_text.place(x=0,y=0)

        # Main Window Btn 
        main_win_btn = Button(self.window, text='Main Window',
                                cursor='hand2',fg=self.main_black_color,
                                command=self.main_win_fun,                   
                                bg='white', font=('Roboto Regular', 14, "bold"),width=14)
        main_win_btn.place(x=1160, y=16)

        # Inventory  BUTTON
        self.inventory_image_open = Image.open('images/inventorytxtbtn.png')
        self.inventory_image_open = self.inventory_image_open.resize((380, 100), Image.ANTIALIAS)
        self.inventory_login_img = ImageTk.PhotoImage(self.inventory_image_open)

        self.inventory_login_btn = Button(window, image=self.inventory_login_img,
                                    cursor='hand2',command=self.invent_new_win,
                                    borderwidth=0,border=0,bg=self.main_black_color)
        self.inventory_login_btn.image = self.inventory_login_img
        self.inventory_login_btn.place(x=490, y=140)

        # Transactions  BUTTON
        self.transaction_image_open = Image.open('images/transactiontxt.png')
        self.transaction_image_open = self.transaction_image_open.resize((380, 100), Image.ANTIALIAS)
        self.transaction_txt_img = ImageTk.PhotoImage(self.transaction_image_open)

        self.transaction_txt_btn = Button(window, image=self.transaction_txt_img,
                                    cursor='hand2',command=self.transaction_new_win,
                                    borderwidth=0,border=0,bg=self.main_black_color)
        self.transaction_txt_btn.image = self.transaction_txt_img
        self.transaction_txt_btn.place(x=490, y=280)
        
        # About BUTTON
        self.about_image_open = Image.open('images/aboutsoft.png')
        self.about_image_open = self.about_image_open.resize((380, 100), Image.ANTIALIAS)
        self.about_soft_img = ImageTk.PhotoImage(self.about_image_open)

        self.about_soft_btn = Button(window, image=self.about_soft_img,
                                        cursor='hand2',command=self.about_soft_win, 
                                        borderwidth=0,border=0,bg=self.main_black_color)
        self.about_soft_btn.image = self.about_soft_img
        self.about_soft_btn.place(x=490, y=420)

    def invent_new_win(self):
        self.newWindow = Toplevel(self.window)
        self.app = InventoryDash(self.newWindow)

    def transaction_new_win(self):
        self.newWindow = Toplevel(self.window)
        self.app = TransDash(self.newWindow)
        
    def about_soft_win(self):
        self.newWindow = Toplevel(self.window)
        self.app = AboutDash(self.newWindow)

    def main_win_fun(self):
        self.newWindow = Toplevel(self.window)
        self.app = BillDash(self.newWindow)

def run_func():
    window = Tk()
    UserDash(window)
    window.mainloop()
        
if __name__ == '__main__':
    run_func()