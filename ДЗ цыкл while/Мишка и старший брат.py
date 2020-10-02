Li,Bob = map(int,input("Вес Лимака и Боба: ").split())
g = 0
while Li <= Bob:
    g+=1
    Li*=3
    Bob*=2
print (g)
