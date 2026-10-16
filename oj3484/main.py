'''หุ่นยนต์เคาะเสียงกระเบื้อง'''
size, fine_per_point = input().split()
size = int(size)
fine_per_point = float(fine_per_point)

floor = []
for _ in range(size):
    floor.append(list(map(int, input().split())))

bad_tiles_in_column = [0] * size
bad_points_in_column = [0] * size
total_bad_tiles = 0
total_bad_points = 0

for row in range(size):
    bad_tiles_in_row = 0
    bad_points_in_row = 0

    for col in range(size):
        bad_points = floor[row][col]

        if bad_points > 0:
            bad_tiles_in_row += 1
            bad_tiles_in_column[col] += 1

        bad_points_in_row += bad_points
        bad_points_in_column[col] += bad_points

    total_bad_tiles += bad_tiles_in_row
    total_bad_points += bad_points_in_row

    print(*floor[row], bad_tiles_in_row, bad_points_in_row)

print(*bad_tiles_in_column)
print(*bad_points_in_column)

total_fine = total_bad_points * fine_per_point
print(total_bad_tiles, total_bad_points, f"{total_fine:.2f}")
