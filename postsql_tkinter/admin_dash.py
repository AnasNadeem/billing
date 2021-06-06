from tkinter import *
from PIL import Image, ImageTk
from all_prod_list import AllProdDash
from transaction_list import TransDash
from user_list import UserListDash
from about_soft import AboutDash
from main_win import BillDash
import psycopg2
from tkinter import messagebox

DB_HOST = 'localhost'
DB_NAME = 'postgres'
DB_USER = 'postgres'
DB_PASS = 'Anas@123Great'

class AdminDash:
    def __init__(self, window,username):
        self.window = window
        self.username = username
        self.window.geometry("1366x720+70+50")
        self.main_black_color = '#0f0f0f'
        self.main_white_color = '#f8f8f8'
        self.window['bg'] = self.main_black_color
        # self.window.iconbitmap("")
        self.window.resizable(False, False)

        # Login Dashboard Text 
        if self.check_admin_user():
            self.window.title("Admin Dashboard")
            admin_dash_text = Label(window, text='Admin Dashboard',font=("Roboto Regular", 36), fg=self.main_white_color,bg=self.main_black_color)
            admin_dash_text.place(x=0,y=0)
        else:
            self.window.title("User Dashboard")
            admin_dash_text = Label(window, text='User Dashboard',font=("Roboto Regular", 36), fg=self.main_white_color,bg=self.main_black_color)
            admin_dash_text.place(x=0,y=0)
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
        self.inventory_login_btn.place(x=490, y=100)

        # Transactions  BUTTON
        self.transaction_image_open = Image.open('images/transactiontxt.png')
        self.transaction_image_open = self.transaction_image_open.resize((380, 100), Image.ANTIALIAS)
        self.transaction_txt_img = ImageTk.PhotoImage(self.transaction_image_open)

        self.transaction_txt_btn = Button(window, image=self.transaction_txt_img,
                                        cursor='hand2',command=self.transaction_new_win,
                                        borderwidth=0,border=0,bg=self.main_black_color)
        self.transaction_txt_btn.image = self.transaction_txt_img
        self.transaction_txt_btn.place(x=490, y=240)

        if self.check_admin_user():
            # USER BUTTON
            self.user_image_open = Image.open('images/usertxtbtn.png')
            self.user_image_open = self.user_image_open.resize((380, 100), Image.ANTIALIAS)
            self.user_login_img = ImageTk.PhotoImage(self.user_image_open)

            self.user_login_btn = Button(window, image=self.user_login_img,
                                                cursor='hand2',command=self.user_new_win,
                                                borderwidth=0,border=0,bg=self.main_black_color)
            self.user_login_btn.image = self.user_login_img
            self.user_login_btn.place(x=490, y=380)
        
            # About BUTTON
            self.about_image_open = Image.open('images/aboutsoft.png')
            self.about_image_open = self.about_image_open.resize((380, 100), Image.ANTIALIAS)
            self.about_soft_img = ImageTk.PhotoImage(self.about_image_open)

            self.about_soft_btn = Button(window, image=self.about_soft_img,
                                            cursor='hand2',command=self.about_soft_win, 
                                            borderwidth=0,border=0,bg=self.main_black_color)
            self.about_soft_btn.image = self.about_soft_img
            self.about_soft_btn.place(x=490, y=520)
        else:
            # About BUTTON
            self.about_image_open = Image.open('images/aboutsoft.png')
            self.about_image_open = self.about_image_open.resize((380, 100), Image.ANTIALIAS)
            self.about_soft_img = ImageTk.PhotoImage(self.about_image_open)

            self.about_soft_btn = Button(window, image=self.about_soft_img,
                                            cursor='hand2',command=self.about_soft_win, 
                                            borderwidth=0,border=0,bg=self.main_black_color)
            self.about_soft_btn.image = self.about_soft_img
            self.about_soft_btn.place(x=490, y=380)
            

    def invent_new_win(self):
        self.newWindow = Toplevel(self.window)
        self.app = AllProdDash(self.newWindow,self.username)

    def transaction_new_win(self):
        self.newWindow = Toplevel(self.window)
        self.app = TransDash(self.newWindow,self.username)

    def user_new_win(self):
        self.newWindow = Toplevel(self.window)
        self.app = UserListDash(self.newWindow)
        
    def about_soft_win(self):
        self.newWindow = Toplevel(self.window)
        self.app = AboutDash(self.newWindow)

    def main_win_fun(self):
        self.newWindow = Toplevel(self.window)
        self.app = BillDash(self.newWindow,self.username)

    def check_admin_user(self):
        con = psycopg2.connect(host=DB_HOST,database=DB_NAME, user=DB_USER, password=DB_PASS)
        cur = con.cursor()
        try:
            cur.execute("""SELECT * FROM users WHERE username=%s""", (self.username,))
            row_db= cur.fetchone()
            if row_db[2]=='Admin':
                return True
            else:
                return False

        except Exception as ex:
            messagebox.showerror('Error', f'Error due to {str(ex)}', parent=self.window)