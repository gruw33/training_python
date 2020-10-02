##Сколько можно собрать пар мальчиков и девочек с умениями не больше +- 1
boys = int(input("Введите количество мальчиков: "))
skills_boys = list(map(int,input().split()))
girls = int(input("Введите количество девочек: "))
skills_girls = list(map(int,input().split()))

skills_boys.sort()
skills_girls.sort()

i =0
j =0
couple = 0
while i < boys and j < girls:
    if abs(skills_boys[i] - skills_girls[j]) <=1:
        couple += 1
        i += 1
        j += 1
    elif skills_boys[i] < skills_girls[j]:
        i += 1
    else:
        j += 1
print("Получилось пар: ", couple)












