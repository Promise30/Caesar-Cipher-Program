alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
            'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
            'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd',
            'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
            'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

from Cipher_logo import cipher_logo

def caesar_cipher(user_text , shift_amount , user_choice):
    """Returns back a string that is either an encrypted or decrypted text based on the user's choice"""
    shift_amount = shift_amount % 26
    
    end_result = ""
    
    if user_choice == "decode":
        shift_amount = shift_amount * -1

        
    for char in user_text:
        if char in alphabet:
            char_position = alphabet.index(char)
            new_position = char_position + shift_amount
            end_result += alphabet[new_position]
        else:
            end_result += char
    print(f"Here's the {user_choice}d result:\n\t {end_result}")


running = True

while running:
    
    print(cipher_logo)
    
    text = input("Enter a text:\n ").lower()
    shift_number = int(input("Enter a shift number:\n "))
    option = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n ")
    
    caesar_cipher(text , shift_number , option)

    restart = input("\nType 'yes' if you want to go again. Type 'no' if otherwise:\n ").lower()
    if restart == 'no':
        running = False
        print("Thank you for using the Caesar Cipher.")
