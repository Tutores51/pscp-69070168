'''CuteCat CuteFox'''
def get_number(animal_id):
    '''...'''
    return int(animal_id[3:])


n = int(input())

herd = {}
for _ in range(n):
    line = input().strip().strip("{}")
    name, number = line.split(":")
    name = name.strip().strip('"')
    number = number.strip().strip('"')
    herd[number] = name

used_names = herd.values()

if "Cat01" not in herd and "Garfield" not in used_names:
    herd["Cat01"] = "Garfield"
if "Fox01" not in herd and "Fubuki" not in used_names:
    herd["Fox01"] = "Fubuki"

cat_numbers = []
fox_numbers = []
for number in herd:
    if number.startswith("Cat"):
        cat_numbers.append(number)
    else:
        fox_numbers.append(number)

cat_numbers.sort(key=get_number)
fox_numbers.sort(key=get_number)

print("Cat :", len(cat_numbers))
print("Fox :", len(fox_numbers))

for number in cat_numbers:
    print(herd[number], ":", number)
for number in fox_numbers:
    print(herd[number], ":", number)
