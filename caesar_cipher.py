import art

print(art.logo)

alphabet = [
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

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


# Create a function called 'encrypt()' that takes 'original_text' and 'shift_amount' as 2 inputs.
def encrypt(original_text, shift_amount):
    # Inside the 'encrypt()' function, shift each letter of the 'original_text' forwards in the alphabet by the shift amount
    cipher_text = " "
    for letter in original_text:
        position = alphabet.index(letter)
        new_position = position + shift_amount
        # What happens if you try to shift z forwards by 9? Can you fix the code?
        if new_position >= 26:
            new_position -= 26
        new_letter = alphabet[new_position]
        cipher_text += new_letter

    print(f"here is the encoded result: {cipher_text}")


# Create a function called 'decrypt()' that takes 'original_text' and 'shift_amount' as 2 inputs.
def decrypt(original_text, shift_amount):
    # Inside the 'decrypt()' function, shift each letter of the 'encrypted_text' backwards in the alphabet by the shift amount
    cipher_text = " "
    for letter in original_text:
        position = alphabet.index(letter)
        new_position = position - shift_amount
        # What happens if you try to shift a letter backwards by 9? Can you fix the code?
        if new_position < 0:
            new_position += 26
        new_letter = alphabet[new_position]
        cipher_text += new_letter

    print(f"Here is the decoded result: {cipher_text}")

# Combine the 'encrypt()' and 'decrypt()' functions into one function called 'caesar()'.
# Use the value of the user chosen 'direction' variable to determine which functionality to use.
def caesar(original_text, shift_amount, encode_or_decode):
    output_text = ""
    if encode_or_decode == "decode":
        shift_amount *= -1

    for letter in original_text:
        if letter not in alphabet:
            output_text += letter
        else:
            shifted_position = alphabet.index(letter) + shift_amount
            shifted_position %= len(alphabet)
            output_text += alphabet[shifted_position]
    print(f"Here is the {encode_or_decode}d result: {output_text}")

# Can you figure out a way to restart the cipher program?
should_continue = True

while should_continue:

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar(original_text=text, shift_amount=shift, encode_or_decode=direction)

    restart = input(
        "Type 'yes' if you want to go again. Otherwise, type 'no'.\n"
    ).lower()
    if restart == "no":
        should_continue = False
        print("\nSee you again!")
