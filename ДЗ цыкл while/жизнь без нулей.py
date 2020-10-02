a = int(input("Введите 3х значное число: "))
b = int(input("Введите 3х значное число: "))
while a <= 0 or b <= 0:
    print("Число не должно начинаться с нуля")
    a = int(input("Введите 3х значное число: "))
    b = int(input("Введите 3х значное число: "))
c = a+b
nomer = [a,b,c]
i = 0
while i < 3:
    chislo = nomer[i]
    razryd = 1
    new_nomer = 0
    while chislo > 0:
        last = chislo % 10
        if last != 0:
            new_nomer = last * razryd + new_nomer
            razryd*= 10
        chislo//= 10
    nomer[i] = new_nomer  
    i+= 1
if nomer[0] + nomer[1] == nomer[3]:
    print("YES")
else:
    print("NO")