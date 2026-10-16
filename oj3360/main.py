'''หั่นขนมปัง'''
width, height, _, _ = map(int, input().split())

vertical_cuts = list(map(int, input().split()))
horizontal_cuts = list(map(int, input().split()))

vertical_cuts = [0] + vertical_cuts + [width]
horizontal_cuts = [0] + horizontal_cuts + [height]

piece_areas = []

for cut_index in range(len(vertical_cuts) - 1):
    piece_width = vertical_cuts[cut_index + 1] - vertical_cuts[cut_index]

    for cut_height_index in range(len(horizontal_cuts) - 1):
        piece_height = (
            horizontal_cuts[cut_height_index + 1]
            - horizontal_cuts[cut_height_index]
        )

        piece_area = piece_width * piece_height
        piece_areas.append(piece_area)

piece_areas.sort(reverse=True)

print(piece_areas[0], piece_areas[1])
