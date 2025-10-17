n = int(input())

for _ in range(n):
    a = input()
    
    while a.find("()") != -1:

        a = a.replace("()","")

    if a == "": print("YES")
    else: print("NO")