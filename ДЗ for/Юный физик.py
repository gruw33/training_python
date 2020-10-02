#Напишите программу, которая определяет по заданным векторам сил, покоится тело или движется.
n = int(input())
a1 = 0
b1 = 0
c1 = 0
for i in range(n):
    a, b, c = map(int,input().split())
    a1+= a
    b1+= b
    c1+= c
if a1 == 0 and b1 == 0 and c1 == 0:
    print("YES")
else:
    print("NO")