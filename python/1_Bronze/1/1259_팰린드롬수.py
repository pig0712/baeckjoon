while True:
    n = input()
    if n == "0": break
    g = True

    for i in range(int((len(n) / 2))):
        if n[i] != n[-i-1] : g = False

    if g == True:
        print("yes")
    else:
        print("no")