from replit import clear
from art import logo

# HINT: You can call clear() to clear the output in the console.
print(logo)
print("Welcome to the secret auction program.")

bid_library = {}
auction_open = True


def collect_bid():
    user_name = input("What is your name?: ")
    user_bid = int(input("What is your bid?: $"))
    bid_library[user_name] = user_bid


def find_winner(bid_dictionary):
    highest_bid = 0
    highest_bidder = ""
    for user_name in bid_dictionary:
        if (bid_dictionary[user_name]) > highest_bid:
            highest_bid = (bid_dictionary[user_name])
            highest_bidder = user_name

    print(f"The winner is {highest_bidder} with a bid of ${highest_bid}")


while auction_open:
    collect_bid()
    more_bids = input("Are there any other bids? Type 'yes' or 'no': ")
    if more_bids.lower() == "no":
        auction_open = False
    clear()

find_winner(bid_library)