
#Hàm Lưu file
def Luu_file(path,data):
    file=open(path,"a",encoding="utf-8")
    file.writelines(data)
    file.writelines("\n")
    file.close()

#Hàm Đọc file
def Doc_file(path):
    file=open(path,"r",encoding="utf-8")
    List_sach=[]
    for i in file:
        List_nho=i.strip()
        X=List_nho.split(";")
        List_sach.append(X)
    file.close()
    return List_sach

