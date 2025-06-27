import pandas as pd

data = pd.read_csv("nato_phonetic_alphabet.csv")
phonetic_alpha = {row.letter: row.code for index, row in data.iterrows()}
while True:
    user_input = input("Enter Your Name: ").upper()
    user_split = list(user_input)
    try:
        user_nato = [phonetic_alpha[letter] for letter in user_split]
        print(user_nato)
        break
    except KeyError:
        print("Only Alphabets are Allowed")
