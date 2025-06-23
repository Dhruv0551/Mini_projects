import pandas as pd

data = pd.read_csv("nato_phonetic_alphabet.csv")
phonetic_alpha = {}
for index, row in data.iterrows():
    phonetic_alpha[row.letter] = row.code


# print(phonetic_alpha)
user_input = input("Enter Your Name: ").upper()
user_nato = []
user_split = list(user_input)
# print(user_split)

for key, value in phonetic_alpha.items():
    if key in user_split:
        user_nato.append(value)


print(user_nato)
