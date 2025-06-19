coffee_menu = {
    "espresso": {
        "water": 50,
        "milk": 0,
        "coffee": 18,
        "price": 1.5
    },
    "latte": {
        "water": 200,
        "milk": 150,
        "coffee": 24,
        "price": 2.5
    },
    "cappuccino": { 
        "water": 250,
        "milk": 100,
        "coffee": 24,
        "price": 3.0
    }
}

material = {
    "water" : 300,
    "milk": 200,
    "coffee" : 100,
    "cash": 0
}

pennies = 0.01
nickles = 0.05
dimes = 0.1
quaters = 0.25

while True:
    choice = input("What do you want: ")
    if choice == "latte" or choice == "espresso" or choice == "cappuccino":
        if material["milk"] >= coffee_menu[choice]["milk"] and material["water"]>=coffee_menu[choice]["water"] and material["coffee"]>=coffee_menu[choice]["coffee"]:
            print(f"Please Pay for {choice}, Price: ${coffee_menu[choice]["price"]} ")
            num_of_pennies = int(input("Enter Number of Pennies: "))
            num_of_nickles = int(input("Enter Number of Nickles: "))
            num_of_dimes = int(input("Enter Number of Dimes: "))
            num_of_quaters = int(input("Enter Number of quaters: "))
            price_paid = (num_of_dimes * dimes) + (num_of_nickles * nickles) + (num_of_pennies * pennies) + (num_of_quaters * quaters)
            if price_paid < coffee_menu[choice]["price"]:
                print("Not Enough Money, Amount Refunded")
            else:
                material["water"] = material["water"] - coffee_menu[choice]["water"]
                material["milk"] = material["milk"] - coffee_menu[choice]["milk"]
                material["coffee"] = material["coffee"] - coffee_menu[choice]["coffee"]
                material["cash"] += coffee_menu[choice]["price"]
                if price_paid > coffee_menu[choice]["price"]:
                    rem_case = round(price_paid-coffee_menu[choice]["price"], 2)
                    print(f"Here is Your Change: ${rem_case}")
                print(f"Enjoy Your {choice}")
        else:
            print(f"Sorry Insufficient material for {choice}")
    elif choice == "report":
        print(material)
    elif choice == "exit":
        print("Thank You for Using Coffee Machine")
        break
    else:
        print("Invalid Choice")

