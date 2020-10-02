a = int(input())
b = int(input())
c = int(input())
if a == b and b == c:
    print ("3")
elif a > b:
    if b == c:
        print("2")
    elif b > c:
        print("0")
    elif b < c:
        print("0")
elif a < b:
    if b == c:
        print("2")
    elif b > c:
        print("0")
    elif b < c:
        print("0")
