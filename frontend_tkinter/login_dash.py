from tkinter import *
# from tkinter.ttk import *
from PIL import Image, ImageTk

class LoginDash:
    def __init__(self, window):
        self.window = window
        self.window.geometry("1366x720+70+50")
        self.main_black_color = '#0f0f0f'
        self.main_white_color = '#f8f8f8'
        # self.window['bg'] = self.main_black_color
        self.window.title("Login Dashboard")
        self.login_frame = ImageTk.PhotoImage \
                (file='images\\login_frame_img.png')
        self.image_panel = Label(self.window, image=self.login_frame)

        self.image_panel.pack(fill='both')

        # self.window.iconbitmap("")
        self.window.resizable(False, False)

        # Login Dashboard Text 
        self.login_dash_text = Label(window, text='Login Dashboard', 
                                    font=("Roboto Regular", 36),
                                    fg=self.main_white_color, bg=self.main_black_color)
        self.login_dash_text.place(x=0,y=0)


        # White Box
        # self.box_image_open = Image.open('images/whitebox.png')
        # self.box_image_open = self.box_image_open.resize((480, 500), Image.ANTIALIAS)
        # self.box_image_img = ImageTk.PhotoImage(self.box_image_open)

        # self.box_image_btn = Label(window, image=self.box_image_img, border=0)
        # self.box_image_btn.image = self.box_image_img
        # self.box_image_btn.place(x=443, y=120)

        # ========================================================================
        # ============================Username====================================
        # ========================================================================

        self.username_label = Label(self.window, text="Username ", bg="white", fg="#4f4e4d",
                                    font=("yu gothic ui", 13, "bold"))
        self.username_label.place(x=495, y=220)

        self.username_entry = Entry(self.window, highlightthickness=0, relief=FLAT, bg="white", fg="#6b6a69",
                                    font=("yu gothic ui semibold", 12))
        self.username_entry.place(x=530, y=255, width=380)  # trebuchet ms

        # ========================================================================
        # ============================Password====================================
        # ========================================================================

        self.password_label = Label(self.window, text="Password ",
                                    bg="white", fg="#4f4e4d",
                                    font=("yu gothic ui", 13, "bold"))
        self.password_label.place(x=495, y=335)

        self.password_entry = Entry(self.window, highlightthickness=0, relief=FLAT, bg="white", fg="#6b6a69",
                                    font=("yu gothic ui semibold", 12), show="*")
        self.password_entry.place(x=530, y=370, width=355)  # trebuchet ms

        self.show_image = ImageTk.PhotoImage \
            (file='images\\show.png')

        self.hide_image = ImageTk.PhotoImage \
            (file='images\\hide.png')

        self.show_button = Button(self.window, image=self.show_image, relief=FLAT,
                                  activebackground="white", command=self.show
                                  , borderwidth=0, background="white", cursor="hand2")
        self.show_button.place(x=890, y=377)

        # ========================================================================
        # ============================Login button================================
        # ========================================================================

        self.login = ImageTk.PhotoImage \
            (file='images\\login.png')

        self.login_button = Button(self.window, image=self.login,
                                   font=("yu gothic ui", 13, "bold"), relief=FLAT, activebackground="white"
                                   , borderwidth=0, background="white", cursor="hand2")
        self.login_button.place(x=640, y=450)

        # ========================================================================
        # ============================Forgot password=============================
        # ========================================================================

        self.forgot_button = Button(self.window, text="Forgot Password?",
                                    font=("yu gothic ui", 13, "bold underline"), fg="red", relief=FLAT,
                                    activebackground="white"
                                    , borderwidth=0, background="white", cursor="hand2")
        self.forgot_button.place(x=767, y=410)


    # Command Function 
    def show(self):
        """allow user to show the password in password field"""
        self.hide_button = Button(self.window, image=self.hide_image, command=self.hide, relief=FLAT,
                                activebackground="white"
                                , borderwidth=0, background="white", cursor="hand2")
        self.hide_button.place(x=890, y=377)
        self.password_entry.config(show='')

    def hide(self):
        """allow user to hide the password in password field"""
        self.show_button = Button(self.window, image=self.show_image, command=self.show, relief=FLAT,
                                activebackground="white"
                                , borderwidth=0, background="white", cursor="hand2")
        self.show_button.place(x=890, y=377)
        self.password_entry.config(show='*')


def run_func():
    window = Tk()
    LoginDash(window)
    window.mainloop()
        
if __name__ == '__main__':
    run_func()