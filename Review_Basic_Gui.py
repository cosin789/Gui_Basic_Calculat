from tkinter import *
from tkinter import ttk

Gui = Tk()
Gui.title("โปรแกรมคำนวณ")
Gui.geometry('350x600+50+50')
Gui.config(bg = 'lightgrey')

Frame1 = Frame(Gui)
Frame1.grid()

#------------------------------------------------#
Label1 = Label(Frame1, text = 'สินค้า')
Label1.grid(row = 0, column = 1, columnspan = 3, padx = 5, pady = 5)

Entry1 = Entry(Frame1,bg = 'lightblue')
Entry1.grid(row = 0, column = 6, columnspan = 3, padx = 5, pady = 5)


#------------------------------------------------#
Label2 = Label(Frame1, text = 'ราคา')
Label2.grid(row = 1, column = 1, columnspan = 3, padx = 5, pady = 5)

Entry2 = Entry(Frame1,bg = 'lightblue')
Entry2.grid(row = 1, column = 6, columnspan = 3, padx = 5, pady = 5)

Label1_2 = Label(Frame1, text = 'บาท')
Label1_2.grid(row = 1, column = 9, columnspan = 3, padx = 5, pady = 5)
#------------------------------------------------#
Label3 = Label(Frame1, text = 'จำนวน')
Label3.grid(row = 2, column = 1, columnspan = 3, padx = 5, pady = 5)

Entry3 = Entry(Frame1,bg = 'lightblue')
Entry3.grid(row = 2, column = 6, columnspan = 3, padx = 5, pady = 5)

Label1_3 = Label(Frame1, text = 'ชิ้น')
Label1_3.grid(row = 2, column = 9, columnspan = 3, padx = 5, pady = 5)
#------------------------------------------------#
Button1 = Button(Frame1, text = 'รวม')
Button1.grid(row = 3, column = 9)
#------------------------------------------------#

#------------------------------------------------#

Gui.mainloop() 