numberlist = []

for i in range(10):
    number = int(input("Lütfen on adet sayı giriniz:"))
    numberlist.append(number)

print(numberlist)

smallestNumber = min(numberlist)
biggestNumber = max(numberlist)

print(f'Girilen En Küçük Değer: {smallestNumber}')
print(f'Girilen En Büyük Değer: {biggestNumber}')

for evenNumber in range(0, biggestNumber, 2):
     print(evenNumber)

upNumber = int(input("Alt limit giriniz: "))
number2 = int(input("Alt limit belirlemek için 1 giriniz"))

if number2 == 1:
     for i in range(upNumber, biggestNumber, 2):
          print(i)
else:
     print("Geçersiz bir giriş yapıldı.")

