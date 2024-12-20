def caesar_cipher(text, shift=5):
    encrypted_text = ""
    
    for char in text:
        if char.isalpha():  # Check if the character is a letter
            start = ord('a') if char.islower() else ord('A')
            encrypted_char = chr(start + (ord(char) - start + shift) % 26)
            encrypted_text += encrypted_char
        else
            encrypted_text += char  # Non-letter characters remain unchanged
    
    return encrypted_text

# Ask the user for input
user_input = input("Please enter a sentence: ")

# Encrypt the input using Caesar cipher
encrypted_sentence = caesar_cipher(user_input)

# Print the encrypted sentence
print("The encrypted sentence is:", encrypted_sentence)

