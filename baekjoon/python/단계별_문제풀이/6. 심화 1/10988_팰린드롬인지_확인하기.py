a = input()


if len(a) % 2 == 0:
    if(a[:int(len(a)/2)] == a[:int(len(a)/2)-1:-1]):
        print(1)
    else:
        print(0)

else:
    if(a[:int(len(a)/2)] == a[:int(len(a)/2):-1]):
        print(1)
    else:
        print(0)