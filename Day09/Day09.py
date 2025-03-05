
import art
print(art.logo)
def find_highest_bid(bidding):
    winner = ""
    highest_bid = 0
    for bidder in bidding:
        bid_amt = bidding[bidder]
        if bid_amt > highest_bid:
            highest_bid = bid_amt
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}.")
bid = {}
cond = True
while cond:
    name = input("What is your name?: ")
    price = int(input("What's your bid?: $"))
    bid[name] = price
    should_continue = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()
    if should_continue == "no":
        cond = False
        find_highest_bid(bid)
    elif should_continue == "yes":
        print("\n" * 20)
