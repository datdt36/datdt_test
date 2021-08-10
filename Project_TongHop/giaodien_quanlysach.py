from tkinter import *
from xuly_data import *
#Xử lý button Thêm

def Show_sach():
    arrSach=Doc_file("database.txt")
    lsb_sach.delete(0,END)
    for i in arrSach:
        lsb_sach.insert(END,i)

def Them_action():
    data=ma_sach.get()+";"+ten_sach.get()+";"+namxb.get()
    Luu_file("database.txt",data)
    Show_sach()



root = Tk()
#Khai báo input từ Entry:
ma_sach=StringVar()
ten_sach=StringVar()
namxb=StringVar()




root.title("Quản lý sách")
root.resizable(height=True,width=True)
root.minsize(height=400,width=400)
Label(root,text="Quản Lý Sách",font=("tahoma",18)).grid(row=0,columnspan=2)

#Listbox
lsb_sach=Listbox(root,width=65,height=15)
lsb_sach.grid(row=1,columnspan=2)
#Show_sach()

#Mã sách
Label(root,text="Mã sách").grid(row=2,column=0)
Entry(root,width=50,text=ma_sach).grid(row=2,column=1)

#Tên sách
Label(root,text="Tên sách").grid(row=3,column=0)
Entry(root,width=50,text=ten_sach).grid(row=3,column=1)

#Nam xuất bản
Label(root,text="Năm xuất bản").grid(row=4,column=0)
Entry(root,width=50,text=namxb).grid(row=4,column=1)

#Button
Button_frame=Frame()
Button(Button_frame,text="Thêm",command=Them_action).pack(side=LEFT)
Button(Button_frame,text="Tìm").pack(side=LEFT)
Button(Button_frame,text="Sắp xếp").pack(side=LEFT)
Button(Button_frame,text="Thoát",command=root.quit).pack(side=LEFT)
Button_frame.grid(row=5,columnspan=2)

root.mainloop()
