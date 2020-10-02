a = int(input("Введите кол-во опрошенных человек: "))
if a <= 0:
    print("Error")
if a == 1:
    print("Что выдумаете?")
    b = int(input("Введите оценку, где 0 это легко и где 1 это тяжело: "))
    if b < 0 or b >= 2:
        print("Error")
    elif b == 0:
        print("Задача простая")
    elif b == 1:
        print("Задача сложная")
elif a == 2:
    print("Что вы думаете?")
    b,c = map(int,input("Введите оценку, где 0 это легко и где 1 это тяжело: ").split())
    if b < 0 or b >= 2 or c < 0 or c >= 2:
        print("Error")
    elif b == 1 or c == 1:
        print("Задача сложная")
    else:
        print("Задача простая")
elif a == 3:
    print("Что вы думаете?")
    b,c,f = map(int,input("Введите оценку, где 0 это легко и где 1 это тяжело: ").split())
    if b < 0 or b >= 2 or c < 0 or c >= 2 or f < 0 or f >= 2:
        print("Error")
    elif b == 1 or c == 1 or f == 1:
        print("Задача сложная")
    else :
        print("Задача простая")
elif a > 3:
    print("Дружище, давай в другой раз. Я еще не разобрался =(")
