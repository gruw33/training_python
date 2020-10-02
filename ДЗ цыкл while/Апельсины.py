a, b = map(int,input().split())
d = 0
while b > 0:
    c = a%b
    a = b
    b = c
print(a)

while a != b:
    if a > b:
        a = a-b
    else :
        b = b-a
    
    d += 1
print(d)
