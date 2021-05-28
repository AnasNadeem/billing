from tkinter import *
# from tkinter.ttk import *
from PIL import Image, ImageTk

class UserListDash:
    def __init__(self, window):
        self.window = window
        self.window.geometry("1366x720+70+50")
        self.main_black_color = '#0f0f0f'
        self.main_white_color = '#f8f8f8'
        self.window['bg'] = self.main_black_color
        self.window.title("User List Dashboard")
        # self.window.iconbitmap("")
        self.window.resizable(False, False)

        # Login Dashboard Text 
        self.admin_dash_text = Label(window, text='User List Dashboard',font=("Roboto Regular", 36), fg=self.main_white_color,bg=self.main_black_color)
        self.admin_dash_text.place(x=0,y=0)


def run_func():
    window = Tk()
    UserListDash(window)
    window.mainloop()
        
if __name__ == '__main__':
    run_func()