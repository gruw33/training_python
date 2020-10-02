a, b = map(int,input().split())
proizvedenie = a*b
while a != b:
    if a > b:
        a = a-b
    else :
        b = b-a
if a > b:
    a = proizvedenie/a
    print("НОК", round(a))
else:
    b = proizvedenie/b
    print("НОК", round(b))