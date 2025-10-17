# Baekjoon 25166 - 배고픈 아리의 샌드위치 구매
s, m = map(int, input().split())

if 1023 + m < s:
    print("Impossible")

elif s <= 1023:
    print("No thanks")

else:
    need = s - 1023
    print(m,need,m & need)
    print("Thanks" if (m & need) == need else "Impossible")

# 위의 코드는 ChatGPT를 사용 하여서 요약 하였으며 int & int 으로 비트 and 연산 할수 있는걸 첨 알았음 ;;