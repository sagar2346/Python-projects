# 'def' is used for declaring a function. The function name is 'encrypt' and it takes two parameters: 'text' and 'shift'.
def encrypt(text, shift):
    # Initialize an empty string to store the final encrypted message.
    encrypted_text = ""

    # Loop through each character in the 'text' string.
    for char in text:
        # If the character is uppercase (A-Z), apply the Caesar cipher.
        if char.isupper():
            new_position = (ord(char) - 65 + shift) % 26  
            new_char = chr(new_position + 65)  
            encrypted_text += new_char 

        # If the character is lowercase (a-z), apply the Caesar cipher.
        elif char.islower():
            new_position = (ord(char) - 97 + shift) % 26  
            new_char = chr(new_position + 97)  
            encrypted_text += new_char  

        # If it's not a letter (e.g., space, punctuation), keep it unchanged.
        else:
            encrypted_text += char  # Just add the character as it is.

    # Return the final encrypted message after the loop is done.
    return encrypted_text

# Define the decrypt function to use the same logic as encrypt but with a negative shift.
def decrypt(text, shift):
    return encrypt(text, -shift)

# Get input from the user
user_input = input("Enter the message: ")
shift_value = int(input("Enter the shift value: "))
choose = input('Type "e" for encryption or "d" for decryption: ').lower()

# Process the user's choice
if choose == 'e':
    encrypted_message = encrypt(user_input, shift_value)
    print(f"Encrypted Message: {encrypted_message}")

elif choose == 'd':
    decrypted_message = decrypt(user_input, shift_value)
    print(f"Decrypted Message: {decrypted_message}")

else:
    print('Enter a valid choice either "e" or "d"')
