'''isPrime_large'''
number = int(input())

if number < 2:
    is_prime = False
elif number == 2:
    is_prime = True
elif not number % 2:
    is_prime = False
else:
    is_prime = True
    divisor = 3
    limit = int(number ** 0.5)
    while divisor <= limit:
        if not number % divisor:
            is_prime = False
            break
        divisor += 2

if is_prime:
    print("YES")
else:
    print("NO")
