from tkinter import *
from xuly_data import *
def Them_action():
    MS=Masach.get()
    TS=Tensach.get()
    NXB=Namxb.get()
    data=MS+";"+TS+";"+NXB
    Luu_file("database.txt",data)
    Show_data()


def Show_data():
    List_sach=Doc_file("database.txt")
    List_box.delete(0,END)
    for i in List_sach:
        List_box.insert(END,i)


root=Tk()
Masach=StringVar()
Tensach=StringVar()
Namxb=StringVar()


root.title("Quản lý sách")
root.resizable(height=True,width=True)
root.minsize(height=400,width=400)
Label(root,text="Quản Lý Sách",font=("tahoma",18)).grid(row=0,columnspan=2)

List_box=Listbox(root,width=60)
List_box.grid(row=1,columnspan=2)
Label(root,text="Mã sách").grid(row=2,column=0)
Entry(root,width=45,text=Masach).grid(row=2,column=1)

Label(root,text="Tên sách").grid(row=3,column=0)
Entry(root,width=45,text=Tensach).grid(row=3,column=1)

Label(root,text="Năm XB").grid(row=4,column=0)
Entry(root,width=45,text=Namxb).grid(row=4,column=1)

button_frame=Frame()
Button(button_frame,text="Thêm",command=Them_action).pack(side=LEFT)
Button(button_frame,text="Tên sách").pack(side=LEFT)
Button(button_frame,text="Thoát",command=root.quit).pack(side=LEFT)

button_frame.grid(row=5,columnspan=2)

root.mainloop()