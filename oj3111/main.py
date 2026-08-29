'''สหกรณ์โรงเรียน'''
import math

member = input().upper()
n = int(input())

total = 0

for _ in range(n):
    total += float(input())

if member == "Y":
    total *= 0.95
elif member == "N" and total >= 500:
    total *= 0.97

total = math.floor(total * 100 + 0.500000001) / 100

print(f"{total:.2f}")
