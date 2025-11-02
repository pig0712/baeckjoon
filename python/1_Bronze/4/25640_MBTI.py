mbit = ["INFP", "ENFP", "ISFP", "ESFP", "INTP", "ENTP", "ISTP", "ESTP", "INFJ", "ENFJ", "ISFJ", "ESFJ", "INTJ", "ENTJ", "ISTJ", "ESTJ"]
dic = {mbit[i] : 0 for i in range(16)}
my_mbit = input()

for _ in range(int(input())):
    dic[input()] +=1

print(dic[my_mbit])