"""Personal ID card"""
id_card = input()
n = 0
for _ in id_card:
    n += 1
if n == 13:
    print("yes")
else:
    print("no")
