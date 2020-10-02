a = int(input())
c = []
y = 360
for i in range(a):
    b = int(input())
    x = y/b*b
    if x != y:
        c+= "YES".split()
    else:
        c+= "NO".split()
print (c)