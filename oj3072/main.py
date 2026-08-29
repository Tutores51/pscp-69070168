'''A-E-I-O-U'''
text = input()

vowels = ['a', 'e', 'i', 'o', 'u']
count = [0, 0, 0, 0, 0]

for ch in text.lower():
    if ch in vowels:
        index = vowels.index(ch)
        count[index] += 1

for i in range(5):
    if count[i] > 0:
        print(vowels[i], ":", count[i])
