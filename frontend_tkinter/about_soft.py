from tkinter import *
# from tkinter.ttk import *
from PIL import Image, ImageTk
from main_win import BillDash
import webbrowser

class AboutDash:
    def __init__(self, window):
        self.window = window
        self.window.geometry("1366x720+70+50")
        self.main_black_color = '#0f0f0f'
        self.main_white_color = '#f8f8f8'
        self.window['bg'] = self.main_black_color
        self.window.title("About Software")
        # self.window.iconbitmap("")
        self.window.resizable(False, False)

        # Login Dashboard Text 
        about_dash_text = Label(window, text='About Software',font=("Roboto Regular", 36), fg=self.main_white_color,bg=self.main_black_color)
        about_dash_text.place(x=0,y=0)

        # Main Window Btn 
        main_win_btn = Button(self.window, text='Main Window',
                                cursor='hand2',fg=self.main_black_color,
                                command=self.main_win_fun,                   
                                bg='white', font=('Roboto Regular', 14, "bold"),width=14)
        main_win_btn.place(x=1160, y=16)

        ripe_chilli_label = Label(window, text='www.RipeChilli.com', font=('Roboto Regular', 12), cursor='hand2')
        ripe_chilli_label.place(x=600, y=680)

        ripe_chilli_label.bind("<Button-1>", lambda e: self.open_website("http://ripechilli.com"))

    def main_win_fun(self):
        self.newWindow = Toplevel(self.window)
        self.app = BillDash(self.newWindow)

    #Define a website function
    def open_website(self, url):
        webbrowser.open_new_tab(url)

def run_func():
    window = Tk()
    AboutDash(window)
    window.mainloop()
        
if __name__ == '__main__':
    run_func()