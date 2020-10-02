a = int(input("Введите номер автобусного билета: "))
a1 = a//100000%10
a2 = a//10000%10
a3 = a//1000%10
a4 = a//100%10
a5 = a//10%10
a6 = a//1%10
if a1+a2+a3==a4+a5+a6:
    print("Yes")
else:
    print("No")

#b = a1+a2+a3
#b1 = a4+a5+a6
#if b==b1:
#    print("Yes")
#else:
#    print("No")

