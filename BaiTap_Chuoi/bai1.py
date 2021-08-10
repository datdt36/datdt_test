s="5;2;4;-4;11;-12;7;9;14"
#1. In ra từng phần tử, mỗi phần tử 1 dòng.
s2=s.split(";")
print(s2)

s_chan=""
s_am=""
sum=0
for i in range(len(s2)):
    print(s2[i])
    if float(s2[i])%2==0:
        s_chan=s_chan+s2[i]+","

    if float(s2[i])<0:
        s_am=s_am+s2[i]+","

    sum=sum+float(s2[i])
    tbc=sum/len(s2)

print("Trung bình cộng của dãy số là:",round(tbc,2))

daysochan=s_chan.strip(",")
print("Dãy số chẵn là: ",daysochan.split(","))
print("Lượng số chẵn là:",len(daysochan.split(",")))

daysoam=s_am.strip(",")
print("Dãy số âm là:",daysoam.split(","))
print("Lượng số âm là:",len(daysoam.split(",")))




#2. In ra List số lẻ và đếm xem có bao nhiêu số lẻ.
#3. In ra List số âm.
#4. Tính trung bình cộng của dãy số trên.
