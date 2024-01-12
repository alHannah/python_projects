import auction_art
import os


def clear():
    os.system('clear' if os.name == 'posix' else 'cls')


print(auction_art.logo)
bidding = True
bids = {}


def check_highest_bidding(biders):
    initial = 0
    highest_bidder = ""
    """Looping in every bids dictionary."""
    for every_bid in biders:
        bidd = biders[every_bid]
        
        if bidd > initial:
            initial = bidd
            highest_bidder = every_bid
    winner = highest_bidder
    winbid = bids[highest_bidder]

    """Print the winner in bidding."""
    print(f"The winner is {highest_bidder} amounting {winbid}")
    print("\n\nALL BIDS:")

    """Print all bid history"""
    for allbids in bids:
        all_biders = allbids
        all_bids = bids[allbids]
        print(f"BIDDER: {all_biders}    BID: {all_bids}")


while bidding:
    """Get the Bidders Name and Bid amount."""
    bidders_name = input("Name: ")
    bidders_bid = int(input("Bid: "))
    
    """Dictionary of bids and bidders."""
    bids[bidders_name] = bidders_bid

    make_more_bid = input("Other Bidders? [y] [n]\n: ")

    """Check for another bid."""
    if make_more_bid == "n":
        bidding = False
        check_highest_bidding(bids)
    elif make_more_bid == "y":
        clear()


  