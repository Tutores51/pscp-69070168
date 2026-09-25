'''สงคราม...ส่งด่วน'''
def main():
    '''pack'''
    start, end = input().upper().split()
    weight = float(input())

    if start == "BKK" and end == "CNX":
        fee = 10
        rate = 30
    elif start == "CNX" and end == "UBP":
        fee = 15
        rate = 40
    elif start == "UBP" and end == "BKK":
        fee = 20
        rate = 40
    elif start == "BKK" and end == "PKT":
        fee = 25
        rate = 50
    elif start == "PKT" and end == "CNX":
        fee = 30
        rate = 60
    elif start == "UBP" and end == "PKT":
        fee = 40
        rate = 70
    else:
        print("Error")
        return

    total = fee + weight * rate
    print(f"{total:.2f}")

main()
