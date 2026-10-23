'''B - Fully pair?'''
from ast import literal_eval

alive_roles = {}
while True:
    line = input().strip()
    if line == "Start":
        break
    if not line:
        continue
    alive_roles.update(literal_eval(line))

dead_roles = {}
while True:
    voted_name = input().strip()
    if voted_name == "End":
        break
    if voted_name in alive_roles:
        dead_roles[voted_name] = alive_roles.pop(voted_name)

impostor_remaining = list(alive_roles.values()).count("Impostor")

print(impostor_remaining, "Impostor Remains")

print("***Alive***")
for member_name in sorted(alive_roles):
    print(member_name, ":", alive_roles[member_name])

print("***Dead***")
for member_name in sorted(dead_roles):
    print(member_name, ":", dead_roles[member_name])
