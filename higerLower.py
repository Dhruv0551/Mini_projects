import random

art = """
╔════════════════╗
║   ⇧  HIGHER    ║
║   ⇩  LOWER     ║
╚════════════════╝
"""

data = [
    {
        "name": "Instagram",
        "follower_count": 620,
        "description": "Social media platform",
        "country": "United States"
    },
    {
        "name": "Cristiano Ronaldo",
        "follower_count": 590,
        "description": "Footballer",
        "country": "Portugal"
    },
    {
        "name": "Ariana Grande",
        "follower_count": 380,
        "description": "Musician and actress",
        "country": "United States"
    },
    {
        "name": "Dwayne Johnson",
        "follower_count": 395,
        "description": "Actor and professional wrestler",
        "country": "United States"
    },
    {
        "name": "Kylie Jenner",
        "follower_count": 400,
        "description": "Reality TV personality and businesswoman",
        "country": "United States"
    },
    {
        "name": "Lionel Messi",
        "follower_count": 510,
        "description": "Footballer",
        "country": "Argentina"
    },
    {
        "name": "TikTok",
        "follower_count": 350,
        "description": "Short-form video platform",
        "country": "China"
    },
    {
        "name": "NASA",
        "follower_count": 100,
        "description": "Space agency",
        "country": "United States"
    },
    {
        "name": "YouTube",
        "follower_count": 430,
        "description": "Video sharing platform",
        "country": "United States"
    },
    {
        "name": "Selena Gomez",
        "follower_count": 430,
        "description": "Musician and actress",
        "country": "United States"
    }
]


def compare():
    points = 0
    alt_choice = ""
    while True:
        option_1 = random.randint(0,9)
        option_2 = random.randint(0,9)
        if option_2 == option_1:
            option_2 = random.randint(0,9)
        print("Your Choices are: ")
        print(f"A. {data[option_1]["name"]}, {data[option_1]["description"]}, {data[option_1]["country"]}")
        print(f"B. {data[option_2]["name"]}, {data[option_2]["description"]}, {data[option_2]["country"]}")
        user_choice = input("Enter Your choice(A/B): ").upper()
        if user_choice == "A":
            user_choice = option_1
            alt_choice = option_2
        elif user_choice == "B":
            alt_choice = option_1
            user_choice = option_2
        else:
            print("Invalid Input Try Again")
            return
        if data[alt_choice]["follower_count"] > data[user_choice]["follower_count"]:
            print("You Lose🥀🥀")
            print(f"Your Points: {points}")
            break
        elif data[alt_choice]["follower_count"] < data[user_choice]["follower_count"]:
            print("Correct Guess")
            points+=1
            print(f"Your points {points}")
        

while True:
    choice = input("Would You like to play the Game?(y/n): ")
    
    print("\n"*4)

    if choice == "y":
        print(art)
        compare()
    elif choice == "n": 
        print("Thank You For Playing")
        break
    else:
        print("Invalid Input")