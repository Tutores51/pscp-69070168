'''BigFrame'''
texts = []

for _ in range(5):
    texts.append(input())

longest_length = max(len(text) for text in texts)

print("*" * (longest_length + 4))

for text in texts:
    spaces = longest_length - len(text)
    print("* " + text + " " * spaces + " *")

print("*" * (longest_length + 4))
