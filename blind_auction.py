candidates = {}
venue = """    _____         _                   _     
   |  _  |___ ___| |_ ___ ___ ___ ___| |___ 
   |     | . |  _| '_| -_| . | . | . | | -_|
   |__|__|___|_| |_,_|___|___|___|___|_|___|
        AUCTION TIME!
"""
print(venue + "\n\n")

name = input("Enter Your Name : ")
candidates[name] = int(input("Enter Your Bid : "))
max_bid = candidates[name]
max_bidder = name

choice = input("Are there any other candidates ?(y/n) ")
while choice == "y":
    if choice != "y" and choice != "n":
        print("Invalid choice")
        break
    print("\n" * 20)
    name = input("Enter Your Name : ")
    candidates[name] = int(input("Enter Your Bid : "))
    choice = input("Are there any other candidates ?(y/n) ")

for candidate in candidates:
    if candidates[candidate] > max_bid:
        max_bid = candidates[candidate]
        max_bidder = candidate

print(f"\n\nThe winner is {max_bidder} with a bid of {max_bid}.")
print("Thank you for participating in the auction!")
