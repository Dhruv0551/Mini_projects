#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

placeholder = "[name]"

with open('./Input/Names/invited_names.txt') as names_file:
    names = names_file.readlines()
    print(names)


with open('./Input/Letters/starting_letter.txt') as letter_file:
    letter = letter_file.read()
    for name in names:  
        strippedWord = name.strip()
        finalLetters = letter.replace(placeholder, strippedWord)
        with open(f'./Output/ReadyToSend/letters_for_{strippedWord}.txt',mode='w') as finalLetterfile:
            finalLetterfile.write(finalLetters)
