alphabets = [
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


def ceaserCypher(original_text, shift, ed):
    def encrypt(original_text, shift):
        encrypted_text = ""
        text_list = list(original_text)
        for letter in text_list:
            if letter in alphabets:
                index = alphabets.index(letter)
                new_index = (index + shift) % len(alphabets)
                encrypted_text += alphabets[new_index]
            else:
                encrypted_text += letter
        return encrypted_text

    if ed == "e":
        return encrypt(original_text, shift)

    # def encrypt2(original_text, shift):
    #     cyp_text = ""
    #     for letter in original_text:
    #         shifted_pos = alphabets.index(letter) + shift % len(alphabets)
    #         if shifted_pos >= len(alphabets):
    #             shifted_pos -= len(alphabets)
    #         elif shifted_pos < 0:
    #             shifted_pos += len(alphabets)
    #         cyp_text += alphabets[shifted_pos]
    #     return cyp_text

    def decrypt(original_text, shift):
        decrypted_text = ""
        for letter in original_text:
            if letter in alphabets:
                index = alphabets.index(letter)
                new_index = (index - shift) % len(alphabets)
                decrypted_text += alphabets[new_index]
            else:
                decrypted_text += letter
        return decrypted_text

    if ed == "d":
        return decrypt(original_text, shift)


want_to_repeat = True
while want_to_repeat:
    user_response = input("Do you want to Continue? (yes/no): ").lower()
    if user_response == "no":
        want_to_repeat = False
        print("Thank you for using the Caesar Cipher Program!")
        break
    elif user_response != "yes":
        print("Invalid input. Please enter 'yes' or 'no'.")
        continue

    choice = input("Do you want to encrypt or decrypt? (e/d): ").lower()
    original_text = input("Enter the text to encrypt/decrypt: ")
    shift = int(input("Enter the shift value: "))
    ceaserCypher(original_text, shift, choice)
    if choice == "e":
        print("Encrypted text:", ceaserCypher(original_text, shift, "e"))
    elif choice == "d":
        print("Decrypted text:", ceaserCypher(original_text, shift, "d"))
    else:
        print("Invalid choice. Please enter 'e' for encrypt or 'd' for decrypt.")
