#Ghi file:
def Luu_file(path,data):
    file=open(path,"a",encoding="utf-8")
    file.writelines(data)
    file.writelines("\n")


#Doc file:
def Doc_file(path):
    file=open(path,"r",encoding="utf-8")
    Arr_sach=[]
    for i in file:
        pt=i.strip()
        X=pt.split(";")
        Arr_sach.append(X)
    return Arr_sach