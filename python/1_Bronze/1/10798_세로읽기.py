lst = []
for _ in range(5):
    lst.append(list(input()))

s = ""
for i in range(15):
    for j in range(15):
        try:
            s += lst[j][i]
        except :
            continue

print(s)