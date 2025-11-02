n = int(input())
x,s = list(map(int,input().split()))
weapons = []
for _ in range(n):
    weapons.append(list(map(int,input().split())))

weapons.sort()

save = -9999

for i in range(len(weapons)):
    if weapons[i][0] > x: break
    if weapons[i][1] >= save: save = weapons[i][1]

if s < save :
    print("YES")
else: print("NO")
