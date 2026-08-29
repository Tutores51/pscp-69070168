'''BrickBridge'''
small_brick = int(input())
big_brick = int(input())
goal = int(input())

big = min(big_brick, goal // 5)
remaining = goal - big * 5

if remaining <= small_brick:
    print(remaining)
else:
    print(-1)
