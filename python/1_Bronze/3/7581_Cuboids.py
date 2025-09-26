while True:
    a = list(map(int,input().split()))
    if a == [0,0,0,0]: break

    if a[0] == 0:
        a[0] = a[3] / (a[1] * a[2])
        print(int(a[0]),a[1],a[2],a[3])
    elif a[1] == 0:
        a[1] = a[3] / (a[0] * a[2])
        print(a[0],int(a[1]),a[2],a[3])
    elif a[2] == 0:
        a[2] = a[3] / (a[1] * a[0])
        print(a[0],a[1],int(a[2]),a[3])
    else:
        a[3] = a[0] * a[1] * a[2]
        print(a[0],a[1],a[2],int(a[3]))