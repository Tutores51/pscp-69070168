ra = int(input())
rb = int(input())
String = input("a" or "b")
ea = 1/ (1 + (10**((rb - ra)/400)))
eb = 1/ (1 + (10**((ra - rb)/400)))
if String == "a":
    print(f"{ea:.2f}")
else:
    print(f"{eb:.2f}")