from tkinter import *

class ConnectDatabase:
    def __init__(self, window):
        self.window = window
        self.window.geometry("1366x720+0+0")
        self.window.title("Database Connection Form")
        # self.window.iconbitmap("")
        self.window.resizable(False, False)

def win():
    window = Tk()
    ConnectDatabase(window)
    window.mainloop()
        
if __name__ == '__main__':
    win()