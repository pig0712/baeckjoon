def fac(a):
    if a <= 1:
        return 1
    return fac(a-1) * a


n,k = list(map(int,input().split()))
print(int(fac(n) / (fac(n-k)*fac(k))))
