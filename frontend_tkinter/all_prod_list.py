from tkinter import *
import tkinter.ttk as ttk
from PIL import Image, ImageTk

class AllProdDash:
    def __init__(self, window):
        self.window = window
        self.window.geometry("1366x720+70+50")
        self.main_black_color = '#0f0f0f'
        self.main_white_color = '#f8f8f8'
        self.window['bg'] = self.main_black_color
        self.window.title("Product List Dashboard")
        # self.window.iconbitmap("")
        self.window.resizable(False, False)

        # Login Dashboard Text 
        admin_dash_text = Label(window, text='Product List Dashboard',font=("Roboto Regular", 36), fg=self.main_white_color,bg=self.main_black_color)
        admin_dash_text.place(x=0,y=0)

        # Frame 
        self.frame_for_tree = Frame(self.window, bd=2, relief=RIDGE)
        self.frame_for_tree.place(x=10, y=100,relwidth=1, height=400)

        self.scrolly = Scrollbar(self.frame_for_tree, orient=VERTICAL)
        self.scrollx = Scrollbar(self.frame_for_tree, orient=HORIZONTAL)
        #Treeview
        self.main_list_tree = ttk.Treeview(self.frame_for_tree,
                columns=("s_no","pr_name","cost_price","sell_price","stocks", "ven_name", "ven_num"), show='headings', yscrollcommand=self.scrolly.set, xscrollcommand=self.scrollx.set )

        self.scrolly.pack(side=RIGHT, fill=Y)
        self.scrollx.pack(side=BOTTOM, fill=X)

        self.scrolly.config(command=self.main_list_tree.yview)
        self.scrollx.config(command=self.main_list_tree.xview)

        self.main_list_tree.heading('s_no', text="SNo")
        self.main_list_tree.heading('pr_name', text="Product Name")
        self.main_list_tree.heading('cost_price', text="Cost Price")
        self.main_list_tree.heading('sell_price', text="Sell Price")
        self.main_list_tree.heading('stocks', text="Stocks")
        self.main_list_tree.heading('ven_name', text="Vendor Name")
        self.main_list_tree.heading('ven_num', text="Vendor Number")
        self.main_list_tree.pack(fill=BOTH, expand=1)

        self.main_list_tree.column('s_no', width=20)
        self.main_list_tree.column('pr_name', width=100)
        self.main_list_tree.column('cost_price', width=100)
        self.main_list_tree.column('sell_price', width=100)
        self.main_list_tree.column('stocks',width=100)
        self.main_list_tree.column('ven_name',width=100)
        self.main_list_tree.column('ven_num',width=100)

def run_func():
    window = Tk()
    AllProdDash(window)
    window.mainloop()
        
if __name__ == '__main__':
    run_func()