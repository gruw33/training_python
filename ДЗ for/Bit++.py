stroki = int(input())
pribavlenie = 0
vichitanie = 0
for i in range(stroki):
    i = input().lower()
    if "++" in i:
        pribavlenie+= 1
    else:
        vichitanie-= 1
rezultat = pribavlenie + vichitanie
print (rezultat)

