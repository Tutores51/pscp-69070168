price = int(input())
fee = price * 0.10
if fee < 50:
    fee = 50
elif fee > 1000:
    fee = 1000
vat = (price + fee) * 0.07
total = price + fee + vat
print(f"{total:.2f}")
