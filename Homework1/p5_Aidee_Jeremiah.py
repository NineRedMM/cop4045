"""Interactive Caesar cipher program.

This program encrypts and decrypts text using a Caesar cipher.
It also counts the frequency of letters in a message.
"""


def caesar_cipher(text, shift):
    """Encrypts text using a Caesar cipher.

    Args:
        text: The string to encrypt.
        shift: The number of positions to shift each letter.

    Returns:
        The encrypted string.
    """
    lowercase = 'abcdefghijklmnopqrstuvwxyz'
    uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    encrypted_text = ''

    shift = shift % 26

    for character in text:
        if character in lowercase:
            index = lowercase.index(character)
            new_index = (index + shift) % 26
            encrypted_text += lowercase[new_index]
        elif character in uppercase:
            index = uppercase.index(character)
            new_index = (index + shift) % 26
            encrypted_text += uppercase[new_index]
        else:
            encrypted_text += character

    return encrypted_text


def caesar_decipher(ciphertext, shift):
    """Decrypts text that was encrypted with a Caesar cipher.

    Args:
        ciphertext: The encrypted string.
        shift: The number of positions used during encryption.

    Returns:
        The original decrypted string.
    """
    return caesar_cipher(ciphertext, -shift)


def letter_frequency(text):
    """Counts how many times each letter appears in text.

    The function ignores capitalization and non-alphabetic characters.

    Args:
        text: The string whose letters will be counted.

    Returns:
        A dictionary containing the frequency of each letter.
    """
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    frequencies = {}

    for letter in alphabet:
        frequencies[letter] = 0

    for character in text.lower():
        if character in alphabet:
            frequencies[character] += 1

    return frequencies


def display_frequency(frequencies):
    """Displays a letter frequency dictionary.

    Args:
        frequencies: A dictionary containing letter frequencies.
    """
    print('\nLetter Frequency:')
    for letter in frequencies:
        print(f'{letter}: {frequencies[letter]}')


def main():
    """Runs the interactive Caesar cipher menu."""
    while True:
        print('\nCaesar Cipher Menu')
        print('1. Encrypt and analyze a message')
        print('2. Decrypt a message')
        print('3. Exit')

        choice = input('Enter your choice: ')

        if choice == '1':
            message = input('Enter a message: ')

            try:
                shift = int(input('Enter a shift value: '))
            except ValueError:
                print('Shift value must be an integer.')
                continue

            ciphertext = caesar_cipher(message, shift)
            deciphered_text = caesar_decipher(ciphertext, shift)
            frequencies = letter_frequency(message)

            print(f'\nCiphered text: {ciphertext}')
            display_frequency(frequencies)
            print(f'\nDeciphered text: {deciphered_text}')

        elif choice == '2':
            ciphertext = input('Enter the ciphered message: ')

            try:
                shift = int(input('Enter the shift value: '))
            except ValueError:
                print('Shift value must be an integer.')
                continue

            deciphered_text = caesar_decipher(ciphertext, shift)
            print(f'Deciphered text: {deciphered_text}')

        elif choice == '3':
            print('Goodbye!')
            break

        else:
            print('Invalid choice. Please enter 1, 2, or 3.')


if __name__ == '__main__':
    main()