

a = int(input("Сколько у Вани кубиков: "))
y = 0
y1 = 0
s = 0
while s<a:
    y+=1
    y1+=y
    s+=y1
if s == a:
    print(y)
else:
    print(y-1)
    


