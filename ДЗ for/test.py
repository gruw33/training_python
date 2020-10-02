n=int(input())
x=0
f=[]
for i in range(n):
    a,b=map(int,input().split())
    x=x-a
    x=x+b
    f.append(x)
f.sort()
f.reverse() 
print(f[0])