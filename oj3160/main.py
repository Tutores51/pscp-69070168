'''หาจำนวนเฉพาะ'''
start_number, end_number = map(int, input().split())

total_primes = 0
prime_text = ""

for number in range(start_number, end_number + 1):
    if number < 2:
        continue

    prime = True

    for divisor in range(2, number):
        if not number % divisor:
            prime = False
            break

    if prime:
        if prime_text:
            prime_text += " "
        prime_text += str(number)
        total_primes += 1

if total_primes > 0:
    print(prime_text)

print("Total primes:", total_primes)
