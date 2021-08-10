from tkinter.tix import *
from xulytaptin import *


#Xử lý button Thêm
def Them_action():
    data=ma_sach.get()+";"+ten_sach.get()+";"+namxb.get()
    Luu_file("database.txt",data)
    Show_list_sach()

def Show_list_sach():
    arrsach=Doc_file("database.txt")
    for i in arrsach:
        list_box.delete(0,END)
        list_box.insert(END,i)


root = Tk()

#Khai báo input.
ma_sach=StringVar()
ten_sach=StringVar()
namxb=StringVar()

root.title("Thư Viện Sách")
root.resizable(width=True,height=True)
root.minsize(width=400,height=400)
Label(root,text="Quản lý Sách",font=("tahoma",16)).grid(row=0,columnspan=2)

#Listbox
list_box=Listbox(root,width=60)
list_box.grid(row=1,columnspan=2)

#Mã sách
Label(root,text="Mã sách").grid(row=2,column=0)
Entry(root,width=50,text=ma_sach).grid(row=2,column=1)

#Tên sách
Label(root,text="Tên sách").grid(row=3,column=0)
Entry(root,width=50,text=ten_sach).grid(row=3,column=1)

#Năm XB
Label(root,text="Năm XB").grid(row=4,column=0)
Entry(root,width=50,text=namxb).grid(row=4,column=1)

#Button
button_frame=Frame()
Button(button_frame,text="Thêm",command=Them_action).pack(side=LEFT)
Button(button_frame,text="Tìm kiếm").pack(side=LEFT)
Button(button_frame,text="Sắp xếp").pack(side=LEFT)
Button(button_frame,text="Thoát",command=root.quit).pack(side=LEFT)
button_frame.grid(row=6,columnspan=2)


root.mainloop()
