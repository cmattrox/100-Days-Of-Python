from art import logo, alphabet

def caesar(text, shift, direction):
        shift %= len(alphabet)
        if (direction == "decode"):
            shift *= -1

        encrypted_text = ""
        for letter in text:
            if (letter not in alphabet):
                encrypted_text += letter
            else:
                index = alphabet.index(letter) + shift

                if (index >= len(alphabet)):
                    index -= len(alphabet)
                elif (index < 0):
                    index += len(alphabet)

                new_letter = alphabet[index]
                encrypted_text += new_letter

        print(f"The {direction}d text is {encrypted_text}")

cont = "y"

while cont == "y":
    print(logo)
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar(text, shift, direction)
    cont = input("Would you like to run again? [y/n]: ").lower()