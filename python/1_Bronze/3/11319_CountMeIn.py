n = int(input())

for i in range(n):
    s = input().replace(" ","")
    a = 0
    for j in ["A","E","I","O","U","a","e","i","o","u"]:
        a += s.count(j)
        
    print(len(s)-a,a)
    