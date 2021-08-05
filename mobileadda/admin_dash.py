from tkinter import *
# from PIL import Image, ImageTk
from all_prod_list import AllProdDash
from transaction_list import TransDash
from user_list import UserListDash
# from about_soft import AboutDash
from main_win import BillDash
# import psycopg2
# from tkinter import messagebox

# DB_HOST = 'localhost'
# DB_NAME = 'postgres'
# DB_USER = 'postgres'
# DB_PASS = 'Anas@123Great'

class AdminDash:
    def __init__(self, window):
        self.window = window
        # self.username = username
        self.window.geometry("1366x720+70+50")
        self.main_black_color = '#0f0f0f'
        self.main_white_color = '#f8f8f8'
        self.window['bg'] = self.main_black_color
        # self.window.iconbitmap("")
        self.window.resizable(False, False)

        # Login Dashboard Text 
        # if self.check_admin_user():
        self.window.title("Admin Dashboard")
        admin_dash_text = Label(window, text='Admin Dashboard',font=("Roboto Regular", 36), fg=self.main_white_color,bg=self.main_black_color)
        admin_dash_text.place(x=0,y=0)
        # else:
            # self.window.title("User Dashboard")
            # admin_dash_text = Label(window, text='User Dashboard',font=("Roboto Regular", 36), fg=self.main_white_color,bg=self.main_black_color)
            # admin_dash_text.place(x=0,y=0)
        # Main Window Btn 
        main_win_btn = Button(self.window, text='Main Window',
                                cursor='hand2',fg=self.main_black_color,
                                command=self.main_win_fun,                   
                                bg='white', font=('Roboto Regular', 14, "bold"),width=14)
        main_win_btn.place(x=1160, y=16)

        # Inventory  BUTTON
        self.inventory_btn = Button(window, text='All Product List',
                                        cursor='hand2',fg=self.main_black_color,
                                        # command=self.invent_new_win,
                                        bg='white', font=('Roboto Regular', 14, "bold"),width=14)
        self.inventory_btn.place(x=490, y=180)

        # Add Payment BUTTON
        self.add_payment_btn = Button(window, text='Add Payment List',
                                        cursor='hand2',fg=self.main_black_color,
                                        # command=self.invent_new_win,
                                        bg='white', font=('Roboto Regular', 14, "bold"),width=14)
        self.add_payment_btn.place(x=490, y=240)

        # Users aka Employee  BUTTON
        self.employee_btn = Button(window, text='User List',
                                    cursor='hand2',fg=self.main_black_color,
                                    # command=self.user_new_win,
                                    bg='white', font=('Roboto Regular', 14, "bold"),width=14)
        self.employee_btn.place(x=490, y=300)

        # Bill BUTTON
        self.bill_btn = Button(window, text='Transactions List',
                                    cursor='hand2',fg=self.main_black_color,
                                    # command=self.transaction_new_win,
                                    bg='white', font=('Roboto Regular', 14, "bold"),width=14)
        self.bill_btn.place(x=490, y=360)

        # About  BUTTON
        self.about_btn = Button(window, text='About',
                                    cursor='hand2',fg=self.main_black_color,
                                    # command=self.about_soft_win,
                                    bg='white', font=('Roboto Regular', 14, "bold"),width=14)
        self.about_btn.place(x=490, y=420)
            
    def invent_new_win(self):
        self.newWindow = Toplevel(self.window)
        self.app = AllProdDash(self.newWindow)

    def transaction_new_win(self):
        self.newWindow = Toplevel(self.window)
        self.app = TransDash(self.newWindow)

    def user_new_win(self):
        self.newWindow = Toplevel(self.window)
        self.app = UserListDash(self.newWindow)
        
    def main_win_fun(self):
        self.newWindow = Toplevel(self.window)
        self.app = BillDash(self.newWindow)

    # def check_admin_user(self):
    #     con = psycopg2.connect(host=DB_HOST,database=DB_NAME, user=DB_USER, password=DB_PASS)
    #     cur = con.cursor()
    #     try:
    #         cur.execute("""SELECT * FROM users WHERE username=%s""", (self.username,))
    #         row_db= cur.fetchone()
    #         if row_db[2]=='Admin':
    #             return True
    #         else:
    #             return False

    #     except Exception as ex:
    #         messagebox.showerror('Error', f'Error due to {str(ex)}', parent=self.window)

def run_func():
    window = Tk()
    AdminDash(window)
    window.mainloop()
        
if __name__ == '__main__':
    run_func()