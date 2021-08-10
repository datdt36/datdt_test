#Luu File:
def Luu_file(path,data):
    file=open(path,"a",encoding="utf-8")
    file.writelines(data)
    file.writelines("\n")
    file.close()


#Doc file:
def Doc_file(path):
    file=open(path,"r",encoding="utf-8")
    ArrSach=[]
    for i in file:
        pt=i.strip()
        X=pt.split(";")
        ArrSach.append(X)
    return ArrSach

