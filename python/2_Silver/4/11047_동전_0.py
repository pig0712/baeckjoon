n,m = map(int,input().split())

coins = []

for _ in range(n):
    coins.append(int(input()))

coins = list(reversed(coins))

c = 0
for i in coins:
    if m//i > 0 : c += m//i ; m = m % i
    if m <= 0: break
print(c)
