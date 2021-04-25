import platform
import sys
import new_invoice
import combo_complete
import platform
import sys
import sqlite3
import tkinter.messagebox as messagebox
from tkinter.messagebox import showerror
from datetime import datetime

try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True

import Amdin_support


def vp_start_gui():
    '''Starting point when module is the main routine.'''

    global val, w, root
    root = tk.Tk()
    try:
        root.iconbitmap(default='transparent.ico')
        Amdin_support.set_Tk_var()
        top = Invoice(root)
        Amdin_support.init(root, top)
        root.mainloop()
    except:
        Amdin_support.set_Tk_var()
        top = Invoice(root)
        Amdin_support.init(root, top)
        root.mainloop()


w = None


def create_Invoice(rt, *args, **kwargs):
    '''Starting point when module is imported by another module.
       Correct form of call: 'create_Invoice(root, *args, **kwargs)' .'''
    global w, w_win, root
    # rt = root
    root = rt
    w = tk.Toplevel(root)
    Amdin_support.set_Tk_var()
    top = Invoice(w)
    Amdin_support.init(w, top, *args, **kwargs)
    return (w, top)


def destroy_Invoice():
    global w
    w.destroy()
    w = None


class Invoice:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9'  # X11 color: 'gray85'
        _ana1color = '#d9d9d9'  # X11 color: 'gray85'
        _ana2color = '#ececec'  # Closest X11 color: 'gray92'
        self.style = ttk.Style()
        if sys.platform == "win32":
            self.style.theme_use('winnative')
        self.style.configure('.', background=_bgcolor)
        self.style.configure('.', foreground=_fgcolor)
        self.style.configure('.', font="TkDefaultFont")
        self.style.map('.', background=[
                       ('selected', _compcolor), ('active', _ana2color)])

        top.geometry("747x630+296+44")
        top.minsize(120, 1)
        top.maxsize(1370, 749)
        top.resizable(1,  1)
        top.title("Amdin POS & IMS")
        top.configure(background="#d9d9d9")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")

        self.style.configure('TNotebook.Tab', background=_bgcolor)
        self.style.configure('TNotebook.Tab', foreground=_fgcolor)
        self.style.map('TNotebook.Tab', background=[
                       ('selected', _compcolor), ('active', _ana2color)])
        self.TNotebook1 = ttk.Notebook(top)
        self.TNotebook1.place(relx=0.0, rely=0.175,
                              relheight=0.827, relwidth=1.001)
        self.TNotebook1_t1 = tk.Frame(self.TNotebook1)
        self.TNotebook1.add(self.TNotebook1_t1, padding=3)
        self.TNotebook1.tab(0, text="Sale", compound="top", underline="3",)
        self.TNotebook1_t1.configure(background="#d9d9d9")
        self.TNotebook1_t1.configure(highlightbackground="#d9d9d9")
        self.TNotebook1_t1.configure(highlightcolor="black")
        self.TNotebook1_t2 = tk.Frame(self.TNotebook1)
        self.TNotebook1.add(self.TNotebook1_t2, padding=3)
        self.TNotebook1.tab(1, text="ADD", compound="top", underline="2",)
        self.TNotebook1_t2.configure(background="#d9d9d9")
        self.TNotebook1_t2.configure(highlightbackground="#d9d9d9")
        self.TNotebook1_t2.configure(highlightcolor="black")
        self.TNotebook1_t3 = tk.Frame(self.TNotebook1)
        self.TNotebook1.add(self.TNotebook1_t3, padding=3)
        self.TNotebook1.tab(2, text="Return", compound="top", underline="5",)
        self.TNotebook1_t3.configure(background="#d9d9d9")
        self.TNotebook1_t3.configure(highlightbackground="#d9d9d9")
        self.TNotebook1_t3.configure(highlightcolor="black")


