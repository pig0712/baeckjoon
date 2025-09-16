n,x = input().split()
c = list(map(int,input().split(" ")))

d = []
for i in c:
  if i < int(x):
    d.append(i)

for i in range(len(d)):
  print(d[i],end=" ")