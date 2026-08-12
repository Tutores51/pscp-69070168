'''ปราสาท'''
def solve(n):
    r = 1

    while r * r < n:
        r += 1

    pos = n - (r - 1) ** 2

    if pos % 2 == 1:
        return 2 * r - 2
    else:
        return 2 * r - 3


n = int(input())
print(solve(n))
