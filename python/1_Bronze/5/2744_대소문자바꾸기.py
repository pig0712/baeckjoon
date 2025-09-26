s = list(input())
a = ""
for i in range(len(s)):
    if s[i].isupper():
        s[i] = s[i].lower()

    else:
        s[i] = s[i].upper()
    a += s[i]
print(a)