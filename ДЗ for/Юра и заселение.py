##Юра и Леша хотят жить в одной комнате. Всего в общежитии есть n комнат. В данный момент в комнате с номером i живут pi человек, когда всего в этой комнате может жить qi человек (pi ≤ qi). Посчитайте, сколько комнат общежития смогут вместить Юру и Лешу вместе?
K = int(input())
friends = 2
approach = 0
for i in range(K):
    a, b = map(int,input().split())
    places = b - a
    if places >= friends:
        approach+= 1
print(approach)
