a = input().replace(" ","")

if a[0] == str(8):
    c = 8
    b = True
    for i in a:
        if i == str(c):
            c -= 1
        elif i != str(c): b = False; print("mixed"); break
    if b == True : print("descending")

elif a[0] == str(1):
    c = 1
    b = True
    for i in a:
        if i == str(c):
            c += 1
        elif i != str(c): b = False; print("mixed"); break
    if b == True : print("ascending")

else : print("mixed")