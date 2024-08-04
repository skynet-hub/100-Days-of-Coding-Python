PLACEHOLDER = "[name]"

with open("./Input/Names/invited_names.txt") as names_file:
    names = names_file.readlines()
    
with open("./Input/Letters/starting_letter.txt") as letter_file:
    contents = letter_file.read()    
    for name in names:
        stripped_name = name.strip()
        new_letter = contents.replace(PLACEHOLDER, stripped_name)
        with open(f"./Output/ReadyToSend/invite_letter_{stripped_name}", mode='w') as new_letter_file:
            new_letter_file.write(new_letter)



