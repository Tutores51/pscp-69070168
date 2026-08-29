'''Arcade of Time: Store Check'''
num, check = map(int, input().split())

time = [0] * 1441

for _ in range(num):
    start, stop = map(int, input().split())
    time[start] += 1
    time[stop] -= 1

for i in range(1, 1441):
    time[i] += time[i - 1]

checks = list(map(int, input().split()))

answer = []

for i in range(check):
    answer.append(str(time[checks[i]]))

print(" ".join(answer))
