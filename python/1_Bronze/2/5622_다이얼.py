s = input()
n = 0

for i in s:

    if (i in ["A","B","C"]):
        n += 3
    elif (i in ["D","E","F"]):
        n += 4
    elif (i in ["G","H","I"]):
        n += 5
    elif (i in ["J","K","L"]):
        n += 6
    elif (i in ["M","N","O"]):
        n += 7
    elif (i in ["P","Q","R","S"]):
        n += 8
    elif (i in ["T","U","V"]):
        n += 9
    elif (i in ["W","X","Y","Z"]):
        n += 10

print(n)