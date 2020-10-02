a, b = map(int,input().split())
while a != b:
    if a > b:
        a = a-b
    else :
        b = b-a
if a > b:
    print("НОД", a)
else:
    print("НОД", b)

