a = int(input())
for _ in range(a):
    p = int(input())
    n = 1

    if p == 1:
        print(1)
    else:
        for i in range(2,p+1):
            n_1 = n
            n = i**2 + n_1

        print(n)