a = input()

lst = list(a.upper())

count = {}
for i in lst:
    try: count[i] += 1
    except : count[i] = 1

mx = max(count.values())

c = []
d = []
for i, j in count.items():
    if j == mx:
        c.append(i)
        d.append(i)

if len(c) == 1:
    print(d[0])
else:
    print("?")