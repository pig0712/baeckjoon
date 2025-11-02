a = input()
if "(" in a:
    a,b = a.split(" (")
    print(a)
    print(b[:-1])
else:
    print(a)
    print("-")