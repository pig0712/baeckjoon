lst = [
    "Never gonna give you up",
    "Never gonna let you down",
    "Never gonna run around and desert you",
    "Never gonna make you cry",
    "Never gonna say goodbye",
    "Never gonna tell a lie and hurt you",
    "Never gonna stop"
]

n = int(input())
a = False
for i in range(n):
    s = input().lstrip().rstrip()
    if s not in lst:
        a = True
        print("Yes")
        break

if a == False:
    print("No")