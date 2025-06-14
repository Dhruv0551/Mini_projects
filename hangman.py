import random

stages = [
    """
    +---+
    |   |
    O   |
    |   |
   / \\ |
   / \\ |
        |=========
    """,
    """
    +---+
    |   |
    O   |
    |   |
   / \\ |
  /   |
        |=========
    """,
    """
    +---+
    |   |
    O   |
    |   |
   / \\ |
        |=========
    """,
    """
    +---+
    |   |
    O   |
    |   |
   /    |
        |=========
    """,
    """
    +---+
    |   |
    O   |
    |   |
        |
        |========= 
    """,
    """
    +---+
    |   |
    O   |
        |
        |        |
        |========= 
    """,
    """
    +---+
    |   |
        |
        |
        |
        |=========
    """,
]


# hangman_words.py

words = [
    "anchor",
    "breeze",
    "candle",
    "dancer",
    "eclipse",
    "fossil",
    "galaxy",
    "hazard",
    "icicle",
    "jungle",
    "kitten",
    "lantern",
    "magnet",
    "nectar",
    "oracle",
    "parrot",
    "quartz",
    "rocket",
    "saddle",
    "trophy",
    "umbrella",
    "velvet",
    "whistle",
    "xenon",
    "yonder",
    "zephyr",
    "advice",
    "banana",
    "cradle",
    "dagger",
    "engine",
    "forest",
    "goblet",
    "hammer",
    "island",
    "jigsaw",
    "kernel",
    "lizard",
    "mantis",
    "napkin",
    "object",
    "pencil",
    "quiver",
    "ribbon",
    "sphinx",
    "talent",
    "unicorn",
    "vacuum",
    "window",
    "yellow",
    "zipper",
    "artist",
    "battle",
    "circle",
    "donkey",
    "effect",
    "flavor",
    "gravel",
    "hunter",
    "insect",
    "jacket",
    "keeper",
    "legend",
    "marble",
    "notion",
    "orange",
    "pirate",
    "quench",
    "rescue",
    "signal",
    "tunnel",
    "update",
    "vessel",
    "wander",
    "yellow",
    "zigzag",
    "almond",
    "basket",
    "clover",
    "doodle",
    "echoes",
    "fluffy",
    "grapes",
    "hollow",
    "impact",
    "jungle",
    "kidnap",
    "laptop",
    "mirror",
    "nugget",
    "outlet",
    "plunge",
    "quirky",
    "refine",
    "silent",
    "timber",
    "unfold",
    "voyage",
    "walnut",
    "yogurt",
    "zodiac",
    "arcade",
    "ballet",
    "cactus",
    "deluxe",
    "effect",
    "fabric",
    "glider",
    "helmet",
    "ignore",
    "jumble",
    "kitten",
    "launch",
    "mystic",
    "needle",
    "option",
    "planet",
    "quartz",
    "rhythm",
    "school",
    "ticket",
    "unique",
    "virtue",
    "wander",
    "yawned",
    "zipper",
    "acorns",
    "beacon",
    "chisel",
    "debris",
    "embark",
    "freeze",
    "gather",
    "hiccup",
    "injury",
    "jungle",
    "knight",
    "luxury",
    "magnet",
    "narrow",
    "outcry",
    "plight",
    "quaint",
    "remind",
    "spooky",
    "timely",
    "unrest",
    "viewer",
    "weasel",
    "yonder",
    "zenith",
]

chosen_word = random.choice(words)


placeholder = ""
num = len(chosen_word)


for i in range(num):
    placeholder += "_"
print(placeholder)
display = ""

guessed_letters = []

game_over = False

lives = 6
while not game_over:
    display = ""
    guess = input("Enter Your letter : ").lower()

    for letters in chosen_word:
        if letters == guess:
            display += guess
            guessed_letters.append(guess)
        elif letters in guessed_letters:
            display += letters
        else:
            display += "_"
    if guess not in guessed_letters:
        guessed_letters.append(guess)
        lives -= 1
        print(stages[lives])

        print(f"You have {lives} lives left.")
        if lives == 0:
            print("You lose!")
            game_over = True
    else:
        print("You already guessed the letter:", guess)

    print(display)
    if display == chosen_word:
        print("You win!")
        game_over = True
    else:
        print("Keep guessing!")
