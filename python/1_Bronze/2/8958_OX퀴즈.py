n = int(input())

for i in range(n):
    r,s,c = input(),0,0

    for i in r:
        if i == "O":
            c += 1
            s += c
        elif i == "X":
            c = 0

    print(s)