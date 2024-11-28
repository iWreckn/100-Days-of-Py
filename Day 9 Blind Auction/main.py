from art import logo
print(logo)

def find_highest_bid(bidding_dictionary):
    highest_bid = 0
    winner = ""
    for bidder in  bidding_dictionary:
        bid_amount = bidding_dictionary[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with the bid of ${highest_bid}.")
print("Welcome to the silent auction.")
bids = {}
continue_bidding = True
while continue_bidding:
    name = input("Enter your name: ")
    price = float(input("Enter your bid: $"))
    bids[name] = price
    should_continue = input("Is there more bidders? \n Yes or No: ").lower()
    if should_continue == 'no':
        continue_bidding = False
        find_highest_bid(bids)
    elif should_continue == 'yes':
        print("\n" * 20)