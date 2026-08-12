'''หาร10ลงตัว'''
n = int(input())

for n in range(n, -1, -1):
    if not n % 10:
        print(n,end=" ")
