#
#
#
# def LuuFile(path,data):
#     file=open(path,"a",encoding="utf-8")
#     file.writelines(data)
#     file.writelines("\n")
#     file.close()
#
# count=1
# while count>0:
#     s=count
#     print(s)
#     count+=1
#     LuuFile("number.txt",str(count))

s=int(input("Nhap vao so n= "))
chuoi=str(s)
List=[]
for i in range(len(chuoi)):
    print(chuoi[i])
    List.append(chuoi[i])
print(List)

print("So nho nhat la:",min(List))
print("So lon nhat la:",max(List))

