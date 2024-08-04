import pandas

df = pandas.read_csv("./nato_phonetic_alphabet.csv")

alpha_dict = {row.letter: row.code for (index, row) in df.iterrows()}

user_input = input("Enter your name: ").upper()

printable_list = [code for (letter, code) in alpha_dict.items() if letter in user_input]

print(printable_list)