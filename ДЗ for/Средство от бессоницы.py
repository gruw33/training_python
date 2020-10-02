k = int(input())
l = int(input())
m = int(input())
n = int(input())
d = int(input())
big = [k,l,m,n,d]
q = 0
for i in range(max(big)):
    if i%k == 0 or i%l == 0 or i%m == 0 or i%n == 0 or i%d == 0:
        q += 1
print(q)