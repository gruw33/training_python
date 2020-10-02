##Программа ищет сочетание букв "рок" в словах количество которых указывается в начале.
n = int(input())
for i in range(n):
    s = input().lower()
    if "рок" in s:
        print(i+1, s, s.find("рок")+1)
        

