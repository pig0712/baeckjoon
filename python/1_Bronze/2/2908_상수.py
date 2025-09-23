s = input()

a,b = map(int,s.split())

a1, b1 = "",""

for i in range(len(str(a))):
    a1 += str(a%10)
    a = int(a/10)

for i in range(len(str(b))):
    b1 += str(b%10)
    b = int(b/10)

print(a1*(a1>b1)+b1*(a1<b1))