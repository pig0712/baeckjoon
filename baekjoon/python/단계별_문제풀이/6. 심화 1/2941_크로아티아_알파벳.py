a = input()

re = ["c=","c-","dz=","d-","lj","nj","s=","z="]

for i in re:
    a = a.replace(i,"1")

print(len(a))