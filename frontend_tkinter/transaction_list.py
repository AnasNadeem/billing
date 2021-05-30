from tkinter import *
import tkinter.ttk as ttk
from PIL import Image, ImageTk
from main_win import BillDash

class TransDash:
    def __init__(self, window):
        self.window = window
        self.window.geometry("1366x720+70+50")
        self.main_black_color = '#0f0f0f'
        self.main_white_color = '#f8f8f8'
        self.window['bg'] = self.main_black_color
        self.window.title("Transactions Lists Dashboard")
        # self.window.iconbitmap("")
        self.window.resizable(False, False)

        # Transaction Dashboard Text 
        self.admin_dash_text = Label(window, text='Transactions Lists Dashboard',font=("Roboto Regular", 36), fg=self.main_white_color,bg=self.main_black_color)
        self.admin_dash_text.place(x=0,y=0)

        # Main Window Btn 
        main_win_btn = Button(self.window, text='Main Window',
                                cursor='hand2',fg=self.main_black_color,
                                command=self.main_win_fun,                   
                                bg='white', font=('Roboto Regular', 14, "bold"),width=14)
        main_win_btn.place(x=1160, y=16)

        # Frame 
        self.frame_for_tree = Frame(self.window, bd=2, relief=RIDGE)
        self.frame_for_tree.place(x=10, y=100,relwidth=1, height=400)

        self.scrolly = Scrollbar(self.frame_for_tree, orient=VERTICAL)
        self.scrollx = Scrollbar(self.frame_for_tree, orient=HORIZONTAL)
        #Treeview
        self.main_list_tree = ttk.Treeview(self.frame_for_tree,
                columns=("bill_no","pr_name","amount","profit","cus_name","cus_num", "date"), show='headings', yscrollcommand=self.scrolly.set, xscrollcommand=self.scrollx.set )

        self.scrolly.pack(side=RIGHT, fill=Y)
        self.scrollx.pack(side=BOTTOM, fill=X)

        self.scrolly.config(command=self.main_list_tree.yview)
        self.scrollx.config(command=self.main_list_tree.xview)

        self.main_list_tree.heading('bill_no', text="Bill No")
        self.main_list_tree.heading('pr_name', text="Product Name")
        self.main_list_tree.heading('amount', text="Total Amount")
        self.main_list_tree.heading('profit', text="Profit")
        self.main_list_tree.heading('cus_name', text="Customer Name")
        self.main_list_tree.heading('cus_num', text="Customer Num")
        self.main_list_tree.heading('date', text="Date")
        self.main_list_tree.pack(fill=BOTH, expand=1)

        self.main_list_tree.column('bill_no', width=100)
        self.main_list_tree.column('pr_name', width=100)
        self.main_list_tree.column('amount', width=100)
        self.main_list_tree.column('profit', width=100)
        self.main_list_tree.column('cus_name', width=100)
        self.main_list_tree.column('cus_num',width=100)
        self.main_list_tree.column('date',width=100)

        # Frame Search 
        self.search_frame = Frame(self.window, bd=2, relief=RIDGE)
        self.search_frame.place(x=240, y=520, height=150,width=900)

        self.search_combo_select = ttk.Combobox(self.search_frame,
                                values=("Select","Bill No","Pr Name", "Total Amount", "Profit","Customer Name","Customer Num","Date"),
                                state='readonly', justify=CENTER,
                                font=('goudy old style', 14)
                                )
        # self.search_combo_select.place(x=10, y=10, width=180)
        self.search_combo_select.grid(row=0, column=0,padx=40,pady=50)
        self.search_combo_select.current(0)

        self.search_txt_entry = Entry(self.search_frame,relief=RIDGE, bg="white", fg="#6b6a69",
                                            font=("yu gothic ui semibold", 12))
        self.search_txt_entry.grid(row=0,column=1,padx=0,pady=50)

        self.search_btn_search =Button(self.search_frame, text='Search',
                                cursor='hand2',fg=self.main_white_color,                   
                                bg=self.main_black_color, font=('goudy old style', 14),width=16)
        self.search_btn_search.grid(row=0, column=2,padx=40, pady=20)
        

    def main_win_fun(self):
        self.newWindow = Toplevel(self.window)
        self.app = BillDash(self.newWindow)

def run_func():
    window = Tk()
    TransDash(window)
    window.mainloop()
        
if __name__ == '__main__':
    run_func()