"""Interactive Caesar cipher and letter-frequency analyzer."""


LOWERCASE_ALPHABET = "abcdefghijklmnopqrstuvwxyz"
UPPERCASE_ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def caesar_cipher(text, shift):
    """Returns text encrypted with a Caesar shift."""
    encrypted_characters = []
    shift = shift % len(LOWERCASE_ALPHABET)

    for character in text:
        if character in LOWERCASE_ALPHABET:
            old_index = LOWERCASE_ALPHABET.index(character)
            new_index = (
                old_index + shift
            ) % len(LOWERCASE_ALPHABET)
            encrypted_characters.append(LOWERCASE_ALPHABET[new_index])

        elif character in UPPERCASE_ALPHABET:
            old_index = UPPERCASE_ALPHABET.index(character)
            new_index = (
                old_index + shift
            ) % len(UPPERCASE_ALPHABET)
            encrypted_characters.append(UPPERCASE_ALPHABET[new_index])

        else:
            encrypted_characters.append(character)

    return "".join(encrypted_characters)


def caesar_decipher(cyphertext, shift):
    """Returns the original text by reversing a Caesar shift."""
    return caesar_cipher(cyphertext, -shift)


def letter_frequency(text):
    """Counts letters while ignoring case and non-alphabetic characters."""
    frequency = {}

    for letter in LOWERCASE_ALPHABET:
        frequency[letter] = 0

    for character in text.lower():
        if character in LOWERCASE_ALPHABET:
            frequency[character] += 1

    return frequency


def _print_frequency(frequency):
    """Prints letter frequencies in alphabetical order."""
    print("Letter frequencies:")

    for letter in LOWERCASE_ALPHABET:
        print("{}: {}".format(letter, frequency[letter]))


def main():
    """Runs the interactive Caesar cipher menu."""
    while True:
        print("\nCaesar Cipher Menu")
        print("1. Encrypt, analyze, and decrypt a message")
        print("2. Quit")

        choice = input("Enter your choice: ")

        if choice == "1":
            message = input("Enter a message: ")
            shift = int(input("Enter shift value: "))

            cyphertext = caesar_cipher(message, shift)
            frequency = letter_frequency(cyphertext)
            clear_text = caesar_decipher(cyphertext, shift)

            print("Ciphered text: {}".format(cyphertext))
            _print_frequency(frequency)
            print("Deciphered text: {}".format(clear_text))

        elif choice == "2":
            print("Goodbye.")
            break

        else:
            print("Invalid choice. Enter 1 or 2.")


if __name__ == "__main__":
    main()