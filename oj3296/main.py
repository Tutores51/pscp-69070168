'''RGB Mixed'''
red1, green1, blue1 = map(int, input().split())
red2, green2, blue2 = map(int, input().split())

red = (red1 + red2) // 2
green = (green1 + green2) // 2
blue = (blue1 + blue2) // 2

print(red, green, blue)
