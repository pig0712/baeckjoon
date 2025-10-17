a = int(input())
b = max(1,a - (len(str(a)) * 9))

if not (a > b) : print(0)

while a > b:
    c = b
    for i in str(b):
        c += int(i)
    if c == a: print(b); break
    if (a == b+1) and (c != a) : print(0)
    b += 1