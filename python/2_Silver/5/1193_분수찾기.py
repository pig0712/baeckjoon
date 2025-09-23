def find_fraction(X):
    an = 0
    n = 1
    s = 0
    while an < X :
        s = an
        an = an + n
        n = n + 1
    n = n - 1
    
    if n % 2 == 1: # 홀
        a,b = n,1
        for i in range(X - s - 1):
            a = a - 1
            b = b + 1

    if n % 2 == 0: # 짝
        a,b = 1,n
        for i in range(X - s - 1):
            a = a + 1
            b = b - 1


    return a, b

X = int(input())
print("%d/%d"%(find_fraction(X)))