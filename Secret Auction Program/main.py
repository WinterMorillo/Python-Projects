"""
    Welcome to the secret auction program!

    This program has been created to run a secret auction, users would be able to bid for
    any item, they won't be able to see the others' birders names, until they all have bid,
    after the auction is finished, the final winner name will be displayed.

    Steps:

    Enter the first birder name.
    Enter the amount
    Enter either yes or no there will be other birders and hit no after all the birders had bid
    to see the final winner.

    This program was first created in replit.com, the module clear was call,
    for this code I'll comment out this line of code, and I'll include the link to my replit profile,
    so you can run the code there and use the clear() method.

    Replit link: https://replit.com/@WinterMorillo/blind-auction-start#main.py
"""

# from replit import clear
import art

# HINT: You can call clear() to clear the output in the console.
bidders_list = {}


def bidders(bidder_name, bidder_offer):
    bidders_list[bidder_name] = bidder_offer


print(art.logo)
print("Welcome to the Secret Auction Program!")
bid_finished = False

while not bid_finished:
    bidder_name = input("What's your name? ")
    bidder_offer = int(input("What's your bid? $"))
    bidders(bidder_name, bidder_offer)
    others = input("Are there any others bidders? ").lower()
    if others == "yes":
        # clear()
        pass
    else:
        # clear()
        bid_finished = True

highest_bid = 0
winner_bidder = ""
for bidder in bidders_list:
    if bidders_list[bidder] > highest_bid:
        winner_bidder = bidder
        highest_bid = bidders_list[bidder]
print(f"The winner is {winner_bidder}, with the highest amount for {highest_bid}")





