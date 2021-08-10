from tkinter import *
from tkinter import messagebox
from xuly_chuoi import *

#Button Them
def Them_action():
    MS=Masach.get()
    TS=Tensach.get()
    NXB=Namxb.get()
    data=MS+";"+TS+";"+NXB
    if MS=="" or TS=="" or NXB=="":
        messagebox.showerror("Chưa đủ thông tin","Không được để trống trường nào hết. ")
    else:
        Luu_file("database.txt",data)
    Show_file()


def Show_file():
    List_sach=Doc_file("database.txt")
    list_box.delete(0,END)
    for i in List_sach:
        list_box.insert(END,i)




root=Tk()
Masach=StringVar()
Tensach=StringVar()
Namxb=StringVar()




root.minsize(height=400,width=400)
root.title("Quản lý sách")
Label(root,text="Quản lý sách",font=("tahoma",16)).grid(row=0,columnspan=2)
list_box=Listbox(root,width=60)
list_box.grid(row=1,columnspan=2)
Show_file()

Label(root,text="Mã sách").grid(row=2,column=0)
Entry(root,width=40,text=Masach).grid(row=2,column=1)

Label(root,text="Tên sách").grid(row=3,column=0)
Entry(root,width=40,text=Tensach).grid(row=3,column=1)

Label(root,text="Năm XB").grid(row=4,column=0)
Entry(root,width=40,text=Namxb).grid(row=4,column=1)

button_frame=Frame()
Button(button_frame,text="Thêm",command=Them_action).pack(side=LEFT)
Button(button_frame,text="Tìm kiếm").pack(side=LEFT)
Button(button_frame,text="Thoát",command=quit).pack(side=LEFT)

button_frame.grid(row=5,columnspan=2)
root.mainloop()