stroki = int(input())
text_new = []
for i in range(stroki):
    text = input().lower()
    if "соль" in text:
        continue
    else:
        text_new.append(text)
print(", ".join(text_new))
