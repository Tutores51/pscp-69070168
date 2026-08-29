'''จำนวนในช่วง [A,B]'''
A = int(input())
B = int(input())
d = int(input())
r = int(input())

answer = (B - r) // d - (A - 1 - r) // d

print(answer)