#  #  # Sale Form Started

        # Bill ID Label Box
        self.bill_id = tk.IntVar()
        self.bill_box = tk.Label(
            self.TNotebook1_t1, background="white", textvariable=self.bill_id)
        self.bill_box.place(relx=0.108, rely=0.037, height=21, relwidth=0.182)

        self.Label4 = tk.Label(
            self.TNotebook1_t1, background="#d9d9d9", text='''Bill ID''')
        self.Label4.place(relx=0.029, rely=0.041, height=21, width=34)
        # Bill ID Label Box End

        # Product Price Label
        self.p_str = tk.IntVar()
        self.p_box = tk.Label(
            self.TNotebook1_t1, background="white", textvariable=self.p_str)
        self.p_box.place(relx=0.515, rely=0.041, height=21, relwidth=0.182)
        self.p_str.set("")

        self.Label5 = tk.Label(
            self.TNotebook1_t1, background="#d9d9d9", text='''Unit Price''')
        self.Label5.place(relx=0.42, rely=0.041, height=21, width=51)
        # Product Price Label End

        # Date Label
        self.s_d_str = tk.IntVar()
        self.s_d_box = tk.Label(
            self.TNotebook1_t1, background="white", textvariable=self.s_d_str)
        self.s_d_box.place(relx=0.786, rely=0.041, height=21, relwidth=0.183)
        self.s_d_str.set('')
        self.s_update_date()
        # Date Label End

        # Product Name Input Box
        self.prod_cbox = tk.IntVar()

        self.p_cbox = combo_complete.AutocompleteCombobox(self.TNotebook1_t1)
        self.p_cbox.set_completion_list(self.combo_input())
        self.p_cbox.place(relx=0.108, rely=0.138,
                          height=21, relwidth=0.183)
        self.p_cbox.focus_set()
        self.p_cbox.bind("<Tab>", self.price_focus)

        self.Label6 = tk.Label(
            self.TNotebook1_t1, background="#d9d9d9", text='''Product''')
        self.Label6.place(relx=0.02, rely=0.143, height=21, width=45)
        # Product Name Input Box End

        # Qty Box Label
        self.Label7 = tk.Label(
            self.TNotebook1_t1, background="#d9d9d9", text='''Qty''')
        self.Label7.place(relx=0.434, rely=0.143, height=21, width=45)

        self.qty_spin = tk.IntVar()

        self.qty_box = tk.Spinbox(self.TNotebook1_t1, from_=1, to=10000, background="white",
                                  buttonbackground="#d9d9d9", textvariable=self.qty_spin)
        self.qty_box.place(relx=0.515, rely=0.143,
                           relheight=0.043, relwidth=0.183)
        self.qty_box.bind("<Tab>", self.focus_next_window)
        self.qty_spin.set('1')

        # Qty Box Label End

        # Product discount Box
        self.add_disc_spin = tk.IntVar()
        self.add_disc = tk.Spinbox(self.TNotebook1_t1, from_=0,
                                   to=100, background="white", textvariable=self.add_disc_spin)
        self.add_disc.place(relx=0.108, rely=0.245,
                            relheight=0.043, relwidth=0.183)
        self.add_disc.bind("<Tab>", self.add_discount)
        self.add_disc_spin.set('0')

        self.Label8 = tk.Label(
            self.TNotebook1_t1, text='''Discount(%)''', background="#d9d9d9")
        self.Label8.place(relx=0.004, rely=0.245, height=21, width=74)
        # Product discount Box End

        # Discounted Price box
        self.disc_p_str = tk.IntVar()
        self.disc_p_box = tk.Label(
            self.TNotebook1_t1, background="white", textvariable=self.disc_p_str)
        self.disc_p_box.place(relx=0.515, rely=0.245,
                              relheight=0.043, relwidth=0.183)
        self.disc_p_str.set("")

        self.Label9 = tk.Label(
            self.TNotebook1_t1, background="#d9d9d9", text='''Discounted Price''')
        self.Label9.place(relx=0.39, rely=0.245, height=21, width=90)
        # Discounted Price box End

        # Product Table Start///
        self.style.configure('Treeview',  font="TkDefaultFont")
        self.p_table = ScrolledTreeView(
            self.TNotebook1_t1, columns="Col1 Col2 Col3 Col4 Col5")
        self.p_table.place(relx=0.005, rely=0.365,
                           relheight=0.38, relwidth=0.79)

        # # build_treeview_support starting.

        self.p_table.heading("#0", text="ID", anchor="center")
        self.p_table.column("#0", width="10", minwidth="20",
                            stretch="1", anchor="center")

        self.p_table.heading("Col1", text="Product", anchor="center")
        self.p_table.column("Col1", width="95",
                            minwidth="10", stretch="1", anchor="center")

        self.p_table.heading("Col2", text="Qty", anchor="center")
        self.p_table.column("Col2", width="65",
                            minwidth="10", stretch="1", anchor="center")

        self.p_table.heading("Col3", text="Discount(%)", anchor="center")
        self.p_table.column("Col3", width="65",
                            minwidth="20", stretch="1", anchor="center")

        self.p_table.heading("Col4", text="Price(Rs.)", anchor="center")
        self.p_table.column("Col4", width="65",
                            minwidth="20", stretch="1", anchor="center")

        self.p_table.heading("Col5", text="Total(Rs.)", anchor="center")
        self.p_table.column("Col5", width="65",
                            minwidth="20", stretch="1", anchor="center")
        self.p_table.bind("<Double-1>", self.s_selected)
        # Product Table End///

        # Sub Total Price
        self.sub = tk.IntVar()
        self.s_total = tk.Label(
            self.TNotebook1_t1, background="white",  textvariable=self.sub)
        self.s_total.place(relx=0.257, rely=0.777,
                           relheight=0.043, relwidth=0.171)
        self.sub.set("")

        self.Label10 = tk.Label(
            self.TNotebook1_t1, background="#d9d9d9", text='''Sub Total''')
        self.Label10.place(relx=0.163, rely=0.777, height=21, width=54)
        # Sub Total Price End

        # Grand Total Label
        self.Label11 = tk.Label(
            self.TNotebook1_t1, text='''Grand Total''', background="#d9d9d9")
        self.Label11.place(relx=0.508, rely=0.777, height=21, width=64)

        self.grand = tk.IntVar()
        self.g_total = tk.Label(
            self.TNotebook1_t1, background="white", textvariable=self.grand)
        self.g_total.place(relx=0.61, rely=0.777,
                           relheight=0.043, relwidth=0.183)
        self.grand.set("")
        # Grand Total Label End

        # Payment Input Box
        self.pay_box = tk.IntVar()
        self.pay = tk.Entry(self.TNotebook1_t1, background="white",
                            textvariable=self.pay_box)
        self.pay.place(relx=0.61, rely=0.838,
                       relheight=0.043, relwidth=0.183)
        self.pay.bind("<Tab>", self.pay_bal)
        self.pay_box.set("")

        self.Label12 = tk.Label(
            self.TNotebook1_t1, background="#d9d9d9", text='''Pay''')
        self.Label12.place(relx=0.534, rely=0.838, height=21, width=34)
        # Payment Input Box End

        # Total Price Balance
        self.balance = tk.IntVar()
        self.blnc = tk.Label(self.TNotebook1_t1, background="white",
                             textvariable=self.balance)
        self.blnc.place(relx=0.61, rely=0.9,
                        relheight=0.043, relwidth=0.183)
        self.balance.set("")

        self.Label13 = tk.Label(
            self.TNotebook1_t1, background="#d9d9d9", text='''Balance''')
        self.Label13.place(relx=0.52, rely=0.9, height=21, width=44)
        # Total Price Balance End

        # Add Button
        self.add_btn = tk.Button(self.TNotebook1_t1, background="#00a629",
                                 font="-family {Segoe UI} -size 12 -weight bold", foreground="#ffffff", text='''ADD''')
        self.add_btn.place(relx=0.854, rely=0.143, height=65, width=75)
        # top.bind(
        #     "<Return>", lambda event, entryField=self.p_cbox: self.adding_return(event, entryField))
        self.add_btn.bind('<Button-1>', lambda event,
                          entryField=self.p_cbox: self.adding_test(event, entryField))
        # Add Button End

        # Update Button
        self.updat_btn = tk.Button(self.TNotebook1_t1, background="#00a629",
                                   font="-family {Segoe UI} -size 12 -weight bold", foreground="#ffffff", text='''UPDATE''')
        self.updat_btn.place(relx=0.854, rely=0.368, height=65, width=75)
        self.updat_btn.bind('<Button-1>', lambda event,
                            entryField=self.p_cbox: self.s_update_test(event, entryField))
        # Update Button End

        # Delete Button
        self.Button1 = tk.Button(self.TNotebook1_t1, background="#b70000",
                                 font="-family {Segoe UI} -size 12 -weight bold", foreground="#ffffff", text='''DELETE''', command=lambda: self.deleting())
        self.Button1.place(relx=0.854, rely=0.593, height=65, width=75)
        # Delete Button End

        # Print Button
        self.print_btn = tk.Button(
            self.TNotebook1_t1, background="#bfbf00", foreground="#ffffff", font="-family {Segoe UI} -size 12 -weight bold", text='''PRINT''')
        self.print_btn.place(relx=0.854, rely=0.798, height=65, width=75)
        top.bind("<Control-p>", self.printing)
        self.print_btn.bind("<Button-1>", self.printing)
        # Print Button End

        self.sub_total = 0
        self.count = 0
        self.p_table_items = []
        self.starting()

