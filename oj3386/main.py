'''Duplicate I'''
first_group_count = int(input())
second_group_count = int(input())

first_group_ids = []

for _ in range(first_group_count):
    student_id = int(input())
    first_group_ids.append(student_id)

second_group_ids = []

for _ in range(second_group_count):
    student_id = int(input())
    second_group_ids.append(student_id)

duplicate_ids = []

for student_id in first_group_ids:
    if student_id in second_group_ids:
        duplicate_ids.append(student_id)

if not duplicate_ids:
    print("Nope")
else:
    duplicate_ids.sort(reverse=True)

    for student_id in duplicate_ids:
        print(student_id)
