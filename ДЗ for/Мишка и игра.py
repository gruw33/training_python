from random import randint
R = int(input("Введите количество раундов: "))
Micha_vin = 0
Kris_vin = 0 
n = 0
for i in range(R):
    Micha = randint(1,6)
    Kris = randint(1,6)
    if Micha > Kris:
        print("Раунд:",(i+1),"победил в раунде Micha со счетом ", Micha,":", Kris)
        Micha_vin+= 1
    elif Micha < Kris:
        print("Раунд:",(i+1),"победил в раунде Kris со счетом ", Micha,":", Kris)
        Kris_vin+= 1
    elif Micha == Kris:
        print("Раунд:",(i+1),"ничья в раунде со счетом ", Micha,":", Kris)
if Micha_vin > Kris_vin:
    print("Победил Micha со счетом: ", Micha_vin,":", Kris_vin)
elif Micha_vin < Kris_vin:
    print("Победил Kris со счетом: ", Kris_vin,":", Micha_vin)
elif Micha_vin == Kris_vin:
    print("Ничья: ", Micha_vin,":", Kris_vin)


