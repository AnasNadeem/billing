from tkinter import *
import tkinter.ttk as ttk 
from PIL import Image, ImageTk
import sqlite3
from tkinter import messagebox

class BillDash:
    def __init__(self, window):
        self.window = window
        self.window.geometry("1366x720+70+50")
        self.main_black_color = '#0f0f0f'
        self.main_white_color = '#f8f8f8'
        self.window['bg'] = self.main_black_color
        self.window.title("Billing Software")
        # self.window.iconbitmap("")
        self.window.resizable(False, False)

        # Defining Variable 
        self.var_cus_name = StringVar()
        self.var_cus_num = StringVar()

        self.var_invoice_num = StringVar()

        self.var_search_prod_by = StringVar()
        self.var_search_prd_text = StringVar()
        
        self.var_pr_name = StringVar()
        self.var_pr_price = StringVar()
        self.var_pr_gst = DoubleVar()

        self.var_quantity_prd = IntVar()
        self.var_discount_prd = DoubleVar()

        # Login Dashboard Text 
        self.admin_dash_text = Label(window, text='Billing Software',font=("Roboto Regular", 36), fg=self.main_white_color,bg=self.main_black_color)
        self.admin_dash_text.place(x=0,y=0)

        # Dashboard Btn 
        main_win_btn = Button(self.window, text='Dashboard',
                                cursor='hand2',fg=self.main_black_color,                   
                                bg='white', font=('Roboto Regular', 14, "bold"),width=14)
        main_win_btn.place(x=1170, y=10)

        # CUSTOMER DETAILS FORM FRAME 
        self.customer_details_frame = LabelFrame(self.window,bd=2,text='Customer Details', relief=FLAT)        
        self.customer_details_frame.place(x=20, y=60, width=780, height=80)

        # Customer Name 
        customer_name_label = Label(self.customer_details_frame, text='Customer Name: ',bg="white", fg="#4f4e4d",
                                    font=("yu gothic ui", 13, "bold"))
        customer_name_label.grid(row=0, column=0,padx=20,pady=10)

        self.customer_name_entry = Entry(self.customer_details_frame,
                                    relief=SUNKEN, bg="white", fg="#6b6a69",
                                    textvariable=self.var_cus_name,
                                    font=("yu gothic ui semibold", 12))
        self.customer_name_entry.grid(row=0,column=1,padx=0,pady=10)
        self.customer_name_entry.bind('<KeyRelease>',self.cus_name_key_press_func)

        # Customer Phone Number 
        customer_num_label = Label(self.customer_details_frame, text='Customer Number: ',bg="white", fg="#4f4e4d",
                                    font=("yu gothic ui", 13, "bold"))
        customer_num_label.grid(row=0, column=2,padx=20,pady=10)

        self.customer_num_entry = Entry(self.customer_details_frame,
                                    relief=SUNKEN, bg="white", fg="#6b6a69",
                                    font=("yu gothic ui semibold", 12),
                                    textvariable=self.var_cus_num)
        self.customer_num_entry.grid(row=0,column=3,padx=0,pady=10)
        self.customer_num_entry.bind('<KeyRelease>',self.cus_num_key_press_func)

        # Bill DETAILS FORM FRAME 
        self.bill_details_frame = LabelFrame(self.window,bd=2,text='Search Bill Details', relief=FLAT)        
        self.bill_details_frame.place(x=810, y=60, width=540, height=80)

        search_txt_label = Label(self.bill_details_frame, text='Invoice No: ',bg="white", fg="#4f4e4d",
                                    font=("yu gothic ui", 13, "bold"))

        search_txt_label.grid(row=0, column=0,padx=20,pady=10)

        self.search_txt_entry = Entry(self.bill_details_frame,relief=SUNKEN, bg="white", fg="#6b6a69",
                                    font=("yu gothic ui semibold", 12),textvariable=self.var_invoice_num
                                    )
        self.search_txt_entry.grid(row=0,column=1,padx=0,pady=10)

        self.search_cus_btn = Button(self.bill_details_frame, text='Search Bill',
                                cursor='hand2',fg=self.main_white_color,                
                                bg=self.main_black_color, font=('goudy old style', 14))
        self.search_cus_btn.grid(row=0,column=2,padx=20,pady=10)

        self.search_cus_btn = Button(self.bill_details_frame, text='Clear',
                                cursor='hand2',fg=self.main_white_color,                
                                bg=self.main_black_color, font=('goudy old style', 14))
        self.search_cus_btn.grid(row=0,column=3,padx=0,pady=10)

        # Product DETAILS FORM FRAME 
        self.prod_frame = LabelFrame(self.window,bd=2,text='Product Details', relief=FLAT)        
        self.prod_frame.place(x=20, y=160, width=780, height=400)

        self.search_prod_select = ttk.Combobox(self.prod_frame,
                                values=("Select By","Product Name", "Vendor Name","Stocks Availability"),
                                state='readonly', justify=CENTER,
                                font=('goudy old style', 14),
                                textvariable=self.var_search_prod_by
                                )
        self.search_prod_select.grid(row=0, column=0,padx=40,pady=10)
        self.search_prod_select.current(0)

        self.search_prod_txt_entry = Entry(self.prod_frame,relief=SUNKEN,
                                    bg="white", fg="#6b6a69",
                                    font=("yu gothic ui semibold", 12),
                                    textvariable=self.var_search_prd_text
                                    )
        self.search_prod_txt_entry.grid(row=0,column=1,padx=0,pady=10)

        self.search_prod_btn = Button(self.prod_frame, text='Search Product',
                                cursor='hand2',fg=self.main_white_color,
                                command=self.show_search_prod_func,                
                                bg=self.main_black_color, font=('goudy old style', 14))
        self.search_prod_btn.grid(row=0,column=2,padx=20,pady=10)

        self.show_all_prod_btn = Button(self.prod_frame, text='Show All',
                                cursor='hand2',fg=self.main_white_color,
                                command=self.show_all_prod_func,                
                                bg=self.main_black_color, font=('goudy old style', 14))
        self.show_all_prod_btn.grid(row=0,column=3,padx=0,pady=10)

        #Treeview
        self.frame_for_tree = Frame(self.prod_frame, bd=2, relief=RIDGE)
        self.frame_for_tree.place(x=00, y=60,width=760, height=210)

        self.scrolly = Scrollbar(self.frame_for_tree, orient=VERTICAL)
        self.scrollx = Scrollbar(self.frame_for_tree, orient=HORIZONTAL)

        self.main_list_tree = ttk.Treeview(self.frame_for_tree,
                columns=("pr_name","sell_price","gst","stocks"), show='headings', yscrollcommand=self.scrolly.set,xscrollcommand=self.scrollx.set)

        self.main_list_tree['selectmode'] = 'browse'

        self.scrolly.pack(side=RIGHT, fill=Y)
        self.scrollx.pack(side=BOTTOM, fill=X)

        self.scrolly.config(command=self.main_list_tree.yview)
        self.scrollx.config(command=self.main_list_tree.xview)

        self.main_list_tree.heading('pr_name', text="Product Name")
        self.main_list_tree.heading('sell_price', text="Sell Price")
        self.main_list_tree.heading('gst', text="GST")
        self.main_list_tree.heading('stocks', text="Stocks")
        
        self.main_list_tree.pack(fill=BOTH, expand=1)

        self.main_list_tree.column('pr_name', width=100)
        self.main_list_tree.column('sell_price', width=100)
        self.main_list_tree.column('gst', width=100)
        self.main_list_tree.column('stocks',width=100)

        self.main_list_tree.bind("<ButtonRelease-1>", self.get_prod_fun)
        self.show_all_prod_func()

        # Product Name Label
        prod_name_label_txt = Label(self.prod_frame, text='Product Name: ',bg="white", fg="#4f4e4d",
                                    font=("yu gothic ui", 13, "bold"))
        
        prod_name_label_txt.place(x=40, y=280)

        # Product Name Dynamic Input
        self.prod_name_dyn = Label(self.prod_frame,textvariable=self.var_pr_name,fg="#4f4e4d",
                                    font=("Roboto Regular", 14, "bold"))
        
        self.prod_name_dyn.place(x=180, y=280)

        # Product Price Label
        prod_price_label_txt = Label(self.prod_frame, text='Price: ',bg="white", fg="#4f4e4d",
                                    font=("yu gothic ui", 13, "bold"))
        
        prod_price_label_txt.place(x=300, y=280)

        # Product Price Dynamic Input
        self.prod_price_dyn = Label(self.prod_frame,textvariable=self.var_pr_price, fg="#4f4e4d",
                                    font=("Roboto Regular", 14, "bold"))
        self.prod_price_dyn.place(x=360, y=280)

        # Product GST Label
        prod_gst_label_txt = Label(self.prod_frame, text='GST: ',bg="white", fg="#4f4e4d",
                                    font=("yu gothic ui", 13, "bold"))
        
        prod_gst_label_txt.place(x=460, y=280)

        # Product GST Dynamic Input
        self.gst_price_dyn = Label(self.prod_frame,textvariable=self.var_pr_gst, fg="#4f4e4d",
                                    font=("Roboto Regular", 14, "bold"))
        self.gst_price_dyn.place(x=520, y=280)
        

        quantity_txt_label = Label(self.prod_frame, text='Quantity: ',bg="white", fg="#4f4e4d",
                                    font=("yu gothic ui", 13, "bold"))
        
        quantity_txt_label.place(x=40, y=330)

        self.quantity_txt_entry = Entry(self.prod_frame,relief=SUNKEN,
                                    bg="white", fg="#6b6a69",
                                    font=("yu gothic ui semibold", 12),
                                    textvariable=self.var_quantity_prd
                                    )
        self.quantity_txt_entry.place(x=160, y=334)

        discount_txt_label = Label(self.prod_frame, text='Discount: ',bg="white", fg="#4f4e4d",
                                    font=("yu gothic ui", 13, "bold"))
        
        discount_txt_label.place(x=380, y=330)

        self.discount_txt_entry = Entry(self.prod_frame,relief=SUNKEN,
                                    bg="white", fg="#6b6a69",
                                    font=("yu gothic ui semibold", 12),
                                    textvariable=self.var_discount_prd
                                    )
        self.discount_txt_entry.place(x=500, y=334)

        self.add_to_cart_btn = Button(self.prod_frame, text='Add To Cart',
                                cursor='hand2',fg=self.main_white_color,
                                command=self.add_to_cart_func,                
                                bg=self.main_black_color, font=('goudy old style', 14))
        self.add_to_cart_btn.place(x=600, y=276)

        self.del_image_open = Image.open('images/bin.png')
        self.del_image_open = self.del_image_open.resize((36, 36), Image.ANTIALIAS)
        self.del_func_img = ImageTk.PhotoImage(self.del_image_open)

        self.del_func_btn = Button(self.prod_frame, image=self.del_func_img,
                                    cursor='hand2',command=self.delete_cart_func,
                                    borderwidth=0,border=0)
        self.del_func_btn.image = self.del_func_img
        self.del_func_btn.place(x=724, y=276)

        self.update_to_cart_btn = Button(self.prod_frame, text='Update',
                                cursor='hand2',fg=self.main_white_color,
                                command=self.update_cart_func,                
                                bg=self.main_black_color, font=('goudy old style', 12))
        self.update_to_cart_btn.place(x=700, y=326)

        # CART Frame
        self.cart_frame = Frame(self.window, bd=2, relief=FLAT)
        self.cart_frame.place(x=810, y=160, width=540, height=120)

        self.scrolly_cart = Scrollbar(self.cart_frame, orient=VERTICAL)
        self.scrollx_cart = Scrollbar(self.cart_frame, orient=HORIZONTAL)

        self.add_to_cart_tree = ttk.Treeview(self.cart_frame,
                columns=("s_no","pr_name","price","quantity","total","discount","gst"), show='headings', yscrollcommand=self.scrolly_cart.set,xscrollcommand=self.scrollx_cart.set)

        self.add_to_cart_tree['selectmode'] = 'browse'

        self.scrolly_cart.pack(side=RIGHT, fill=Y)
        self.scrollx_cart.pack(side=BOTTOM, fill=X)

        self.scrolly_cart.config(command=self.add_to_cart_tree.yview)
        self.scrollx_cart.config(command=self.add_to_cart_tree.xview)

        self.add_to_cart_tree.heading('s_no', text="S.No")
        self.add_to_cart_tree.heading('pr_name', text="Product Name")
        self.add_to_cart_tree.heading('price', text="Price")
        self.add_to_cart_tree.heading('quantity', text="Quantity")
        self.add_to_cart_tree.heading('total', text="Total Amount")
        self.add_to_cart_tree.heading('discount', text="Discount")
        self.add_to_cart_tree.heading('gst', text="GST")
        
        self.add_to_cart_tree.pack(fill=BOTH, expand=1)

        self.add_to_cart_tree.column('s_no', width=100)
        self.add_to_cart_tree.column('pr_name', width=100)
        self.add_to_cart_tree.column('price', width=100)
        self.add_to_cart_tree.column('quantity',width=100)
        self.add_to_cart_tree.column('total',width=100)
        self.add_to_cart_tree.column('discount',width=100)
        self.add_to_cart_tree.column('gst',width=100)

        self.add_to_cart_tree.bind("<ButtonRelease-1>", self.get_cart_func)

        # Bill FRAME 
        self.bill_frame = Frame(self.window, bd=2, relief=FLAT)
        self.bill_frame.place(x=810, y=300, width=540, height=400)

        self.scrolly_bill = Scrollbar(self.bill_frame, orient=VERTICAL)
        # self.scrollx_bill = Scrollbar(self.bill_frame, orient=HORIZONTAL)
        
        self.bill_text_area = Text(self.bill_frame, yscrollcommand=self.scrolly_bill.set)
        self.bill_text_area.insert(END, """\t\t   Ripe Chilli Enterprises\n\t\t\tKhagaul Patna\n\t\t\t    801105""")
        self.fill_in_bill()
        self.scrolly_bill.pack(side=RIGHT, fill=Y)
        # self.scrollx_bill.pack(side=BOTTOM, fill=X)

        self.scrolly_bill.config(command=self.bill_text_area.yview)
        # self.scrollx_bill.config(command=self.bill_text_area.xview)

        self.bill_text_area.pack(fill=BOTH, expand=1)


        # Buttons Lots of Buttons Frame
        self.buttons_lots_buttons = Frame(self.window, bd=0, relief=RIDGE)
        self.buttons_lots_buttons.place(x=20,y=580, width=780, height=120)
        
        self.total_button_button = Button(self.buttons_lots_buttons, text='Total Price',
                                cursor='hand2',fg=self.main_white_color,
                                command=self.total_price_func,                
                                bg=self.main_black_color, font=('goudy old style', 14),width=10)
        self.total_button_button.grid(row=0, column=0, padx=20, pady=40)

        self.total_button_button = Button(self.buttons_lots_buttons, text='Generate Bill',
                                cursor='hand2',fg=self.main_white_color,
                                command=self.general_bill_func,                
                                bg=self.main_black_color, font=('goudy old style', 14),width=12)
        self.total_button_button.grid(row=0, column=1, padx=20, pady=40)

        self.total_button_button = Button(self.buttons_lots_buttons, text='Print',
                                cursor='hand2',fg=self.main_white_color,                
                                bg=self.main_black_color, font=('goudy old style', 14),width=8)
        self.total_button_button.grid(row=0, column=2, padx=20, pady=40)

        self.total_button_button = Button(self.buttons_lots_buttons, text='Send On Whatsapp',
                                cursor='hand2',fg=self.main_white_color,                
                                bg=self.main_black_color, font=('goudy old style', 14),width=16)
        self.total_button_button.grid(row=0, column=3, padx=20, pady=40)

        self.total_button_button = Button(self.buttons_lots_buttons, text='Clear',
                                cursor='hand2',fg=self.main_white_color,
                                command=self.clear_all_func,                
                                bg=self.main_black_color, font=('goudy old style', 14),width=8)
        self.total_button_button.grid(row=0, column=4, padx=20, pady=40)

    def get_prod_fun(self, ev):
        f = self.main_list_tree.focus()
        content = (self.main_list_tree.item(f))
        row = content['values']
        self.var_pr_name.set(row[0])
        self.var_pr_price.set(row[1])
        self.var_pr_gst.set(row[2])
       
    def show_all_prod_func(self):
        con = sqlite3.connect(r'bs.db')
        cur = con.cursor()
        try:
            cur.execute('SELECT * FROM inventory')
            rows_db = cur.fetchall()
            self.main_list_tree.delete(*self.main_list_tree.get_children())
            for row in rows_db: 
                self.main_list_tree.insert('', END, values=(row[1], row[4],row[5] ,row[2]))

        except Exception as ex:
            messagebox.showerror('Error', f'Error due to {str(ex)}', parent=self.window)


    def show_search_prod_func(self):
        con = sqlite3.connect(r'bs.db')
        cur = con.cursor()
        try:
            if self.var_search_prod_by.get()=='Select By':
                messagebox.showwarning('Please Select', "Select an option", parent=self.window)
            elif self.var_search_prod_by.get()=='Product Name':
                cur.execute('SELECT * FROM inventory WHERE pr_name=?', (self.var_search_prd_text.get(),))
                rows_db = cur.fetchall()
                if rows_db!=[]:
                    self.main_list_tree.delete(*self.main_list_tree.get_children())
                    for row in rows_db:
                        self.main_list_tree.insert('', END, values=(row[1], row[4],row[5] ,row[2]))
                else:
                    messagebox.showinfo('No Matching Results', f'Nothing Matched With Product Name: {self.var_search_prd_text.get()}.', parent=self.window)
                    self.show_all_prod_func()
            elif self.var_search_prod_by.get()=='Vendor Name':
                cur.execute('SELECT * FROM inventory WHERE ven_name=?', (self.var_search_prd_text.get(),))
                rows_db = cur.fetchall()
                if rows_db!=[]:
                    self.main_list_tree.delete(*self.main_list_tree.get_children())
                    for row in rows_db:
                        self.main_list_tree.insert('', END, values=(row[1], row[4],row[5] ,row[2]))
                else:
                    messagebox.showinfo('No Matching Results', f'Nothing Matched With Vendor Number: {self.var_search_prd_text.get()}.', parent=self.window)
                    self.show_all_prod_func()
            elif self.var_search_prod_by.get()=='Stocks Availability':
                cur.execute('SELECT * FROM inventory WHERE stocks > ?', (self.var_search_prd_text.get(),))
                rows_db = cur.fetchall()
                if rows_db!=[]:
                    self.main_list_tree.delete(*self.main_list_tree.get_children())
                    for row in rows_db:
                        self.main_list_tree.insert('', END, values=(row[1], row[4],row[5] ,row[2]))
                else:
                    messagebox.showinfo('No Matching Results', f'Nothing Matched With Stocks availability of {self.var_search_prd_text.get()}.', parent=self.window)
                    self.show_all_prod_func()
        except Exception as ex:
            messagebox.showerror('Error', f'Error due to {str(ex)}')
        
    def clear_prod_fun(self):
        self.var_search_prod_by.set('Search By')
        self.var_search_prd_text.set('')
        self.var_pr_name.set('')
        self.var_pr_price.set('')
        self.var_pr_gst.set(0.0)
        self.var_quantity_prd.set(0)
        self.var_discount_prd.set(0.0)

    def add_to_cart_func(self):
        if self.var_pr_name.get()=='':
            messagebox.showerror('Empty Input','Please Select A Product', parent=self.window)
        elif self.var_quantity_prd.get()==0:
            messagebox.showerror('Empty Input','Please Select Quantity', parent=self.window)
        else:
            con = sqlite3.connect(r'bs.db')
            cur = con.cursor()
            try:
                cur.execute('SELECT * FROM inventory where pr_name=? and sell_price=?',(self.var_pr_name.get(),self.var_pr_price.get()))
                row_db = cur.fetchone()
                if row_db[2]>=self.var_quantity_prd.get():
                    total_amount_pr = (float(self.var_pr_price.get()) * float(self.var_quantity_prd.get()))
                    self.add_to_cart_tree.insert('', END, values=(
                    (len(self.add_to_cart_tree.get_children())+1),
                    self.var_pr_name.get(),
                    self.var_pr_price.get(),
                    self.var_quantity_prd.get(),
                    total_amount_pr,
                    self.var_discount_prd.get(),
                    self.var_pr_gst.get(),
                    ))
                    self.deselect_tree_item(self.main_list_tree)
                    self.deselect_tree_item(self.add_to_cart_tree)
                    self.show_in_bill()
                    self.clear_prod_fun()
                    
                else:
                    messagebox.showerror('Too much Quantity','Not much quantity left in stocks.', parent=self.window)

            except Exception as ex:
                messagebox.showerror('Error', f'Error due to {str(ex)}', parent=self.window)

    def get_cart_func(self, ev):
        f = self.add_to_cart_tree.focus()
        content = (self.add_to_cart_tree.item(f))
        row = content['values']
        self.var_pr_name.set(row[1])
        self.var_pr_price.set(row[2])
        self.var_pr_gst.set(row[6])
        self.var_quantity_prd.set(row[3])
        self.var_discount_prd.set(row[5])

    def update_cart_func(self):
        selected = self.add_to_cart_tree.focus()
        temp = self.add_to_cart_tree.item(selected, 'values')
        new_quantity = self.var_quantity_prd.get()
        total_amount_pr = (float(self.var_pr_price.get()) * float(self.var_quantity_prd.get()))
        new_discount = self.var_discount_prd.get()
        self.add_to_cart_tree.item(selected, values=(temp[0], temp[1],temp[2],new_quantity,total_amount_pr,new_discount, temp[6]))
        self.deselect_tree_item(self.main_list_tree)
        self.deselect_tree_item(self.add_to_cart_tree)
        self.show_in_bill()
        self.clear_prod_fun()

    def delete_cart_func(self):
        f = self.add_to_cart_tree.focus()
        content = (self.add_to_cart_tree.item(f))
        row = content['values']
        self.add_to_cart_tree.delete(f)
        self.deselect_tree_item(self.main_list_tree)
        self.deselect_tree_item(self.add_to_cart_tree)
        self.show_in_bill()
        self.clear_prod_fun()

    def clear_all_func(self):
        self.clear_prod_fun()
        self.var_cus_name.set('')
        self.var_cus_num.set('')
        self.deselect_tree_item(self.main_list_tree)
        self.deselect_tree_item(self.add_to_cart_tree)
        self.add_to_cart_tree.delete(*self.add_to_cart_tree.get_children())
        self.bill_text_area.delete(11.0,END)

    def deselect_tree_item(self, tree_name):
        tree_name.selection_remove(tree_name.selection())

    def total_price_func(self):
        if len(self.add_to_cart_tree.get_children())==0:
            messagebox.showerror('Error', 'Add some product to the cart.',parent=self.window)
        else:
            children_rows = self.add_to_cart_tree.get_children()
            total_price_pr = 0
            for rows in children_rows:
                total_price_pr = total_price_pr + float(self.add_to_cart_tree.item(rows)['values'][4])
            messagebox.showinfo('Total Price', f'Total Price: {total_price_pr}',parent=self.window)

    def cus_name_key_press_func(self, ev):
        self.bill_text_area.delete(5.15,5.99)
        self.bill_text_area.insert(5.16,self.var_cus_name.get())

    def cus_num_key_press_func(self, ev):
        self.bill_text_area.delete(6.17,6.99)
        self.bill_text_area.insert(6.18,self.var_cus_num.get())

    def show_in_bill(self):
        child_rows = self.add_to_cart_tree.get_children()
        self.bill_text_area.delete(11.0,END)
        for rows in child_rows:
            row = self.add_to_cart_tree.item(rows)['values']
            self.bill_text_area.insert(END,f'\n\t{row[0]}\t{row[1]}\t{row[2]}\t{row[3]}\t{row[4]}\t{row[5]}\t{row[6]}')


    def fill_in_bill(self):
        self.bill_text_area.insert(END, f'\nInvoice Number: ')
        self.bill_text_area.insert(END, f'\nCustomer Name: ')
        self.bill_text_area.insert(END, f'\nCustomer Number: ')
        self.bill_text_area.insert(END, """\n\n =============================================================""")
        self.bill_text_area.insert(END, """\n   S.No\tProduct Name\tPrice\tQuantity\tTotal Price\tDiscount\tGST""")
        self.bill_text_area.insert(END, """\n =============================================================""")

    

    def general_bill_func(self):
        pass

def run_func():
    window = Tk()
    BillDash(window)
    window.mainloop()
        
if __name__ == '__main__':
    run_func()