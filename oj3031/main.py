'''ink'''
import math

s, n = map(int, input().split())

for n in range(n):
    x, y = map(int, input().split())

    area = 3.1416 * (x * x + y * y)
    time = math.ceil(area / s)

    print(time)
