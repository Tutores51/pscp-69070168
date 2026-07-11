'''check surprising'''
total_score = float(input())
highest_score = float(input())

lowest_score = max(0, total_score - highest_score * 2)

if highest_score - lowest_score > 2:
    print("Surprising")
else:
    print("Not surprising")
