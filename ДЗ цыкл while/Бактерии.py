a = int(input("Желаемое количество бактерий: "))
summa_v_korobke = 1
day = 0
while summa_v_korobke < a:
    prihod = summa_v_korobke + 1
    summa_v_korobke = summa_v_korobke * 2
    day+=1
print(day)
