a = [input() for _ in range(20)]

# P 인 과목 삭제
lst = []
for i in range(20):
    if a[i][-1] != "P":
        lst.append(a[i])

# 학점, 등급 나누기
credit = []
rating = []
for i in lst:
    s = list(i.split(" "))
    credit.append(s[1])
    rating.append(s[2])

# 학점을 실수형으로 변환
credit = list(map(float,credit))

f_rat = []
# 등급 점수로 변환 (실수형)
for i in range(len(rating)):
    if rating[i] == "A+":
        f_rat.append(4.5)
    elif rating[i] == "A0":
        f_rat.append(4.0)
    elif rating[i] == "B+":
        f_rat.append(3.5)
    elif rating[i] == "B0":
        f_rat.append(3.0)
    elif rating[i] == "C+":
        f_rat.append(2.5)
    elif rating[i] == "C0":
        f_rat.append(2.0)
    elif rating[i] == "D+":
        f_rat.append(1.5)
    elif rating[i] == "D0":
        f_rat.append(1.0)
    elif rating[i] == "F":
        f_rat.append(0.0)


# 계산
ss = 0
for i in range(len(credit)):
    ss += credit[i]*f_rat[i]

print(round(ss / sum(credit),6))