# # # Sale Form End
#
#
# # # ADD Form Started

        # Product Name Box
        self.Label14 = tk.Label(
            self.TNotebook1_t2, background="#d9d9d9", text='''Name''')
        self.Label14.place(relx=0.041, rely=0.061, height=21, width=34)

        self.add_name = tk.IntVar()
        self.a_name = ttk.Entry(
            self.TNotebook1_t2, textvariable=self.add_name)
        self.a_name.place(relx=0.108, rely=0.061,
                          relheight=0.043, relwidth=0.183)
        self.a_name.bind("<Tab>", self.a_price_focus)
        self.a_name.focus_set()
        self.add_name.set("")
        # Product Name Box End

        # Product Price Box
        self.Label15 = tk.Label(
            self.TNotebook1_t2, background="#d9d9d9", text='''Price''')
        self.Label15.place(relx=0.4, rely=0.061, height=21, width=34)

        self.prev_price = tk.IntVar()
        self.a_price = ttk.Entry(
            self.TNotebook1_t2, textvariable=self.prev_price)
        self.a_price.place(relx=0.5, rely=0.061,
                           relheight=0.043, relwidth=0.183)
        self.a_price.bind("<Tab>", self.focus_next_window)
        self.prev_price.set("")
        # Product Price Box End

        # Date Label
        self.a_d_str = tk.IntVar()
        self.a_d_box = tk.Label(
            self.TNotebook1_t2, background="white", textvariable=self.a_d_str)
        self.a_d_box.place(relx=0.786, rely=0.06, height=21, relwidth=0.183)
        self.a_d_str.set('')
        self.a_update_date()
        # Date Label End

        # Stock Spin Box
        self.Label16 = tk.Label(
            self.TNotebook1_t2, background="#d9d9d9", text='''Stock''')
        self.Label16.place(relx=0.041, rely=0.164, height=21, width=34)

        self.stock_spin = tk.IntVar()
        self.a_stock = tk.Spinbox(self.TNotebook1_t2, from_=1.0, to=100000.0, background="white",
                                  buttonbackground="#d9d9d9", textvariable=self.stock_spin)
        self.a_stock.place(relx=0.108, rely=0.164,
                           relheight=0.039, relwidth=0.183)
        self.stock_spin.set('1')
        # Stock Spin Box End

        #  # Add Form Treeview Start
        self.style.configure('Treeview',  font="TkDefaultFont")
        self.a_tree = ScrolledTreeView(self.TNotebook1_t2)
        self.a_tree.place(relx=0.005, rely=0.266,
                          relheight=0.689, relwidth=0.800)

        self.a_tree.configure(columns="Col1 Col2 Col3")
        # build_treeview_support starting.
        self.a_tree.heading("#0", text="Product ID", anchor="center")
        self.a_tree.column("#0", width="65", minwidth="20",
                           stretch="1", anchor="center")

        self.a_tree.heading("Col1", text="Product", anchor="center")
        self.a_tree.column("Col1", width="65", minwidth="20",
                           stretch="1", anchor="center")

        self.a_tree.heading("Col2", text="Stock", anchor="center")
        self.a_tree.column("Col2", width="65",
                           minwidth="20", stretch="1", anchor="center")

        self.a_tree.heading("Col3", text="Unit Price", anchor="center")
        self.a_tree.column("Col3", width="65",
                           minwidth="20", stretch="1", anchor="center")
        self.product_show()
        self.a_tree.bind("<Double-1>", self.a_selecting)

        #  # Add Form Treeview End

        # Add Button
        self.a_add_btn = tk.Button(self.TNotebook1_t2, background="#00a629",
                                   font="-family {Segoe UI} -size 12 -weight bold", foreground="#ffffff", text='''ADD''')
        self.a_add_btn.place(relx=0.867, rely=0.19, height=70, width=75)
        self.a_add_btn.bind('<Button-1>', lambda event,
                            entryField=self.a_name: self.product_add_btn(event, entryField))
        self.TNotebook1_t2.bind(
            "<Return>", lambda event, entryField=self.a_name: self.product_add_return(event, entryField))
        # Add Button End

        # Update Button
        self.a_update_btn = tk.Button(self.TNotebook1_t2, background="#00a629",
                                      font="-family {Segoe UI} -size 12 -weight bold", foreground="#ffffff", text='''UPDATE''')
        self.a_update_btn.place(relx=0.867, rely=0.45, height=70, width=75)
        self.a_update_btn.bind('<Button-1>', lambda event,
                               entryField=self.a_name: self.product_update_btn(event, entryField))
        # Update Button End

        self.Button3 = tk.Button(self.TNotebook1_t2, background="#960105",
                                 font="-family {Segoe UI} -size 12 -weight bold", foreground="#ffffff", text='''DELETE''', command=self.product_delete)
        self.Button3.place(relx=0.867, rely=0.71, height=70, width=75)

