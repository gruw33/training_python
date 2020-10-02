n = int(input())
a = 0
b = str("0")
for i in range(n):
    m = int(input())    
    if b != m:
        a+= 1        
    b = m
print(a)


