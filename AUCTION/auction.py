import auction_art
import os


def clear():
    os.system('clear' if os.name == 'posix' else 'cls')


"""List of bidders"""
bidders = []


def new_bidders(name, bid):
    dictionary_of_bidders = {
        "name": name,
        "bid": bid
    }
    bidders.append(dictionary_of_bidders)


bidding = True
while bidding:
    name = input("Name: ").lower()
    bid = int(input("Bid ammount: "))

    new_bidders(name, bid)

    new_bid = input("Is there other bidders?\n[yes] [no]\n:").lower()
    if new_bid == "yes":
        bidding = True
    elif new_bid == "no":
        bidding = False
    else:
        print("\n...")

if bidders:
    winner = max(bidders, key=lambda x: x["bid"])
    winner_name = winner["name"]
    winner_bid = winner["bid"]
    print(f"The winner is {winner_name}, amounting {winner_bid}")
else:
    print("No bidders found.")
