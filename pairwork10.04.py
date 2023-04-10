def fibonacciLister ():
    x = 1 
    y = 1
    list = [x,y]

    for i in range(25):
        z=x+y
        x=y
        y=z
        list.append(z)
     
    print(list)

fibonacciLister ()



def perfectNumber ():
    sayi= int(input("Bir sayı giriniz: "))
    toplam = 0
    for i in range(1,sayi):
        if sayi % i == 0:
            toplam += i 
    if toplam == sayi:
        print("Mükemmel sayı")
    else:
        print("Mükemmel sayı değildir")        

perfectNumber ()

def hesapMakinesi ():
    
    sayi1 = int(input("bir sayi giriniz:"))
    sayi2 = int(input("bir sayi giriniz:"))
    islem = input("işlem seçiniz:")

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


hesapMakinesi ()


def ortHesabi ():
    vize = float(input("vize notunu giriniz:"))
    final = float(input("final notunu giriniz:"))
    ortalama = (vize*0.4) + (final*0.6)

    if ortalama >= 0 and ortalama < 50:
        print(f'FF, notunuz:{ortalama}')
    elif ortalama >= 50 and ortalama < 60:
        print(f'DD, notunuz:{ortalama}')
    elif ortalama >= 60 and ortalama < 70:
        print(f'CC, notunuz:{ortalama}')
    elif ortalama >= 70 and ortalama < 80:
        print(f'BB, notunuz:{ortalama}')
    elif ortalama >=80 and ortalama <= 100:
        print(f'AA, notunuz:{ortalama}')


ortHesabi ()

