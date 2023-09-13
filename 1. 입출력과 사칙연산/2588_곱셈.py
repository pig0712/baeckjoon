a = int(input())
b = int(input())
c = str(b)
for i in range(3):
    print("%s"%(int(c[i])*a))
print("%s"%(a*b))

# a,b = map(int,input().split("\n"))
# print("%d\n%d\n%d\n%d"%(a*(b % 10),a*((b // 10) % 10),a*((b // 100)),a*b))