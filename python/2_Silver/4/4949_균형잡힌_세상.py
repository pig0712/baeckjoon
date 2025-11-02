import sys

txt = sys.stdin.read().split("\n")


filter = []
for i in txt:
    if i == ".": break
    a = ""
    for j in i:
        if (j == "[") or (j == "]") or (j == "(") or (j == ")"):
            a += j
    filter.append(a)

result = []
for i in filter:
    for j in range(100):
        i = str(i).replace("()","")
        i = str(i).replace("[]","")
    result.append(i)

for i in result:
    if i == "": print("yes")
    else: print("no")