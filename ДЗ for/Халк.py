n = int(input())
a = [" I hate"," it"," that I love"," that"]
b = []
for i in range(n):
    if n == 1:
        b = a[0]+a[1]
    elif n == 2:
        b = []
        b = a[0]+a[2]+a[1]
    elif n == 3:
        b = []
        b = a[0]+a[2]+a[3]+a[0]+a[1]
print(b)

#не полное решение