#  #  # Add Form End
#
#
#  #  # Return Form Started

        # Date Label
        self.r_d_str = tk.IntVar()
        self.r_d_box = tk.Label(
            self.TNotebook1_t3, background="white", textvariable=self.r_d_str)
        self.r_d_box.place(relx=0.718, rely=0.041, height=21, relwidth=0.183)
        self.r_d_str.set('')
        self.r_update_date()
        # Date Label End

        # Product name box
        self.Label17 = tk.Label(
            self.TNotebook1_t3, text='''Product''', background="#d9d9d9")
        self.Label17.place(relx=0.073, rely=0.143, height=21, width=44)

        self.prod_name = tk.IntVar()
        self.p_name_box = tk.Label(
            self.TNotebook1_t3, background="white", cursor="ibeam", textvariable=self.prod_name)
        self.p_name_box.place(relx=0.162, rely=0.143,
                              relheight=0.043, relwidth=0.182)
        self.prod_name.set("")
        # Product name box End

        # Discounted Price box
        self.Label18 = tk.Label(
            self.TNotebook1_t3, text='''Discounted Price''', background="#d9d9d9")
        self.Label18.place(relx=0.589, rely=0.143, height=21, width=89)

        self.prod_price = tk.IntVar()
        self.price_box = tk.Label(
            self.TNotebook1_t3, background="white", cursor="ibeam", textvariable=self.prod_price)
        self.price_box.place(relx=0.716, rely=0.143,
                             relheight=0.043, relwidth=0.182)
        self.prod_price.set("")
        # Discounted Price box End

        # Discount box
        self.Label19 = tk.Label(
            self.TNotebook1_t3, background="#d9d9d9", text='''Discount(%)''')
        self.Label19.place(relx=0.056, rely=0.234, height=21, width=64)

        self.prod_disc_spin = tk.IntVar()
        self.r_disc_box = tk.Spinbox(
            self.TNotebook1_t3, from_=0, to=100, background="white", textvariable=self.prod_disc_spin)
        self.r_disc_box.place(relx=0.162, rely=0.234,
                              relheight=0.039, relwidth=0.182)
        self.r_disc_box.bind('<Tab>', self.r_update_show)
        self.prod_disc_spin.set("")
        # Discount box End

        # Qty box
        self.Label20 = tk.Label(
            self.TNotebook1_t3, background="#d9d9d9", text='''Quantity''')
        self.Label20.place(relx=0.615, rely=0.224, height=21, width=54)

        self.prod_qty_spin = tk.IntVar()
        self.r_qty_box = tk.Spinbox(self.TNotebook1_t3, from_=1.0,
                                    to=100000.0, background="white", textvariable=self.prod_qty_spin)
        self.r_qty_box.place(relx=0.716, rely=0.234,
                             relheight=0.039, relwidth=0.182)
        self.prod_qty_spin.set("")
        # Qty box End

        # Bill Search
        self.label_bill_id = tk.Label(
            self.TNotebook1_t3, background="#d9d9d9", text='''Bill ID''')
        self.label_bill_id.place(relx=0.081, rely=0.041, height=21, width=34)

        self.bill_id_box = ttk.Entry(self.TNotebook1_t3, cursor="ibeam")
        self.bill_id_box.place(relx=0.162, rely=0.041,
                               relheight=0.043, relwidth=0.182)
        self.bill_id_box.focus_set()

        self.srch_btn = tk.Button(self.TNotebook1_t3, background="#d9d9d9",
                                  font="-family {Segoe UI} -size 10 -weight bold", text='''Search''')
        self.srch_btn.place(relx=0.378, rely=0.041, height=21, width=87)
        self.srch_btn.bind(
            "<Button-1>", lambda event, entryField=self.p_name_box: self.searching_return(event, entryField))
        # Bill Search End

        #
        # Return Treeview Start

        self.style.configure('Treeview',  font="TkDefaultFont")
        self.r_table = ScrolledTreeView(
            self.TNotebook1_t3, columns="Col1 Col2 Col3 Col4 Col5")
        self.r_table.place(
            relx=0.014, rely=0.346, relheight=0.523, relwidth=0.839)

        # build_treeview_support starting.
        self.r_table.heading("#0", text="I.D", anchor="center")
        self.r_table.column(
            "#0", width="10", minwidth="20", stretch="1", anchor="center")

        self.r_table.heading("Col1", text="Item Name", anchor="center")
        self.r_table.column(
            "Col1", width="95", minwidth="20", stretch="1", anchor="center")

        self.r_table.heading("Col2", text="Qty", anchor="center")
        self.r_table.column(
            "Col2", width="65", minwidth="10", stretch="1", anchor="center")

        self.r_table.heading(
            "Col3", text="Discount(%)", anchor="center")
        self.r_table.column(
            "Col3", width="65", minwidth="20", stretch="1", anchor="center")

        self.r_table.heading("Col4", text="Price (Rs.)", anchor="center")
        self.r_table.column(
            "Col4", width="65", minwidth="20", stretch="1", anchor="center")

        self.r_table.heading("Col5", text="Total (Rs.)", anchor="center")
        self.r_table.column(
            "Col5", width="65", minwidth="20", stretch="1", anchor="center")

        self.r_table.bind("<Double-1>", self.r_selecting)

        # Return Treeview End
        #

        # Grand Total box
        self.Label21 = tk.Label(
            self.TNotebook1_t3, background="#d9d9d9", text='''Grand Total''')
        self.Label21.place(relx=0.554, rely=0.896, height=21, width=74)

        self.r_grand = tk.IntVar()
        self.grand_box = tk.Label(
            self.TNotebook1_t3, cursor="ibeam", background="white", textvariable=self.r_grand)
        self.grand_box.place(relx=0.673, rely=0.896,
                             relheight=0.043, relwidth=0.182)
        self.r_grand.set("")
        # Grand Total box End

        # Update Button
        self.updt_btn = tk.Button(self.TNotebook1_t3, background="#00a629",
                                  font="-family {Segoe UI} -size 12 -weight bold", foreground="#ffffff", text='''UPDATE''', command=self.r_update)
        self.updt_btn.place(relx=0.878, rely=0.407, height=70, width=75)
        self.updt_btn.bind('<Button-1>', lambda event,
                           entryField=self.r_disc_box: self.r_update_test(event, entryField))
        # Update Button End

        # Delete Button
        self.dlt_btn = tk.Button(self.TNotebook1_t3, font="-family {Segoe UI} -size 12 -weight bold",
                                 background="#920104", foreground="#ffffff", text='''DELETE''', command=self.r_deleting)
        self.dlt_btn.place(relx=0.878, rely=0.672, height=70, width=75)
        # Delete Button End

        self.Label1 = tk.Label(top)
        self.Label1.place(relx=0.274, rely=0.019,
                          relheight=0.137, relwidth=0.46)
        self.Label1.configure(activebackground="#f9f9f9")
        self.Label1.configure(activeforeground="black")
        self.Label1.configure(background="#000000")
        self.Label1.configure(borderwidth="7")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(font="-family {Calibri} -size 18 -weight bold")
        self.Label1.configure(foreground="#ffffff")
        self.Label1.configure(highlightbackground="#d9d9d9")
        self.Label1.configure(highlightcolor="black")
        self.Label1.configure(text='''Company Name''')

        self.Frame1 = tk.Frame(top)
        self.Frame1.place(relx=0.758, rely=0.019,
                          relheight=0.137, relwidth=0.234)
        self.Frame1.configure(relief='groove')
        self.Frame1.configure(borderwidth="2")
        self.Frame1.configure(relief="groove")
        self.Frame1.configure(background="#ffffff")
        self.Frame1.configure(highlightbackground="#d9d9d9")
        self.Frame1.configure(highlightcolor="black")

        self.Label2 = tk.Label(self.Frame1)
        self.Label2.place(relx=0.137, rely=0.14,
                          relheight=0.26, relwidth=0.826)
        self.Label2.configure(activebackground="#f9f9f9")
        self.Label2.configure(activeforeground="black")
        self.Label2.configure(background="#ffffff")
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(
            font="-family {Calibri} -size 12 -weight bold -slant italic")
        self.Label2.configure(foreground="#000000")
        self.Label2.configure(highlightbackground="#d9d9d9")
        self.Label2.configure(highlightcolor="black")
        self.Label2.configure(text='''abc@xyz.com''')

        self.Label3 = tk.Label(self.Frame1)
        self.Label3.place(relx=0.069, rely=0.57,
                          relheight=0.26, relwidth=0.850)
        self.Label3.configure(activebackground="#f9f9f9")
        self.Label3.configure(activeforeground="black")
        self.Label3.configure(background="#ffffff")
        self.Label3.configure(disabledforeground="#a3a3a3")
        self.Label3.configure(
            font="-family {Calibri} -size 12 -weight bold -slant italic")
        self.Label3.configure(foreground="#000000")
        self.Label3.configure(highlightbackground="#d9d9d9")
        self.Label3.configure(highlightcolor="black")
        self.Label3.configure(text='''+92-300-0000000''')

        self.Labelframe1 = tk.LabelFrame(top)
        self.Labelframe1.place(relx=0.016, rely=0.019,
                               relheight=0.137, relwidth=0.234)
        self.Labelframe1.configure(relief='ridge')
        self.Labelframe1.configure(foreground="black")
        self.Labelframe1.configure(labelanchor="n")
        self.Labelframe1.configure(relief="ridge")
        self.Labelframe1.configure(text='''LOGO''')
        self.Labelframe1.configure(background="#d9d9d9")
        self.Labelframe1.configure(highlightbackground="#d9d9d9")
        self.Labelframe1.configure(highlightcolor="black")

#  #  # Return Form End
#

