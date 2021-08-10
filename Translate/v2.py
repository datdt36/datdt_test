from  googletrans import Translator
while True:
    translate=Translator()
    nhap=input("Nhập từ muốn dịch: ")
    result=translate.translate(nhap)
    print(result)
    print(result.text)