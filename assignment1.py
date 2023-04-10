baslik = "HABERİNİZ OLSUN"
vade = 12
faizOrani1 = 1.47 
faizOrani2 = 1.44

print(baslik)
print(type(baslik))
print(type(vade))
print(type(faizOrani1))
print(type(faizOrani2))

mesaj = "Hoş Geldin"
musteriAdi = "Engin"
musteriSoyadi = "Demiroğ"
sonucMesaj = mesaj + musteriAdi + musteriSoyadi

print(sonucMesaj)

sayi1 = 10
sayi2 = 10
print(sayi1+sayi2)


dolarDun = 7.65
dolarBugun = 7.75

if dolarDun > dolarBugun:
    print("Azalış oku")
elif dolarBugun < dolarBugun:
    print("Artış oku")
else:
    print("Eşittir oku")

print("Bitti")



krediler = ["Hızlı Kredi", "Maaşını Halkbank'tan alanlara özel", "Mutlu emekli ihtiyaç kredisi"]
print(krediler)
print(krediler[[0]])
print(krediler[[1]])
print(krediler[[2]])
print(len(krediler))
krediler[[0]] = "Çabuk kredi"
print(krediler)


for kredi in krediler:
    print(kredi)
for i in range(10):
    print(i)

for i in range(3,10):
    print(i)

for i in range(0.10,2):
    print(i)

for i in range(len(krediler)):
    print(krediler[i])


def kredileriListele():
    krediler = ["Hızlı Kredi", "Maaşını Halkbank'tan alanlara özel", "Mutlu emekli ihtiyaç kredisi"]
    for kredi in krediler:
        print("<option>" + kredi + "<option>")
