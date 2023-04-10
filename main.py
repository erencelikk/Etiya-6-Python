print("Merhaba Etiya")
print ("Hoş Geldiniz")

# yorum

#değişkenler - start
#metinsel, numerik, obje

#string
text = "Merhaba"

print(text)
print(text)
text = "Selam"
print(text)
print(text)
print(text)

studentcount = 45 #int #integer => tam sayı
print(studentcount +5)

averagepoint = 25.5 
print(averagepoint +5)

isverified = True 
print(isverified)

print(type(text))
print(type(studentcount))
print(type(averagepoint))
print(type(isverified))


number= 10

print(number + 10)
print(number - 5)
print(number / 2)
print(number * 5)
print(number % 3)
print(number / 2)


print(number == 10)
print(number != 11)
print(number < 10)
print(number <= 10)

print("***************")

sayilar = [100, 200, 300, 400, 500, "Merhaba", 15.5, True]
print(sayilar)
sayilar.append(100)
sayilar.append(600)
print(sayilar)
sayilar.pop()
print(sayilar)
sayilar.remove("Merhaba")
sayilar.extend([700, 800, 900])


vize = int(input("Vize notunuzu giriniz: "))
final = int(input("Final notunuzu giriniz: "))
ortalama = (vize * 0.4) + (final * 0.6) 

# eğer final 40'dan küçükse kullanıcı kaldı
# eğer ortalama 50'den küçükse kullanıcı kaldı
# eğer vize finalin 2 katı ise kullanıcı kaldı
# bunun dışındaki tüm durumlarda kullanıcı geçti yazdırmak istiyoruz.

if final < 40:
    print("Failed")
elif ortalama < 50:
    print("Failed")
elif vize == 2*final:
    print("Failed")
else:
    print("Passed")

