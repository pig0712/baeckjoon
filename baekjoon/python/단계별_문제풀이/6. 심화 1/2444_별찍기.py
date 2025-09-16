n = int(input())
for i in range(n*2-1):

    if i < n:
        pass
        print(" "*(n-i-1) + "*"*((i+1)*2-1))
    else :
        print(" "*(i-n+1) + "*"*((2*n-i-1)*2-1))