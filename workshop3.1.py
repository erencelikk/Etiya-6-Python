x = 1 
y = 1
list = [x,y]

for i in range(25):
    z=x+y
    x=y
    y=z
    list.append(z)
     
print(list)

