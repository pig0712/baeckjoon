def list_e_type(a):
    b = [None for _ in range(3)]
    for i,j in enumerate(a):
        b[i] = str(type(j))
    return(b)

from sys import stdin
input = stdin.readline

numbers = [None for _ in range(3)]

for i in range(3):
    inp = input()
    try:
        numbers[i] = int(inp)
    except:
        numbers[i] = inp

trans = list_e_type(numbers)

for i,j in enumerate(trans):
    if j == "<class 'int'>":
        if i == 0:
            result = int(numbers[0])+3
            break
        elif i == 1:
            result = int(numbers[1])+2
            break
        else:
            result = int(numbers[2])+1
            break



print(f"{result}"*((result%3!=0) & (result%5!=0))+"Fizz"*(result%3==0)+"Buzz"*(result%5==0))


# 다른사람의 최단시간 풀이

for i in range(3, 0, -1):
    x = input()
    if x not in ['Fizz', 'Buzz', 'FizzBuzz']: # 난 이걸 왜 타입 변환까지 했을까. 
        n = int(x) + i
        print('Fizz'*(n % 3 == 0) + 'Buzz'*(n % 5 == 0) or n)
        break