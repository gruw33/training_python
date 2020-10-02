a = int(input())
while a <= 0:
    print("error")
b = a%10
if b == 1:
    print(b ,"korova")
elif b >= 2 and b <= 4:
    print(b ,"korovy")
elif b >=5:
    print(b ,"korov")