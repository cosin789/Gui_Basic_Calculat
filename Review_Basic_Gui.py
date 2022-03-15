from tkinter import *
from tkinter import ttk
import csv
from datetime import datetime
from tkinter.ttk import Notebook

Gui = Tk()
Gui.title("โปรแกรมคำนวณ")
Gui.geometry('350x600+50+50')
Gui.config(bg = 'lightgrey')
n = Notebook(Gui)

Frame1 = Frame(Gui)
Frame1.grid()
Frame2 = Frame(Gui)
Frame2.grid()


icon_fr1 = PhotoImage(file = 'Finance-Wallet-icon.png')
icon_fr2 = PhotoImage(file = 'Bulleted-List-icon.png')
main_icon_fr1 = PhotoImage(file = 'City-Market-Square-icon.png')
#------------------------------------------------#
n.add(Frame1,text = f'{"คำนวณราคา" : ^{30}}',image = icon_fr1,compound = 'top')
n.add(Frame2,text = "คำนวณราคา",image = icon_fr2,compound = 'top')
#n.pack()
n.pack(fill = BOTH)
#------------------------------------------------#
Dict_Days = {'Mon' : 'จันทร์',
 'Tue' : 'อังคาร',
 'Wed' : 'พุธ',
 'Thu' : 'พฤหัสบดี',
 'Fri' : 'ศุกร์',
 'Sat' : 'เสาร์',
 'Sun' : 'อาทิตย์'}
Date = datetime.now()
#--------------Define Botton when pressed---------------#
def Bottonpressed():
    Get_expance = v_expanse.get()
    Get_price = v_price.get()
    Get_piece = v_piece.get()
    Todays = datetime.now().strftime('%a')
    Dt = datetime.now().strftime(f'%Y-%m-%d-{Dict_Days[Todays]}')
#------------Rule-----------------------------#
    if Get_expance == '':
        print('กรุณากรอกข้อมูลให้ครบ')
        return
    elif Get_price == '':
        return
    elif Get_piece == '':
        Get_piece == 1
    try:
        Total = int(Get_piece)*int(Get_price)
        print(f'{Get_expance},{Get_price},{Get_piece},{Total}')
        print(Dt)
    except Exception as e:
        print('ERROR')
        print(e)
#------------save file to csv---------------------#
    with open('savedata_4.csv','a', encoding = 'utf-8',newline = '') as f:
        fw = csv.writer(f)
        data = [Get_expance,Get_price,Get_piece,Total]
        fw.writerow(data)
#------------show file to tree table---------------------#
    def update_table():
        resulttable.delete(*resulttable.get_children())
        data = read_csv() #get_children = รหัสพิเศษ *resuluttable เหมือนรัน forloop
        for i in data:
            resulttable.insert('','end',value = i) #ลองเปลี่ยน end เป็น 0 or 1
    print(data)

    update_table()
#------------read file csv---------------------#
try:
    def read_csv():
        with open('savedata_4.csv',newline='', encoding='utf') as f: #ให้เปิดไฟล์ CSV3 ขึ้นมาเเล้วตั้งชื่อว่า f
            file_reader = csv.reader(f) #reader file : f
            data = list(file_reader)
        return data # รีเทิร์นค่าไปยัง read_csv ใช้ข้างนอก
        return read_csv()
    read_csv()  

except Exception as e1:
    print(e1)


#---------------Make a tree table-------------------------------#


header =['รายการ', 'ราคา', 'จำนวน', 'รวม']
resulttable = ttk.Treeview(Frame2, columns = header, show = 'headings', height = 10)
resulttable.pack()

for i in range(len(header)):
    resulttable.heading(header[i],text = header[i])
headerwidth = [50,60,60,70]
for h,w in zip(header, headerwidth):
    resulttable.column(h,width = w)

L0 = ttk.Label(Frame2,text = 'ตารางคำนวณ')
L0.pack()

#------------------------------------------------#
Label1 = Label(Frame1, text = 'สินค้า')
Label1.grid(row = 0, column = 1, columnspan = 3, padx = 5, pady = 5)

v_expanse = StringVar()

Entry1 = Entry(Frame1, textvariable = v_expanse)
Entry1.grid(row = 0, column = 6, columnspan = 3, padx = 5, pady = 5)

#------------------------------------------------#
Label2 = Label(Frame1, text = 'ราคา')
Label2.grid(row = 1, column = 1, columnspan = 3, padx = 5, pady = 5)

v_price = StringVar()
v_price.set('')

Entry2 = Entry(Frame1, textvariable = v_price)
Entry2.grid(row = 1, column = 6, columnspan = 3, padx = 5, pady = 5)

Label1_2 = Label(Frame1, text = 'บาท')
Label1_2.grid(row = 1, column = 9, columnspan = 3, padx = 5, pady = 5)
#------------------------------------------------#
Label3 = Label(Frame1, text = 'จำนวน')
Label3.grid(row = 2, column = 1, columnspan = 3, padx = 5, pady = 5)

v_piece = StringVar()
v_piece.set('')

Entry3 = Entry(Frame1, textvariable = v_piece)
Entry3.grid(row = 2, column = 6, columnspan = 3, padx = 5, pady = 5)

Label1_3 = Label(Frame1, text = 'ชิ้น')
Label1_3.grid(row = 2, column = 9, columnspan = 3, padx = 5, pady = 5)
#------------------------------------------------#
Button1 = ttk.Button(Frame1, text = 'รวม', command = Bottonpressed,cursor = 'hand1')
Button1.grid(row = 3, column = 9)
#------------------------------------------------#

#------------------------------------------------#

Gui.mainloop() 