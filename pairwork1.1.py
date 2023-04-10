sayi1 = int(input("bir sayi giriniz:"))
sayi2 = int(input("bir sayi giriniz:"))
islem = input("işlem seçiniz:")

"""if islem == "+":
    toplam = sayi1+sayi2
elif islem == "-":
    toplam = sayi1 - sayi2
    
elif islem == "*":
    toplam = sayi1 * sayi2
elif islem == "/":
    toplam = sayi1 / sayi2
else:
    toplam = print("yanlış işlem seçtiniz")

print(toplam)"""


toplam = sayi1 + sayi2
cikarma = sayi1 - sayi2
carpma = sayi1 * sayi2
bolme = sayi1 / sayi2

if islem == "+":
    print(toplam)
elif islem == "-":
    print(cikarma)
elif islem == "*":
    print(carpma)
elif islem == "/":
    print(bolme)
else :
    print("hatalı işlem seçimi")
    
