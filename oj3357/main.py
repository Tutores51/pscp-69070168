'''giraffe'''
giraffe_count = int(input())

giraffe_heights = []

for _ in range(giraffe_count):
    height = int(input())
    giraffe_heights.append(height)

full_giraffe_count = 0

if giraffe_count == 1:
    full_giraffe_count = 1
else:
    if giraffe_heights[0] > giraffe_heights[1]:
        full_giraffe_count += 1

    for index in range(1, giraffe_count - 1):
        left_height = giraffe_heights[index - 1]
        current_height = giraffe_heights[index]
        right_height = giraffe_heights[index + 1]

        if current_height > left_height and current_height > right_height:
            full_giraffe_count += 1

    if giraffe_heights[-1] > giraffe_heights[-2]:
        full_giraffe_count += 1

print(full_giraffe_count)
