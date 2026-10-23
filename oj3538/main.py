'''B - Fully pair?'''

letters = input()

unpaired_letters = ""

for letter in letters:
    if letter not in unpaired_letters:
        if letters.count(letter) % 2 == 1:
            unpaired_letters += letter

if unpaired_letters:
    print(unpaired_letters)
else:
    print("fully paired")
