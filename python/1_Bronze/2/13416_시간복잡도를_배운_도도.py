b = -1
for _ in range(int(input())):
    a = input()

    a = a.replace("for","for ")
    a = a.replace("while","while ")

    if b < a.count(" "): b = a.count(" ")

print(b)