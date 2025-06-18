import random

cards = [2,3,4,5,6,7,8,9,10,10,10,10,11]
limit = 21
min_limit = 16


def total(cards):
    total = sum(cards)
    aces = cards.count(11)

    while total > 21 and aces:
        total -= 10
        aces -= 1

    return total



while True:
	want_to_repeat = input("Do you want to play BlackJack(y/n): ")


	if want_to_repeat == "y":

		print("\n"*5)
		user_cards = []
		user_cards.extend([random.choice(cards),random.choice(cards)])
		print(f"Your cards are {user_cards} and the total is {total(user_cards)}")
		
		
		dealer_cards = []
		dealer_cards.extend([random.choice(cards),random.choice(cards)])
		if total(dealer_cards) < min_limit:
			while total(dealer_cards) < min_limit:
				dealer_cards.append(random.choice(cards))
		print(f"Dealer's first card is {dealer_cards[0]}")
		
		
		
		while True:
			choice = input("Type 'y' to get another card, type 'n' to pass: ")
			if choice == "y":
				user_cards.append(random.choice(cards))
				print(f"Your cards are : {user_cards} and total is {total(user_cards)}")
				if total(user_cards) > limit:
					print("You are busted for exceeding the limit(21)")
					print("You Lose🥀🥀🥀")
					break
		
			elif choice == "n":
				print(f"Total of Your Cards: {total(user_cards)}")
				print(f"Dealer's Cards {dealer_cards} and total {total(dealer_cards)}")
				if total(dealer_cards) == limit:
					print("Dealer has BlackJack!!!")
					print("You Lose🥀🥀🥀")
					break
				elif total(dealer_cards) > limit:
					print("Dealer is Busted for exceeding the Limit")
					print("You win😤😤")
					break
				elif total(dealer_cards) > total(user_cards):
					print("Dealer has Better cards")
					print("You Lose🥀🥀🥀")
					break
				elif total(dealer_cards) < total(user_cards):
					print("You have Better Cards")
					print("You win😤😤")
					break
				elif total(dealer_cards) == total(user_cards):
					print("Its a Tie!!!")
					break


	elif want_to_repeat == "n":
		print("Thanks for Playing")
		break


	else:
		print("Invalid Input")