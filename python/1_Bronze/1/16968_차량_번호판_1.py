a = input()
d = 1

for i in range(len(a)):
    if (i > 0) and (a[i-1] == a[i]) : 
        if a[i] == "c":
            d *= 25
        else:
            d *= 9

    else :
        if a[i] == "c":
            d *= 26
        else:
            d *= 10

print(d)