#
# Sale Product Functions Start

    def starting(self):
        conn = sqlite3.connect('ims.db')
        c = conn.cursor()

        c.execute("SELECT * FROM bills")
        items = c.fetchall()

        bill_id = items[-1]

        bill_ids = bill_id[0]

        bil_id = bill_ids + 1
        self.bill_id.set(bil_id)
        c.close()
        conn.close()

    def s_selected(self, event):
        name = self.p_table.item(self.p_table.selection())['values'][0]
        qty = self.p_table.item(self.p_table.selection())['values'][1]
        disc = self.p_table.item(self.p_table.selection())['values'][2]
        disc_price = self.p_table.item(self.p_table.selection())['values'][3]

        conn = sqlite3.connect('ims.db')

        my_cursor = conn.execute(
            "SELECT rowid,* FROM product WHERE name=?", (name,))
        data_row = my_cursor.fetchone()

        price = data_row[3]

        my_cursor.close()
        conn.close()

        self.p_cbox.set(name)
        self.qty_spin.set(qty)
        self.add_disc_spin.set(disc)
        self.p_str.set(price)
        self.disc_p_str.set(disc_price)

    def s_update_test(self, event, entryField):

        name = self.p_cbox.get()

        if name in self.p_table_items:
            self.s_update()

            root.after(1, lambda: entryField.focus_set())

            return("break")
        else:
            messagebox.showerror("Warning", "Please Add Item First!")

    def s_update(self):

        selected = self.p_table.focus()

        name = str(self.p_table.item(self.p_table.selection())['values'][0])

        stock = int(float(self.p_table.item(
            self.p_table.selection())['values'][1]))

        prod_qty = int(self.qty_box.get())

        conn = sqlite3.connect('ims.db')

        my_cursor = conn.execute(
            "SELECT rowid,* FROM product WHERE name=?", (name,))
        data_row = my_cursor.fetchone()

        prod_price = data_row[3]

        st = data_row[2]

        disc_prcnt = float(self.add_disc.get())

        disc_price = (disc_prcnt / 100) * prod_price

        d_prod_price = prod_price - disc_price

        print("discounted price: ", d_prod_price, type(d_prod_price))

        t_price = d_prod_price * prod_qty

        print("total price: ", t_price, type(t_price))

        self.p_table.item(selected, text="", values=(
            name, prod_qty, disc_prcnt, d_prod_price, t_price))

        if stock > prod_qty:
            stk = stock - prod_qty
            qty = st + stk
            my_cursor = conn.execute(
                "UPDATE product SET stock = ? WHERE name = ?", (qty, name))
            conn.commit()

        elif stock < prod_qty:
            stk = prod_qty - stock
            qty = st - stk

            if qty < 0:
                messagebox.showerror("Warning", "Out of Stock!")
            else:
                my_cursor = conn.execute(
                    "UPDATE product SET stock = ? WHERE name = ?", (qty, name))
                conn.commit()

        elif stock == prod_qty:
            pass

        my_cursor.close()
        conn.close()

        # For Grand Total calculation
        self.grand_total = 0
        for i in self.p_table.get_children():
            total_prices = float(self.p_table.item(i)['values'][4])
            self.grand_total += total_prices
            print(self.grand_total)

        self.grand.set(self.grand_total)

        # Clearing Boxes
        self.p_cbox.set("")
        self.qty_spin.set("0")
        self.add_disc_spin.set("0")
        self.p_str.set("")
        self.disc_p_str.set("")

    def s_update_date(self):
        global s_dates
        s_dates = datetime.today().strftime('%Y-%m-%d-%H:%M:%S')
        self.s_d_str.set(s_dates)
        self.s_d_box.after(1000, self.s_update_date)

    def a_update_date(self):
        global a_dates
        a_dates = datetime.today().strftime('%Y-%m-%d-%H:%M:%S')
        self.a_d_str.set(a_dates)
        self.a_d_box.after(1000, self.a_update_date)

    def r_update_date(self):
        global r_dates
        r_dates = datetime.today().strftime('%Y-%m-%d-%H:%M:%S')
        self.r_d_str.set(r_dates)
        self.r_d_box.after(1000, self.r_update_date)

    def printing(self, event):

        print("hello")
        conn = sqlite3.connect('ims.db')
        c = conn.cursor()

        date = s_dates

        tree_items = []

        c.execute("""INSERT INTO bills(bill_time) VALUES(?)""", (date,))

        conn.commit()

        c.execute("SELECT * FROM bills")
        items = c.fetchall()

        bill_id = items[-1]

        bill_ids = bill_id[0]

        for i in self.p_table.get_children():
            tree_items.append(self.p_table.item(i)['values'])

            item = self.p_table.item(i)['values'][0]
            quty = int(float(self.p_table.item(i)['values'][1]))
            discnt = float(self.p_table.item(i)['values'][2])
            prices = float(self.p_table.item(i)['values'][3])
            total_prices = float(self.p_table.item(i)['values'][4])

            c.execute("""INSERT INTO items(item_name, qty, discount, price, total_price, bill_id) VALUES(?,?,?,?,?,?)""",
                      (item, quty, discnt, prices, total_prices, bill_ids))
            conn.commit()

        print(tree_items)

        for i, item in enumerate(tree_items):
            item.insert(0, i+1)

        print(tree_items)

        c.close()
        conn.close()

        grand_total = self.grand_total

        new_invoice.print_invoice(bill_ids, date, tree_items, grand_total)

        # Clearing boxes
        self.p_table_items = []
        self.qty_spin.set('1')
        self.p_cbox.delete(0, 'end')
        self.p_str.set("")
        self.disc_p_str.set("")
        self.add_disc_spin.set('0')
        self.sub.set("")
        self.balance.set("")
        self.grand.set("")
        self.pay_box.set("")

        self.sub_total = 0
        self.count = 0

        # tree view remove all
        for row in self.p_table.get_children():
            self.p_table.delete(row)

        # bill id increment
        bil_id = bill_ids + 1
        self.bill_id.set(bil_id)

    # Combo Input

    def combo_input(self):
        conn = sqlite3.connect('ims.db')
        cursor = conn.execute('select name from product')

        result = []

        for row in cursor.fetchall():
            result.append(row[0])

        print(result)

        cursor.close()
        conn.close()

        return result

    # Price Input Box
    def price_focus(self, event):

        name = str(self.p_cbox.get())

        conn = sqlite3.connect('ims.db')
        my_cursor = conn.execute(
            "SELECT rowid,* FROM product WHERE name=?", (name,))
        self.data_row = my_cursor.fetchone()

        price = self.data_row[3]

        event.widget.tk_focusNext().focus()

        self.p_str.set(price)

        my_cursor.close()
        conn.close()

        return("break")

    def add_discount(self, event):

        name = str(self.p_cbox.get())

        conn = sqlite3.connect('ims.db')
        my_cursor = conn.execute(
            "SELECT rowid,* FROM product WHERE name=?", (name,))
        data_row = my_cursor.fetchone()

        get_price = data_row[3]

        get_add_disc = int(self.add_disc.get())

        disc_price = (get_add_disc / 100) * get_price

        price = get_price - disc_price

        self.disc_p_str.set(price)

        my_cursor.close()
        conn.close()

        event.widget.tk_focusNext().focus()

        return('break')

    def focus_next_window(self, event):

        event.widget.tk_focusNext().focus()

        return("break")

    def adding_test(self, event, entryField):

        self.adding()

        root.after(1, lambda: entryField.focus_set())

        return("break")

    def adding(self):

        try:
            print("Name box: ", self.p_cbox.get())

            name = str(self.p_cbox.get())

            print("Qty box: ", self.qty_box.get())

            qty = float(self.qty_box.get())

            if name not in self.p_table_items:

                conn = sqlite3.connect('ims.db')

                my_cursor = conn.execute(
                    "SELECT rowid,* FROM product WHERE name=?", (name,))
                data_row = my_cursor.fetchone()

                get_price = data_row[3]

                get_add_disc = int(self.add_disc.get())

                disc_price = ((get_add_disc / 100) * get_price)

                price = get_price - disc_price

                ids = data_row[0]

                st = data_row[2] - qty

                if st < 0:
                    messagebox.showerror("Warning", "Out of Stock!")

                else:
                    p_total = price * qty

                    print(p_total)

                    self.sub_total = self.sub_total + p_total

                    self.sub.set(self.sub_total)

                    print("Subtracted Stock:", st)

                    # discount = float(self.disc.get())
                    self.grand_total = self.sub_total
                    self.grand.set(self.grand_total)

                    # Updating Stock value

                    my_cursor = conn.execute(
                        "UPDATE product SET stock = ? WHERE rowid = ?", (st, ids))
                    conn.commit()

                    # adding to tree view
                    #  iid = self.count,

                    self.p_table.insert('', 'end', text=self.count,
                                        values=(data_row[1], qty, get_add_disc, price, p_total)),
                    self.count += 1

                    self.p_table_items.append(name)

                    print(self.p_table_items)

                    # Clearing boxes
                    self.qty_spin.set('1')
                    self.p_cbox.delete(0, 'end')
                    self.p_str.set("")
                    self.disc_p_str.set("")
                    self.add_disc_spin.set('0')

                my_cursor.close()
                conn.close()

                for row in self.a_tree.get_children():
                    self.a_tree.delete(row)

                self.product_show()

            else:
                messagebox.showerror("Warning", "Please Update Table Item!")

        except sqlite3.Error as my_err:
            print("error: ", my_err)

    def grand_total(self, event):

        # discount = float(self.disc.get())
        self.grand_total = self.sub_total
        print("ok")

        self.grand.set(self.grand_total)

        event.widget.tk_focusNext().focus()

        return("break")

    def pay_bal(self, event):

        self.payment = int(float(self.pay.get()))

        balanc_pay = self.payment - self.grand_total

        self.balance.set(balanc_pay)

        event.widget.tk_focusNext().focus()

        return("break")

    def deleting(self):
        # selected item
        items = self.p_table.selection()

        # getting total price of a product in tree view
        t_p = self.p_table.item(self.p_table.selection())['values'][3]
        p = float(t_p)

        # getting name of a product in tree view
        name = self.p_table.item(self.p_table.selection())['values'][0]

        # getting stock of a product in tree view
        stock = self.p_table.item(self.p_table.selection())['values'][1]
        stock = float(stock)

        # Updating DB
        conn = sqlite3.connect('ims.db')

        my_cursor = conn.execute(
            "SELECT rowid,* FROM product WHERE name=?", (name,))
        data_row = my_cursor.fetchone()

        st = data_row[2] + stock

        my_cursor = conn.execute(
            "UPDATE product SET stock = ? WHERE name = ?", (st, name))
        conn.commit()

        # print(data_row[1])
        print("Added Stock: ", st)

        my_cursor.close()
        conn.close()

        #
        # Updating Add Form Table
        for row in self.a_tree.get_children():
            self.a_tree.delete(row)

        self.product_show()

        # discount = int(float(self.disc.get()))

        if self.pay.get() == "":

            self.sub_total = self.sub_total - p
            self.sub.set(self.sub_total)
            # print("ok: ", self.sub_total)

            # Grand Total after item deleting
            self.grand_total = self.sub_total
            self.grand.set(self.grand_total)

        else:
            # Setting Sub Total after deleting items
            self.sub_total = self.sub_total - p
            self.sub.set(self.sub_total)
            # print("ok: ", self.sub_total)

            # Grand Total after item deleting
            self.grand_total = self.sub_total
            self.grand.set(self.grand_total)

            # Balance after item deleting
            self.payment = int(self.pay.get())
            balanc_pay = self.payment - self.grand_total
            self.balance.set(balanc_pay)

        self.count -= 1

        self.p_table.delete(items)

        # updating items
        self.p_table_items = []

        for i in self.p_table.get_children():
            item_num = str(self.p_table.item(i)['values'][0])
            self.p_table_items.append(item_num)

