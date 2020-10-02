x = int(input("Сколько Вы пробежажли в первый день: "))
y = int(input("Ваша цель (км): "))
c = 1
while y > x:
    x = x + x * 0.1
    c += 1

print (c)

