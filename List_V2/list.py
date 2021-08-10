import random
n=int(input("nhập vào số phần tự mong muốn: "))
List=[]
for i in range(n):
    pt=random.randrange(1,10)
    List.append(pt)
print(List)