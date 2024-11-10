import pandas

df = pandas.read_csv("./nato_phonetic_alphabet.csv")

alpha_dict = {row.letter: row.code for (index, row) in df.iterrows()}
print(alpha_dict)


def generate_phonetic():
    user_input = input("Enter your word: ").upper()

    try:
        printable_list = [alpha_dict[letter] for letter in user_input]
    except KeyError:
        print("Sorry only letters in the alphabet please...") 
        generate_phonetic()          
    else:    
        print(printable_list)    

generate_phonetic()        