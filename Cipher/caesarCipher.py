from art import logo

print(logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def caesar(text_place, shift_number, direction_place):
    caesar_text = ''
    if direction_place == "decode":
        shift_number *= -1
    for char in text_place:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = position + shift_number
            new_letter = alphabet[new_position]
            caesar_text += new_letter
        else:
            caesar_text += char    
  
    print(f"The {direction}d message is: {caesar_text}")        

should_continue = True
while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))


    shift = shift % 26     

    caesar(text_place=text, shift_number=shift, direction_place=direction)  

    go_again = input("DO you wanna run the program again? 'Y' ot 'N' ").lower()
    if go_again == "n":
        should_continue = False
        print("Good bye")
