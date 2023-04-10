
sayi= int(input("Bir sayı giriniz: "))
toplam = 0
for i in range(1,sayi):
    if sayi % i == 0:
        toplam += i 
if toplam == sayi:
    print("Mükemmel sayı")
else:
    print("Mükemmel sayı değildir")        