# Sale Product Functions End
#
#
# Add Product Functions

    def product_show(self):

        # Connecting DB
        conn = sqlite3.connect('ims.db')

        # Fetching Values from DB
        my_cursor = conn.execute("SELECT rowid,* FROM product")
        items = my_cursor.fetchall()

        self.item_names = []

        for item in items:
            self.a_tree.insert('', 'end', text=item[0], values=(
                item[1], item[2], item[3])),

            self.item_names.append(item[1])

        my_cursor.close()
        conn.close()

    def a_price_focus(self, event):

        try:
            name = str(self.a_name.get())

            conn = sqlite3.connect('ims.db')
            my_cursor = conn.execute(
                "SELECT rowid,* FROM product WHERE name=?", (name,))
            data_row = my_cursor.fetchone()

            price = data_row[3]

            stock = data_row[2]

            event.widget.tk_focusNext().focus()

            self.prev_price.set(price)

            self.stock_spin.set(stock)

            my_cursor.close()
            conn.close()

            return("break")

        except:

            event.widget.tk_focusNext().focus()

            return("break")

    def product_add_btn(self, event, entryField):

        if self.a_name.get() not in self.item_names:

            self.product_add()

            root.after(1, lambda: entryField.focus_set())

            return("break")

        else:
            messagebox.showerror("Warning", "Product already exists.")

    def product_add_return(self, event, entryField):

        if self.a_name.get() not in self.item_names:

            self.product_add()

            root.after(1, lambda: entryField.focus_set())

            return("break")

        else:
            messagebox.showerror("Warning", "Product already exists.")

    def product_add(self):

        conn = sqlite3.connect('ims.db')

        name = str(self.a_name.get())
        stock = float(self.a_stock.get())
        price = float(self.a_price.get())

        name = name.lower()

        try:

            my_cursor = conn.execute(
                "INSERT INTO product VALUES(?,?,?,?)", (name, stock, price, price))

            conn.commit()

            my_cursor = conn.execute(
                "SELECT rowid,* FROM product WHERE name=?", (name,))
            data_row = my_cursor.fetchone()

            self.a_tree.insert('', 'end', text=data_row[0], values=(
                data_row[1], data_row[2], data_row[3])),

            self.item_names.append(data_row[1])

            my_cursor.close()
            conn.close()

            # Clearing boxes
            self.stock_spin.set('1')
            self.a_name.delete(0, 'end')
            self.a_price.delete(0, 'end')

        except sqlite3.Error as my_err:
            print("error: ", my_err)

    def product_update_btn(self, event, entryField):

        if self.a_name.get() in self.item_names:

            self.product_update()

            root.after(1, lambda: entryField.focus_set())

            return("break")

        else:
            messagebox.showerror(
                "Warning", "Product doesn't exists.\nPlease 'ADD' the product.")

    def product_update_return(self, event, entryField):

        if self.a_name.get() in self.item_names:

            self.product_update()

            root.after(1, lambda: entryField.focus_set())

            return("break")

        else:
            messagebox.showerror(
                "Warning", "Product doesn't exists.\nPlease 'ADD' the product.")

    def product_update(self):

        conn = sqlite3.connect('ims.db')

        name = str(self.a_name.get())
        stock = float(self.a_stock.get())
        price = float(self.a_price.get())

        name = name.lower()

        every_item = self.a_tree.get_children()

        try:

            my_cursor = conn.execute(
                "UPDATE product SET name=?, stock=?, price=?, retail=? WHERE name=?", (name, stock, price, price, name))

            conn.commit()

            my_cursor = conn.execute(
                "SELECT rowid,* FROM product WHERE name=?", (name,))
            data_row = my_cursor.fetchone()

            my_cursor.close()
            conn.close()

            tree_items = []
            ids = []

            # getting names in tree view
            for i in self.a_tree.get_children():
                tree_items.append(self.a_tree.item(i)['values'][0])

            # Updating the considered item
            for i in range(len(tree_items)):
                if name != "" and name == tree_items[i][:len(name)]:
                    selections = tree_items[i]
                    indx = tree_items.index(selections)

            selected = every_item[indx]

            self.a_tree.item(selected, text=data_row[0], values=(
                data_row[1], data_row[2], data_row[3])),

            # Clearing boxes

            self.stock_spin.set('1')
            self.a_name.delete(0, 'end')
            self.a_price.delete(0, 'end')

        except sqlite3.Error as my_err:
            print("error: ", my_err)

    def product_delete(self):

        # selected item
        items = self.a_tree.selection()

        naam = self.a_tree.item(self.a_tree.selection())['values'][0]
        print(naam)

        conn = sqlite3.connect('ims.db')

        my_cursor = conn.execute("DELETE FROM product WHERE name=?", (naam,))

        conn.commit()

        self.a_tree.delete(items)

        # Show items after deleting

        my_cursor = conn.execute("SELECT rowid,* FROM product")
        items = my_cursor.fetchall()

        self.item_names = []

        print('Items after deletion:-')

        for item in items:
            self.item_names.append(item[1])
            print(item)

        my_cursor.close()
        conn.close()

    def a_selecting(self, event):
        name = self.a_tree.item(self.a_tree.selection())['values'][0]
        stock = self.a_tree.item(self.a_tree.selection())['values'][1]
        price = self.a_tree.item(self.a_tree.selection())['values'][2]

        self.add_name.set(name)
        self.stock_spin.set(stock)
        self.prev_price.set(price)

