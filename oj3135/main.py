'''ของขวัญและขโมย'''
number_of_people, step_size, thief_number = map(int, input().split())

current_person = 1
checked_people = 0

while True:
    checked_people += 1

    if current_person == thief_number:
        break

    next_person = (current_person - 1 + step_size) % number_of_people + 1

    if next_person == 1:
        break

    current_person = next_person

print(checked_people)
