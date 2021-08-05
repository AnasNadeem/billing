from tkinter import *
import tkinter.ttk as ttk
from PIL import Image, ImageTk
import psycopg2
from tkinter import messagebox

DB_HOST = 'localhost'
DB_NAME = 'postgres'
DB_USER = 'postgres'
DB_PASS = 'Anas@123Great'

class TransDash:
    def __init__(self, window,username):
        self.window = window
        self.username = username
        self.window.geometry("1366x720+70+50")
        self.main_black_color = '#0f0f0f'
        self.main_white_color = '#f8f8f8'
        self.window['bg'] = self.main_black_color
        self.window.title("Transactions Lists Dashboard")
        # self.window.iconbitmap("")
        self.window.resizable(False, False)
        
        # Defining Variable 
        self.var_bill_search_by = StringVar()
        self.var_bill_search_txt = StringVar()

        # Transaction Dashboard Text 
        self.admin_dash_text = Label(window, text='Transactions Lists Dashboard',font=("Roboto Regular", 36), fg=self.main_white_color,bg=self.main_black_color)
        self.admin_dash_text.place(x=0,y=0)

        # Main Window Btn 
        main_win_btn = Button(self.window, text='Dashboard',
                                cursor='hand2',fg=self.main_black_color,
                                command=self.go_to_dashboard_func,                   
                                bg='white', font=('Roboto Regular', 14, "bold"),width=14)
        main_win_btn.place(x=1160, y=16)

        # Frame 
        self.frame_for_tree = Frame(self.window, bd=2, relief=RIDGE)
        self.frame_for_tree.place(x=10, y=100,width=500, height=600)

        self.scrolly = Scrollbar(self.frame_for_tree, orient=VERTICAL)
        self.scrollx = Scrollbar(self.frame_for_tree, orient=HORIZONTAL)
        #Treeview
        if self.check_location():
            self.main_list_tree = ttk.Treeview(self.frame_for_tree,
                    columns=("bill_no","cus_name","cus_num","date","location"), show='headings', yscrollcommand=self.scrolly.set, xscrollcommand=self.scrollx.set )

            self.scrolly.pack(side=RIGHT, fill=Y)
            self.scrollx.pack(side=BOTTOM, fill=X)
            self.main_list_tree['selectmode'] = 'browse'
            self.scrolly.config(command=self.main_list_tree.yview)
            self.scrollx.config(command=self.main_list_tree.xview)

            self.main_list_tree.heading('bill_no', text="Bill No")
            self.main_list_tree.heading('cus_name', text="Customer Name")
            self.main_list_tree.heading('cus_num', text="Customer Number")
            self.main_list_tree.heading('date', text="Date")
            self.main_list_tree.heading('location', text="Location")
            self.main_list_tree.pack(fill=BOTH, expand=1)

            self.main_list_tree.column('bill_no', width=100)
            self.main_list_tree.column('cus_name', width=100)
            self.main_list_tree.column('cus_num',width=100)
            self.main_list_tree.column('date', width=100)
            self.main_list_tree.column('location', width=100)

            self.main_list_tree.bind("<ButtonRelease-1>", self.show_prod_func)
        else:
            self.main_list_tree = ttk.Treeview(self.frame_for_tree,
                    columns=("bill_no","cus_name","cus_num","date"), show='headings', yscrollcommand=self.scrolly.set, xscrollcommand=self.scrollx.set )

            self.scrolly.pack(side=RIGHT, fill=Y)
            self.scrollx.pack(side=BOTTOM, fill=X)
            self.main_list_tree['selectmode'] = 'browse'
            self.scrolly.config(command=self.main_list_tree.yview)
            self.scrollx.config(command=self.main_list_tree.xview)

            self.main_list_tree.heading('bill_no', text="Bill No")
            self.main_list_tree.heading('cus_name', text="Customer Name")
            self.main_list_tree.heading('cus_num', text="Customer Number")
            self.main_list_tree.heading('date', text="Date")
            self.main_list_tree.pack(fill=BOTH, expand=1)

            self.main_list_tree.column('bill_no', width=100)
            self.main_list_tree.column('cus_name', width=100)
            self.main_list_tree.column('cus_num',width=100)
            self.main_list_tree.column('date', width=100)

            self.main_list_tree.bind("<ButtonRelease-1>", self.show_prod_func)
        # Frame Search 
        self.search_frame = Frame(self.window, bd=2, relief=RIDGE)
        self.search_frame.place(x=520, y=200, height=350,width=280)
        self.search_combo_select = ttk.Combobox(self.search_frame,
                                values=("Select By","Bill No","Customer Name","Customer Num","Date"),
                                state='readonly', justify=CENTER,
                                font=('goudy old style', 14),
                                textvariable=self.var_bill_search_by
                                )
        # self.search_combo_select.place(x=10, y=10, width=180)
        self.search_combo_select.grid(row=0, column=0,padx=24,pady=20)
        self.search_combo_select.current(0)

        self.search_txt_entry = Entry(self.search_frame,relief=SUNKEN, 
                                            bg="white", fg="#6b6a69",
                                            font=("yu gothic ui semibold", 14),
                                            textvariable=self.var_bill_search_txt)
        self.search_txt_entry.grid(row=1,column=0,padx=24,pady=20)

        self.search_btn_search =Button(self.search_frame, text='Search',
                                cursor='hand2',fg=self.main_white_color,
                                command=self.search_bill_func,            
                                bg=self.main_black_color, font=('goudy old style', 14),width=16)
        self.search_btn_search.grid(row=2, column=0,padx=24, pady=20)

        self.del_trns_btn =Button(self.search_frame, text='Delete',
                                cursor='hand2',fg=self.main_white_color,
                                command=self.del_trns_func,                   
                                bg=self.main_black_color, font=('goudy old style', 14),width=16)
        self.del_trns_btn.grid(row=3, column=0,padx=10, pady=20)
        
        # Bill AREA FRAME 
        self.bill_frame = LabelFrame(self.window,text="Bill Information", bd=2, relief=FLAT)
        self.bill_frame.place(x=810, y=100, width=540, height=600)

        self.scrolly_bill = Scrollbar(self.bill_frame, orient=VERTICAL)
        
        self.bill_text_area = Text(self.bill_frame, yscrollcommand=self.scrolly_bill.set)
        self.scrolly_bill.pack(side=RIGHT, fill=Y)

        self.scrolly_bill.config(command=self.bill_text_area.yview)

        self.bill_text_area.pack(fill=BOTH, expand=1)

        self.show_all_tr_func()

    def check_location(self):
        con = psycopg2.connect(host=DB_HOST,database=DB_NAME, user=DB_USER, password=DB_PASS)
        cur = con.cursor()
        try:
            cur.execute("""SELECT * FROM users WHERE username=%s""", (self.username,))
            row_db= cur.fetchone()
            if row_db[5]=='All':
                return True
            else:
                return False

        except Exception as ex:
            messagebox.showerror('Error', f'Error due to {str(ex)}', parent=self.window)

    def show_all_tr_func(self):
        con = psycopg2.connect(host=DB_HOST,database=DB_NAME, user=DB_USER, password=DB_PASS)
        cur = con.cursor()
        try:
            cur.execute('SELECT * FROM users WHERE username=%s', (self.username,))
            check_user_row = cur.fetchone()
            if self.check_location():
                cur.execute('SELECT * FROM bill')
                rows_db = cur.fetchall()
                self.main_list_tree.delete(*self.main_list_tree.get_children())
                for row in rows_db: 
                    self.main_list_tree.insert('', END, values=(
                        row[0],
                        row[1],
                        row[2],
                        row[4],
                        row[5]
                    ))
            else:
                cur.execute('SELECT * FROM bill where location=%s', (check_user_row[5],))
                rows_db = cur.fetchall()
                self.main_list_tree.delete(*self.main_list_tree.get_children())
                for row in rows_db: 
                    self.main_list_tree.insert('', END, values=(
                        row[0],
                        row[1],
                        row[2],
                        row[4],
                    ))

        except Exception as ex:
            messagebox.showerror('Error', f'Error due to {str(ex)}', parent=self.window)

    def del_trns_func(self):
        con = psycopg2.connect(host=DB_HOST,database=DB_NAME, user=DB_USER, password=DB_PASS)
        cur = con.cursor()
        f = self.main_list_tree.focus()
        content = (self.main_list_tree.item(f))
        row = content['values']
        try:
            cur.execute('SELECT * FROM bill where bill_no=%s', (row[0],))
            yes_no = messagebox.askyesno('Are you Sure?', f'Sure to Delete {row[1]}?', parent=self.window)
            if yes_no:
                cur.execute("DELETE FROM bill where bill_no=%s",(row[0],))
                con.commit()
                self.show_all_tr_func()
            else:
                messagebox.showinfo('Not deleted', f'{row[1]} is not deleted :)', parent=self.window)
                
        except Exception as ex:
            messagebox.showerror('Error', f'Error due to {str(ex)}', parent=self.window)

    def show_prod_func(self, ev):
        con = psycopg2.connect(host=DB_HOST,database=DB_NAME, user=DB_USER, password=DB_PASS)
        cur = con.cursor()
        f = self.main_list_tree.focus()
        content = (self.main_list_tree.item(f))
        row = content['values']
        try:
            cur.execute('SELECT * FROM bill where bill_no=%s', (row[0],))
            row_db = cur.fetchone()
            file_act_path = f'invoice_bill\{row_db[1]}{row_db[2]}{row_db[4]}'
            with open(file_act_path,'r') as rf:
                rf_file_txt = rf.read()
                self.bill_text_area.delete(1.0, END)
                self.bill_text_area.insert(1.0, rf_file_txt)
        except Exception as ex:
            messagebox.showerror('Error', f'Error due to {str(ex)}', parent=self.window)

    def search_bill_func(self):
        con = psycopg2.connect(host=DB_HOST,database=DB_NAME, user=DB_USER, password=DB_PASS)
        cur = con.cursor()
        try:
            if self.var_bill_search_by.get()=='Select By':
                messagebox.showwarning('Please Select', "Select an option", parent=self.window)
            elif self.var_bill_search_by.get()=='Bill No':
                cur.execute('SELECT * FROM bill WHERE bill_no=%s', (self.var_bill_search_txt.get(),))
                rows_db = cur.fetchall()
                if rows_db!=[]:
                    self.main_list_tree.delete(*self.main_list_tree.get_children())
                    for row in rows_db:
                        self.main_list_tree.insert('', END, values=(
                    row[0],
                    row[1],
                    row[2],
                    row[4],))
                else:
                    messagebox.showinfo('No Matching Results', f'Nothing Matched With Bill No: {self.var_bill_search_txt.get()}.', parent=self.window)
            elif self.var_bill_search_by.get()=='Customer Name':
                cur.execute('SELECT * FROM bill WHERE cus_name=%s', (self.var_bill_search_txt.get().capitalize(),))
                rows_db = cur.fetchall()
                if rows_db!=[]:
                    self.main_list_tree.delete(*self.main_list_tree.get_children())
                    for row in rows_db:
                        self.main_list_tree.insert('', END, values=(
                    row[0],
                    row[1],
                    row[2],
                    row[4],))
                else:
                    messagebox.showinfo('No Matching Results', f'Nothing Matched by {self.var_bill_search_txt.get()}.', parent=self.window)
            elif self.var_bill_search_by.get()=='Customer Num':
                cur.execute('SELECT * FROM bill WHERE cus_num=%s', (self.var_bill_search_txt.get(),))
                rows_db = cur.fetchall()
                if rows_db!=[]:
                    self.main_list_tree.delete(*self.main_list_tree.get_children())
                    for row in rows_db:
                        self.main_list_tree.insert('', END, values=(
                    row[0],
                    row[1],
                    row[2],
                    row[4],))
                else:
                    messagebox.showinfo('No Matching Results', f'Nothing Matched by {self.var_bill_search_txt.get()}.', parent=self.window)
            elif self.var_bill_search_by.get()=='Date':
                cur.execute('SELECT * FROM bill WHERE date=%s', (self.var_bill_search_txt.get(),))
                rows_db = cur.fetchall()
                if rows_db!=[]:
                    self.main_list_tree.delete(*self.main_list_tree.get_children())
                    for row in rows_db:
                        self.main_list_tree.insert('', END, values=(
                    row[0],
                    row[1],
                    row[2],
                    row[4],))
                else:
                    messagebox.showinfo('No Matching Results', f'Nothing Matched With Email Id: {self.var_bill_search_txt.get()}.', parent=self.window)
        except Exception as ex:
            messagebox.showerror('Error', f'Error due to {str(ex)}', parent=self.window)

    def go_to_dashboard_func(self):
        self.window.destroy()