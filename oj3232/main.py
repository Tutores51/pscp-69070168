'''กบน้อยกระโดด'''
X, Y = map(int, input().split())

total = 0
jump = X
count = 0

while jump > 0:
    total += jump
    count += 1

    if total >= Y:
        print(count)
        break

    jump -= 2
else:
    print(-1)
