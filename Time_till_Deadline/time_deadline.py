import datetime
print("Nhập mục tiêu của bạn: \n")
nhap=input()
list=nhap.split(":")
print(list)
muctieu=list[0]
deadline=list[1]
print(muctieu)
print(deadline)
homnay=datetime.date.today()
print(homnay)