'''temperature'''
temperature = float(input())
unit = input()
changeto = input()

if unit == "C":
    c = temperature
elif unit == "F":
    c = (temperature - 32) * 5 / 9
elif unit == "K":
    c = temperature - 273.15
else:
    c = temperature * 5 / 9 - 273.15

if changeto == "C":
    newtemp = c
elif changeto == "F":
    newtemp = c * 9 / 5 + 32
elif changeto == "K":
    newtemp = c + 273.15
else:
    newtemp = (c + 273.15) * 9 / 5

print(f"{newtemp:.2f}")
