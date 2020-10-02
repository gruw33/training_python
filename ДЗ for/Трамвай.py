ostanovki = int(input())
a1 = 0
b1 = 0
for i in range(ostanovki):
    a, b = map(int,input("Сколько вышло и вошло человек: ").split())
    #b1 = b1 - a
    #b1 = b1 + b
    #if i >= 0:
    if i == 0 and a > 0:
        print("Перед первой остановкой трамвай должен быть пустым!")
        a, b = map(int,input("Сколько вышло и вошло человек: ").split())
    b1 = b1 - a
    b1 = b1 + b
    if b1 > a1:
            a1 = b1
    #if a >= b1:
       # print("Выйти не может больше чем находится в салоне")
       # a, b = map(int,input("Сколько вышло и вошло человек: ").split())
    #c = ostanovki - 1
    #if i == c and b1 > c:
        #print("на последней остановке ни кто не должен входить!")
        #a, b = map(int,input("Сколько вышло и вошло человек: ").split())

#print(b1)    
print(a1)