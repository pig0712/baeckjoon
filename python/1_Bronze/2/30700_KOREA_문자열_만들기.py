s = input()
f = "KOREA"
a = 0
c = 0
for i in s:
    if i == f[a]: c+=1; a+=1
    if a >= 5: a = 0
print(c)