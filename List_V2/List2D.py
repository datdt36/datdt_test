import random

row=int(input("nhập vào số dòng: "))
column=int(input("nhập vào số cột: "))
List2D=[]
for i in range(row):
    List=[]
    for j in range(column):
        pt=random.randrange(1,10)
        List.append(pt)
    List2D.append(List)
print(List2D)

for i in range(len(List2D)):
    for j in range(len(List2D[i])):
        print(List2D[i][j],end="\t")
    print()