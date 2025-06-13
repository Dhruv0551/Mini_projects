import random

lowercase_letters = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
]

uppercase_letters = [
    "A",
    "B",
    "C",
    "D",
    "E",
    "F",
    "G",
    "H",
    "I",
    "J",
    "K",
    "L",
    "M",
    "N",
    "O",
    "P",
    "Q",
    "R",
    "S",
    "T",
    "U",
    "V",
    "W",
    "X",
    "Y",
    "Z",
]

letters = lowercase_letters + uppercase_letters
# print(letters)

digits = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

symbols = [
    "!",
    '"',
    "#",
    "$",
    "%",
    "&",
    "'",
    "(",
    ")",
    "*",
    "+",
    ",",
    "-",
    ".",
    "/",
    ":",
    ";",
    "<",
    "=",
    ">",
    "?",
    "@",
    "[",
    "]",
    "^",
    "_",
    "`",
    "{",
    "|",
    "}",
    "~",
]


charnum = int(input("How many characters do you want in your password? "))
symnum = int(input("How many symbols do you want in your password? "))
dignum = int(input("How many digits do you want in your password? "))
password = ""
for i in range(charnum - symnum - dignum):
    password += random.choice(letters)
for i in range(symnum):
    password += random.choice(symbols)
for i in range(dignum):
    password += random.choice(digits)
password = list(password)
random.shuffle(password)
password = "".join(password)
print(f"Your password is: {password}")
