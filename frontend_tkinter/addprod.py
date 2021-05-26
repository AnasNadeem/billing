from tkinter import *
import tkinter.ttk as ttk
from PIL import Image, ImageTk

class AddProdDash:
    def __init__(self, window):
        self.window = window
        self.window.geometry("1366x720+70+50")
        self.main_black_color = '#0f0f0f'
        self.main_white_color = '#f8f8f8'
        self.window['bg'] = self.main_black_color
        self.window.title("Add Product Dashboard")

        # self.window.iconbitmap("")
        self.window.resizable(False, False)

        # Login Dashboard Text 
        self.login_dash_text = Label(window, text='Add Product',font=("Roboto Regular", 36), fg=self.main_white_color,bg=self.main_black_color)
        self.login_dash_text.place(x=0,y=0)


        # White Box
        self.box_image_open = Image.open('images/whitebox.png')
        self.box_image_open = self.box_image_open.resize((460, 560), Image.ANTIALIAS)
        self.box_image_img = ImageTk.PhotoImage(self.box_image_open)

        self.box_image_btn = Label(window, image=self.box_image_img, border=0)
        self.box_image_btn.image = self.box_image_img
        self.box_image_btn.place(x=453, y=80)
# https://www.youtube.com/watch?v=i4qLI9lmkqw
        self.wrapper = LabelFrame(window)        
        self.canvas_wrap = Canvas(self.wrapper)
        self.canvas_wrap.pack(side=LEFT, fill='both', expand='yes')

        self.yscrollbar = ttk.Scrollbar(self.wrapper, orient='vertical', command=self.canvas_wrap.yview)
        self.yscrollbar.pack(side=RIGHT, fill='y')

        self.canvas_wrap.configure(yscrollcommand=self.yscrollbar.set)
        self.canvas_wrap.bind('<Configure>', lambda e:self.canvas_wrap.configure( scrollregion = self.canvas_wrap.bbox('all')))
        self.frame_wrap = Frame(self.canvas_wrap)
        self.canvas_wrap.create_window((0,0), window=self.frame_wrap, anchor='nw')

        self.wrapper.place(x=463, y=110)

        # Inside Box Label Text Box 

def run_func():
    window = Tk()
    AddProdDash(window)
    window.mainloop()
        
if __name__ == '__main__':
    run_func()