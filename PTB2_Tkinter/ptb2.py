from cmath import sqrt
from tkinter import *

#Hàm cho button Tiếp
def Tiep_action():
    a.set("")
    b.set("")
    c.set("")
    kq.set("")

#Hàm cho button Giải
def Giai_action():
    A=float(a.get())
    B=float(b.get())
    C=float(c.get())
    if A==0 and B==0 and C==0:
        kq.set("Phương trình vô nghiệm")
    elif A==0 and B==0 and C!=0:
        kq.set("Phương trình vô nghiệm")
    elif A==0 and B!=0:
        kq.set("x="+str(-C/B))
    else:
        denta=(B*B) - (4*A*C)
        if denta==0:
            kq.set("Nghiệm kép="+str(-B/2*A))
        elif denta<0:
            kq.set("Phương trình vô nghiệm")
        else:
            x1=(-B+sqrt(denta))/(2*A)
            x2=(-B-sqrt(denta))/(2*A)
            kq.set("x1="+str(x1)+" ; "+"x2="+str(x2))



root = Tk()

#Gán biến:
a=StringVar()
b=StringVar()
c=StringVar()
kq=StringVar()



root.title("Phương trình bậc 2")
root.resizable(height=True,width=True)
root.minsize(height=200,width=300)
Label(root,text="ax2+bx+c=0",font=("tahoma",16)).grid(row=0,columnspan=2)

#Hệ số a.
Label(root,text="Hệ số a").grid(row=1,column=0)
Entry(root,width=30,text=a).grid(row=1,column=1)

#Hệ số b.
Label(root,text="Hệ số b").grid(row=2,column=0)
Entry(root,width=30,text=b).grid(row=2,column=1)

#Hệ số c.
Label(root,text="Hệ số c").grid(row=3,column=0)
Entry(root,width=30,text=c).grid(row=3,column=1)

#Button
frameButtbon=Frame()
Button(frameButtbon,text="Giải",command=Giai_action).pack(side=LEFT)
Button(frameButtbon,text="Tiếp",command=Tiep_action).pack(side=LEFT)
Button(frameButtbon,text="Thoát",command=root.quit).pack(side=LEFT)
frameButtbon.grid(row=4,columnspan=2)

#Kết quả
Label(root,text="Kết quả").grid(row=5,column=0)
Entry(root,width=30,text=kq).grid(row=5,column=1)


root.mainloop()
