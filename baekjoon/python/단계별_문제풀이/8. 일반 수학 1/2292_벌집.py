x = int(input())
distance, max_value = 1, 1

while True:
    if x <= max_value:
        print(distance)
        break

    distance += 1
    max_value += 3*((distance-1)*2)