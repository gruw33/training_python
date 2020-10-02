##Вычисление сколько лет необходимо ждать что бы накопить определённую сумму с определенной ставкой
x = int(input())
p = int(input())
y = int(input())
g = 0
while x < y:
    g+=1
    x = x + x * p / 100
    x = round(x)
print(g)



