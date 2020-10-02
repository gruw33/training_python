house_1,house_2,house_3 = map(int,input("Введите координаты домов: ").split())
while house_1 < 0 or house_2 < 0 or house_3 < 0:
    print("Введены неправельные координаты")
    house_1,house_2,house_3 = map(int,input("Введите координаты домов: ").split())
if house_1 == house_2 and house_2 == house_3:
    print("Друзья живут вместе, идти не надо!!!")

elif house_2 > house_1 and house_1 > house_3:
    way = (house_2-house_1) + (house_3-house_1)
    print("Суммарное растояние до дома 1 = ", way)

elif house_1 > house_2 and house_2 > house_3:
    way = (house_1-house_2) + (house_2-house_3)
    print("Суммарное растояние до дома 2 = ", way)

elif house_1 > house_3 and house_3 > house_2:
    way = (house_1-house_3) + (house_3-house_2)
    print("Суммарное растояние до дома 3 = ", way)