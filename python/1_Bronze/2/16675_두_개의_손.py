ML, MR, TL, TR = input().split()

#둘다 다를 경우
if ML != MR and TL != TR:
    print("?")
    
#MS만 같을 경우
elif ML == MR and TL != TR:
    if ML == 'S' and (TL == 'R' or TR == 'R'):
        print("TK")
    elif ML == 'P' and (TL == 'S' or TR == 'S'):
        print("TK")
    elif ML == 'R' and (TL == 'P' or TR == 'P'):
        print("TK")
    else:
        print("?")

#TK만 같을 경우
elif ML != MR and TL == TR:
    if TL == 'S' and (ML == 'R' or MR == 'R'):
        print("MS")
    elif TL == 'P' and (ML == 'S' or MR == 'S'):
        print("MS")
    elif TL == 'R' and (ML == 'P' or MR == 'P'):
        print("MS")
    else:
        print("?")

#둘다 같을 경우
else:
    if ML == 'S':
        if TL == 'P':
            print("MS")
        if TL == 'S':
            print("?")
        if TL == 'R':
            print("TK")
    if ML == 'R':
        if TL == 'P':
            print("TK")
        if TL == 'S':
            print("MS")
        if TL == 'R':
            print("?")
    if ML == 'P':
        if TL == 'P':
            print("?")
        if TL == 'S':
            print("TK")
        if TL == 'R':
            print("MS")

# 조건문이 많이 생겼을때 노트로 정리 하던 주석으로 정리하던 일단 정리해서 코드 짜기. 안그러면 다 꼬임 코드가.