A1, P1 = list(map(int,input().split()))
R2, P2 = list(map(int,input().split()))

if A1 / P1 > ((R2**2) * 3.14159265358) / P2:
    print("Slice of pizza")
else:
    print("Whole pizza")