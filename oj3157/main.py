'''เกมสะสมแต้ม'''
n = int(input())
count = 0
for _ in range(n):
    want = input()
    if want == "+":
        count += 10
    elif want == "-":
        count -= 5
print(count)
