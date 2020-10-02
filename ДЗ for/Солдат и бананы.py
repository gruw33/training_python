#Солдат хочет купить w бананов в магазине. Ему надо заплатить k долларов за первый банан, 2k долларов — за второй и так далее (иными словами, за i-й банан надо заплатить i·k долларов).

#У него есть n долларов. Сколько долларов ему придется одолжить у однополчанина, чтобы купить w бананов?
price, money, pieces = map(int,input().split())
following = 0
for i in range(1,pieces+1):
    following = price*i
    money-= following
if money <= 0:
    print(abs(money))
else:
    print("0")
