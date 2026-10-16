'''Shorten'''
numbers = []

while True:
    number = int(input())

    if number == -1:
        break

    numbers.append(number)

if len(numbers) > 0:
    result = []

    start = numbers[0]
    end = numbers[0]

    for number in numbers[1:]:
        if number == end + 1:
            end = number
        else:
            if start == end:
                result.append(str(start))
            else:
                result.append(str(start) + "-" + str(end))

            start = number
            end = number

    if start == end:
        result.append(str(start))
    else:
        result.append(str(start) + "-" + str(end))

    print(", ".join(result))
