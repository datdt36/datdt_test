from tkinter import *
#Hàm xử lý button Tiếp
def Tiep_action():
    a.set("")
    b.set("")
    kq.set("")


#Ham su xy button Giai
def Giai_action():
    a_Num=float(a.get())
    b_Num=float(b.get())
    if a_Num==0 and b_Num==0:
        kq.set("Phương trình vô số nghiệm")
    elif a_Num==0 and b_Num!=0:
        kq.set("Phương trình vô nghiệm")
    else:
        kq.set(-(b_Num/a_Num))


root = Tk()

a=StringVar()
b=StringVar()
kq=StringVar()

root.title("GPT bậc nhất")
root.resizable(height=True,width=True)
root.minsize(height=200,width=250)
Label(root,text="Phương trình bậc nhất",font=("tahoma",16)).grid(row=0,columnspan=2)

#Hệ số a.
Label(root,text="Hệ số a").grid(row=1,column=0)
Entry(root,width=30,text=a).grid(row=1,column=1)

#Hệ số b.
Label(root,text="Hệ số b").grid(row=2,column=0)
Entry(root,width=30,text=b).grid(row=2,column=1)

#Button
frame_Button=Frame()
Button(frame_Button,text="Giải",command=Giai_action).pack(side=LEFT)
Button(frame_Button,text="Tiếp",command=Tiep_action).pack(side=LEFT)
Button(frame_Button,text="Thoát",command=root.quit).pack(side=LEFT)
frame_Button.grid(row=3,columnspan=2)

#Kết quả.
Label(root,text="Kết quả").grid(row=5,column=0)
Entry(root,width=30,text=kq).grid(row=5,column=1)

root.mainloop()