# Add Product Functions End
#
#
# Returns Product Functions

    def r_selecting(self, event):
        name = self.r_table.item(self.r_table.selection())['values'][0]
        qty = self.r_table.item(self.r_table.selection())['values'][1]
        disc = self.r_table.item(self.r_table.selection())['values'][2]
        price = self.r_table.item(self.r_table.selection())['values'][3]

        self.prod_name.set(name)
        self.prod_qty_spin.set(qty)
        self.prod_disc_spin.set(disc)
        self.prod_price.set(price)

    def r_update_show(self, event):

        name = self.r_table.item(self.r_table.selection())['values'][0]

        print(name)

        conn = sqlite3.connect('ims.db')
        my_cursor = conn.execute(
            "SELECT rowid,* FROM product WHERE name=?", (name,))
        data_row = my_cursor.fetchone()

        prod_price = data_row[3]

        get_add_disc = int(float(self.r_disc_box.get()))

        disc_price = (get_add_disc / 100) * prod_price

        price = prod_price - disc_price

        self.prod_price.set(price)

        my_cursor.close()
        conn.close()

        event.widget.tk_focusNext().focus()

        return('break')


# # # Return Slip Printing Commented & can be Uncommented when needed...
#
#
    # def r_printing(self, event):

    #     conn = sqlite3.connect('ims.db')
    #     c = conn.cursor()

    #     tree_items = []

    #     for i in self.r_table.get_children():
    #         tree_items.append(self.r_table.item(i)['values'])

    #         item = self.r_table.item(i)['values'][0]
    #         quty = int(float(self.r_table.item(i)['values'][1]))
    #         discnt = float(self.r_table.item(i)['values'][2])
    #         prices = float(self.r_table.item(i)['values'][3])
    #         total_prices = float(self.r_table.item(i)['values'][4])

    #     print(tree_items)

    #     for i, item in enumerate(tree_items):
    #         item.insert(0, i+1)

    #     print(tree_items)

    #     c.close()
    #     conn.close()

    #     grand_total = self.grand_total

    #     bill_ids = self.bill_id_box.get()

    #     new_invoice.print_invoice(bill_ids, tree_items, grand_total)

    #     # Clearing boxes
    #     self.qty_spin.set('1')
    #     self.p_cbox.delete(0, 'end')
    #     self.p_str.set("")
    #     self.disc_p_str.set("")
    #     self.add_disc_spin.set('0')
    #     self.sub.set("")
    #     self.balance.set("")
    #     self.grand.set("")
    #     self.pay_box.set("")

    #     # tree view remove all
    #     for row in self.r_table.get_children():
    #         self.p_table.delete(row)

    def r_update_test(self, event, entryField):
        self.r_update()

        root.after(1, lambda: entryField.focus_set())

        return("break")

    def r_update(self):

        selected = self.r_table.focus()

        name = str(self.r_table.item(self.r_table.selection())['values'][0])

        stock = int(float(self.r_table.item(
            self.r_table.selection())['values'][1]))

        bill_ids = int(self.bill_id_box.get())
        print(bill_ids, type(bill_ids))

        conn = sqlite3.connect('ims.db')

        my_cursor = conn.execute(
            "SELECT rowid,* FROM product WHERE name=?", (name,))
        data_row = my_cursor.fetchone()

        st = data_row[2]

        prod_price = data_row[3]

        disc_prcnt = float(self.r_disc_box.get())

        disc_price = (disc_prcnt / 100) * prod_price

        d_prod_price = prod_price - disc_price

        print("discounted price: ", d_prod_price, type(d_prod_price))

        prod_qty = int(self.r_qty_box.get())

        t_price = d_prod_price * prod_qty

        print("total price: ", t_price, type(t_price))

        # stmt = """UPDATE items SET qty = :qty, discount = :discount, price = :price, total_price = :total_price WHERE bill_id = :bill_id and item_name = :item_name"""

        my_cursor = conn.execute("""UPDATE items SET qty = :qty, discount = :discount, price = :price, total_price = :total_price WHERE bill_id = :bill_id and item_name = :item_name""", dict(
            qty=prod_qty, discount=disc_prcnt, price=d_prod_price, total_price=t_price, bill_id=bill_ids, item_name=name))

        conn.commit()

        if stock > prod_qty:
            stk = stock - prod_qty
            qty = st + stk
            my_cursor = conn.execute(
                "UPDATE product SET stock = ? WHERE name = ?", (qty, name))
            conn.commit()

        elif stock < prod_qty:
            stk = prod_qty - stock
            qty = st - stk

            if qty < 0:
                messagebox.showerror("Warning", "Out of Stock!")
            else:
                my_cursor = conn.execute(
                    "UPDATE product SET stock = ? WHERE name = ?", (qty, name))
                conn.commit()

        elif stock == prod_qty:
            pass

        self.r_table.item(selected, text="", values=(
            name, prod_qty, disc_prcnt, d_prod_price, t_price))

        my_cursor.close()
        conn.close()

        # For Grand Total calculation
        self.g_total = 0
        for i in self.r_table.get_children():
            total_prices = float(self.r_table.item(i)['values'][4])
            self.g_total += total_prices
            print(self.g_total)

        self.r_grand.set(self.g_total)

        # Clearing Boxes
        self.prod_name.set("")
        self.prod_qty_spin.set("")
        self.prod_disc_spin.set("")
        self.prod_price.set("")

    def searching_return(self, event, entryField):

        self.searching()

        root.after(1, lambda: entryField.focus_set())

        return("break")

    def searching(self):
        # tree view remove all
        for row in self.r_table.get_children():
            self.r_table.delete(row)

        conn = sqlite3.connect('ims.db')

        bill_id = int(self.bill_id_box.get())

        if self.bill_id_box.get() == "":
            messagebox.showerror("Warning", "Enter Bill ID!")

        else:
            my_cursor = conn.execute(
                "SELECT * FROM items WHERE bill_id=?", (bill_id,))
            items = my_cursor.fetchall()

            count = 1
            self.g_total = 0
            for item in items:
                self.g_total += item[4]
                self.r_table.insert('', 'end', text=count,
                                    values=(item[0], item[1], item[2], item[3], item[4])),
                count += 1
                print(self.g_total)

            self.r_grand.set(self.g_total)

            my_cursor.close()
            conn.close()

    def r_deleting(self):
        bill_ids = int(self.bill_id_box.get())

        # selected item
        items = self.r_table.selection()

        # getting name of a product in tree view
        name = self.r_table.item(self.r_table.selection())['values'][0]

        # getting qty of a product in tree view
        qty = self.r_table.item(self.r_table.selection())['values'][1]
        qty = float(qty)

        # getting total price in tree view
        prod_total = self.r_table.item(self.r_table.selection())['values'][4]
        prod_total = float(prod_total)

        self.g_total = self.g_total - prod_total
        self.r_grand.set(self.g_total)

        conn = sqlite3.connect('ims.db')

        # Updating in product table
        my_cursor = conn.execute(
            "SELECT rowid,* FROM product WHERE name=?", (name,))
        data_row = my_cursor.fetchone()

        print(data_row[2])

        st = data_row[2] + qty

        my_cursor = conn.execute(
            "UPDATE product SET stock = ? WHERE name = ?", (st, name))
        conn.commit()

        # Deleting from items table
        my_cursor = conn.execute("DELETE FROM items WHERE bill_id = :bill_ids and item_name= :item",
                                 dict(bill_ids=bill_ids, item=name))
        conn.commit()

        # print(data_row[1])
        print("Added Stock: ", st)

        my_cursor.close()
        conn.close()

        self.r_table.delete(items)

