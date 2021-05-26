from tkinter import *
# from tkinter.ttk import *
from PIL import Image, ImageTk

class LoginDash:
    def __init__(self, window):
        self.window = window
        self.window.geometry("1366x720+70+50")
        self.main_black_color = '#0f0f0f'
        self.main_white_color = '#f8f8f8'
        self.window['bg'] = self.main_black_color
        self.window.title("Login Dashboard")

        # self.window.iconbitmap("")
        self.window.resizable(False, False)

        # Login Dashboard Text 
        self.login_dash_text = Label(window, text='Login Dashboard',font=("Roboto Regular", 36), fg=self.main_white_color,bg=self.main_black_color)
        self.login_dash_text.place(x=0,y=0)


        # White Box
        self.box_image_open = Image.open('images/whitebox.png')
        self.box_image_open = self.box_image_open.resize((480, 500), Image.ANTIALIAS)
        self.box_image_img = ImageTk.PhotoImage(self.box_image_open)

        self.box_image_btn = Label(window, image=self.box_image_img, border=0)
        self.box_image_btn.image = self.box_image_img
        self.box_image_btn.place(x=443, y=120)

class SigninDash:
    def __init__(self, window):
        self.window = window
        self.window.geometry("1366x720+70+50")
        self.main_black_color = '#0f0f0f'
        self.main_white_color = '#f8f8f8'
        self.window['bg'] = self.main_black_color
        self.window.title("Signin Dashboard")
        # self.window.iconbitmap("")
        self.window.resizable(False, False)

        # Login Dashboard Text 
        self.login_dash_text = Label(window, text='Signin Dashboard',font=("Roboto Regular", 36), fg=self.main_white_color,bg=self.main_black_color)
        self.login_dash_text.place(x=0,y=0)

        # ADMIN LOGIN BUTTON
        self.admin_image_open = Image.open('images/adminbtn.png')
        self.admin_image_open = self.admin_image_open.resize((380, 100), Image.ANTIALIAS)
        self.admin_login_img = ImageTk.PhotoImage(self.admin_image_open)

        self.admin_login_btn = Button(window, image=self.admin_login_img, borderwidth=0,border=0,bg=self.main_black_color,command=self.open_login_window)
        self.admin_login_btn.image = self.admin_login_img
        self.admin_login_btn.place(x=490, y=180)

        # USER LOGIN BUTTON
        self.user_image_open = Image.open('images/userloginbtn.png')
        self.user_image_open = self.user_image_open.resize((380, 100), Image.ANTIALIAS)
        self.user_login_img = ImageTk.PhotoImage(self.user_image_open)

        self.user_login_btn = Button(window, image=self.user_login_img, borderwidth=0,border=0,bg=self.main_black_color,command=self.open_login_window)
        self.user_login_btn.image = self.user_login_img
        self.user_login_btn.place(x=490, y=340)

    def open_login_window(self):
        self.newWindow = Toplevel(self.window)
        self.app = LoginDash(self.newWindow)

def run_func():
    window = Tk()
    SigninDash(window)
    window.mainloop()
        
if __name__ == '__main__':
    run_func()