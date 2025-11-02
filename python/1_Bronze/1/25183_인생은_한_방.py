_ = input()
s = input()
s = " "+s+" "
# 65 = A, 90 = Z

c = 1
for i in range(1,len(s)-1):
    if (ord(s[i]) == 65) and (ord(s[i+1]) == 66): c+=1
    elif (ord(s[i]) == 90) and (ord(s[i+1]) == 89) : c+=1
    elif (ord(s[i]) == ord(s[i+1])+1) or (ord(s[i]) == ord(s[i+1])-1): c+=1
    else : c=1

    if c >= 5: break
if c == 5: print("YES")
else: print("NO")