'''ไพ่ 44 ใบ'''
card = input().upper()

suit = card[-1]
card = card[:-1]

if card == "A":
    card = "ace"
elif card == "J":
    card = "jack"
elif card == "Q":
    card = "queen"
elif card == "K":
    card = "king"

if suit == "D":
    suit = "diamonds"
elif suit == "H":
    suit = "hearts"
elif suit == "S":
    suit = "spades"
elif suit == "C":
    suit = "clubs"

print(card, "of", suit)
