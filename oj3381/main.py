'''Point Sorting'''
test_case_count = int(input())

for _ in range(test_case_count):
    point_count = int(input())
    points = []

    for _ in range(point_count):
        x_coordinate, y_coordinate = map(int, input().split())
        points.append([x_coordinate, y_coordinate])

    for first_index in range(point_count):
        for second_index in range(first_index + 1, point_count):
            first_x = points[first_index][0]
            first_y = points[first_index][1]

            second_x = points[second_index][0]
            second_y = points[second_index][1]

            first_function_value = first_x + first_y
            second_function_value = second_x + second_y

            need_swap = False

            if first_function_value > second_function_value:
                need_swap = True
            elif (first_function_value == second_function_value
                  and first_y < second_y):
                need_swap = True

            if need_swap:
                points[first_index], points[second_index] = (
                    points[second_index],
                    points[first_index]
                )

    for point in points:
        print(point[0], point[1])
