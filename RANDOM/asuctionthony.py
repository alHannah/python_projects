

def clear():
    os.system('clear' if os.name == 'posix' else 'cls')

bidding = True
bids = {}

def check(biders):
    initial = 0
    win = ""
    for every_bid in biders:
        bidd = biders[every_bid]
        if bidd > initial:
            initial = bidd
            win = every_bid
    winner = win
    winbid = bids[win]
    print(f"The winner is {win} ammounting {winbid}")

    for allbids in bids:
        all_biders = allbids
        all_bids = bids[allbids]
        print(f"{all_biders} {all_bids}")
while bidding:
    name = input("Name: ")
    bid = int(input("Bid: "))
    bids[name] = bid


    condition = input("Other Bidders? [y] [n]\n: ")
    if condition == "n":
        bidding = False
        check(bids)
    elif condition == "y":
        print("\n\n")

  