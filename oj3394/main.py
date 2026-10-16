'''ส่งต่อ'''
student_count, start_student = map(int, input().split())

forward_to = []

for _ in range(student_count):
    next_student = int(input())
    forward_to.append(next_student)

visited_students = []

current_student = start_student

while current_student:
    if current_student in visited_students:
        break

    visited_students.append(current_student)

    next_student = forward_to[current_student - 1]
    current_student = next_student

print(len(visited_students))
