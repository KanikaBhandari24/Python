logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________
                       .-------------.
                      /_______________
'''
print(logo)

bid = {} 
finished = False

def highest(bidding):
    highest_bid = 0
    for bidder in bidding:
        amount = bidding[bidder]
        if amount > highest_bid:
            highest_bid = amount
            winner = bidder
        
    print(f"The winner is {winner} with a bid of ${highest_bid}")

while not finished:
    name = input("Enter your name: ")
    price = int(input("What is your bid? $"))
    #dict[key] = value
    bid[name] = price
    more = input("Are there any other bidders? Types 'yes' or 'no'\n")
    if more == "no":
        finished = True
        highest(bid)
        
        

