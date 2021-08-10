from tkinter import *
#Hàm xử lý button Tiếp:
def Tiep_action():
    a.set("")
    b.set("")
    kq.set("")

#Hàm sử lý button Giải:
def Giai_action():
    aNumber=float(a.get())
    bNumber=float(b.get())
    if aNumber==0 and bNumber==0:
        kq.set("Phương trình vô số nghiệm")
    elif aNumber==0 and bNumber!=0:
        kq.set("Phương trình vô nghiệm")
    else:
        kq.set(-(bNumber/aNumber))


root = Tk()

a=StringVar()
b=StringVar()
kq=StringVar()



root.title("Giải Phương trình bậc nhất")
root.resizable(height=True,width=True)
root.minsize(height=200,width=250)

Label(root,text="Phương trình bậc 1",font=("tahoma",16),justify=CENTER).grid(row=0,columnspan=2)
#Hệ số a:
Label(root,text="Hệ số a").grid(row=1,column=0)
Entry(root,width=30,text=a).grid(row=1,column=1)

#Hệ số b:
Label(root,text="Hệ số b").grid(row=2,column=0)
Entry(root,width=30,text=b).grid(row=2,column=1)

#Button
frameButton=Frame()
Button(frameButton,text="Giải",command=Giai_action).pack(side=LEFT)
Button(frameButton,text="Tiếp",command=Tiep_action).pack(side=LEFT)
Button(frameButton,text="Thoát",command=quit).pack(side=LEFT)
frameButton.grid(row=3,columnspan=2)

#Kết quả.
Label(root,text="Kết quả").grid(row=4,column=0)
Entry(root,width=30,text=kq).grid(row=4,column=1)


root.mainloop()
