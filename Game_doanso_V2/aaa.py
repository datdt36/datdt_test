import random
i=0
while True:
    songuoi=int(input("Nhập vào số của bạn: "))
    somay=random.randrange(1,6)

    print("Số của bạn là: ",songuoi)
    print("Số của máy là: ",somay)

    if songuoi!=somay:
        print("Bạn đoán sai rồi")
    else:
        print("Bạn đoán đúng rồi. Bạn giỏi quá")
        hoi=input("Bạn có muốn chơi tiếp không?")
        if hoi!="yes":
            break
        else:
            i=-1

    if i==2:
        hoi2=input("Bạn đoán đủ 3 lần rồi, muốn chơi lại từ đầu hay nghỉ đây?")
        if hoi2!="yes":
            break
        else:
            i=-1
    i+=1
#    print(i)