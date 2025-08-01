import os

def SilentAuction(winner_names, max_value):
    print(f"The winner is {winner_names} with a bid of ₹{max_value}")

print("Welcome to Silent Auction Program")
new = {}
compare = "yes"

while compare.lower() == "yes":
    name = input("What is your name: ")
    cost = int(input("What is your bid: ₹"))
    new[name] = cost
    compare = input("Are there any other bidders? (yes/no): ")
    os.system('cls')
     
max_value = max(new.values())
winners = [k for k, v in new.items() if v == max_value]
winner_names = ", ".join(winners)
SilentAuction(winner_names, max_value)
