n = int(input())
a = 2
b = sum(map(int,list(str(bin(n))[2:])))
for i in range(3,n+1):
    if b < (n // i) + (n % i): b = (n // i) + (n % i); a = i
print(b,a)