# Returns Product Functions End
#
#


# The following code is added to facilitate the Scrolled widgets you specified.


class AutoScroll(object):
    '''Configure the scrollbars for a widget.'''

    def __init__(self, master):
        #  Rozen. Added the try-except clauses so that this class
        #  could be used for scrolled entry widget for which vertical
        #  scrolling is not supported. 5/7/14.
        try:
            vsb = ttk.Scrollbar(master, orient='vertical', command=self.yview)
        except:
            pass
        hsb = ttk.Scrollbar(master, orient='horizontal', command=self.xview)
        try:
            self.configure(yscrollcommand=self._autoscroll(vsb))
        except:
            pass
        self.configure(xscrollcommand=self._autoscroll(hsb))
        self.grid(column=0, row=0, sticky='nsew')
        try:
            vsb.grid(column=1, row=0, sticky='ns')
        except:
            pass
        hsb.grid(column=0, row=1, sticky='ew')
        master.grid_columnconfigure(0, weight=1)
        master.grid_rowconfigure(0, weight=1)
        # Copy geometry methods of master  (taken from ScrolledText.py)
        if py3:
            methods = tk.Pack.__dict__.keys() | tk.Grid.__dict__.keys() \
                | tk.Place.__dict__.keys()
        else:
            methods = tk.Pack.__dict__.keys() + tk.Grid.__dict__.keys() \
                + tk.Place.__dict__.keys()
        for meth in methods:
            if meth[0] != '_' and meth not in ('config', 'configure'):
                setattr(self, meth, getattr(master, meth))

    @staticmethod
    def _autoscroll(sbar):
        '''Hide and show scrollbar as needed.'''
        def wrapped(first, last):
            first, last = float(first), float(last)
            if first <= 0 and last >= 1:
                sbar.grid_remove()
            else:
                sbar.grid()
            sbar.set(first, last)
        return wrapped

    def __str__(self):
        return str(self.master)


def _create_container(func):
    '''Creates a ttk Frame with a given master, and use this new frame to
    place the scrollbars and the widget.'''
    def wrapped(cls, master, **kw):
        container = ttk.Frame(master)
        container.bind('<Enter>', lambda e: _bound_to_mousewheel(e, container))
        container.bind(
            '<Leave>', lambda e: _unbound_to_mousewheel(e, container))
        return func(cls, container, **kw)
    return wrapped


class ScrolledTreeView(AutoScroll, ttk.Treeview):
    '''A standard ttk Treeview widget with scrollbars that will
    automatically show/hide as needed.'''
    @_create_container
    def __init__(self, master, **kw):
        ttk.Treeview.__init__(self, master, **kw)
        AutoScroll.__init__(self, master)


def _bound_to_mousewheel(event, widget):
    child = widget.winfo_children()[0]
    if platform.system() == 'Windows' or platform.system() == 'Darwin':
        child.bind_all('<MouseWheel>', lambda e: _on_mousewheel(e, child))
        child.bind_all('<Shift-MouseWheel>',
                       lambda e: _on_shiftmouse(e, child))
    else:
        child.bind_all('<Button-4>', lambda e: _on_mousewheel(e, child))
        child.bind_all('<Button-5>', lambda e: _on_mousewheel(e, child))
        child.bind_all('<Shift-Button-4>', lambda e: _on_shiftmouse(e, child))
        child.bind_all('<Shift-Button-5>', lambda e: _on_shiftmouse(e, child))


def _unbound_to_mousewheel(event, widget):
    if platform.system() == 'Windows' or platform.system() == 'Darwin':
        widget.unbind_all('<MouseWheel>')
        widget.unbind_all('<Shift-MouseWheel>')
    else:
        widget.unbind_all('<Button-4>')
        widget.unbind_all('<Button-5>')
        widget.unbind_all('<Shift-Button-4>')
        widget.unbind_all('<Shift-Button-5>')


def _on_mousewheel(event, widget):
    if platform.system() == 'Windows':
        widget.yview_scroll(-1*int(event.delta/120), 'units')
    elif platform.system() == 'Darwin':
        widget.yview_scroll(-1*int(event.delta), 'units')
    else:
        if event.num == 4:
            widget.yview_scroll(-1, 'units')
        elif event.num == 5:
            widget.yview_scroll(1, 'units')


def _on_shiftmouse(event, widget):
    if platform.system() == 'Windows':
        widget.xview_scroll(-1*int(event.delta/120), 'units')
    elif platform.system() == 'Darwin':
        widget.xview_scroll(-1*int(event.delta), 'units')
    else:
        if event.num == 4:
            widget.xview_scroll(-1, 'units')
        elif event.num == 5:
            widget.xview_scroll(1, 'units')


if __name__ == '__main__':
    vp_start_gui()
