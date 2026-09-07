"""Unit tests for the Caesar cipher program."""

import unittest

import p5_jeremiah_aidee


class CaesarCipherTest(unittest.TestCase):
    """Tests the Caesar cipher functions."""

    def test_caesar_cipher(self):
        """Tests basic Caesar cipher encryption."""
        result = p5_jeremiah_aidee.caesar_cipher('Hello World', 3)
        self.assertEqual(result, 'Khoor Zruog')

    def test_caesar_cipher_preserves_case(self):
        """Tests that capitalization is preserved."""
        result = p5_jeremiah_aidee.caesar_cipher('AbC', 1)
        self.assertEqual(result, 'BcD')

    def test_caesar_cipher_wraps_alphabet(self):
        """Tests letters wrapping from z back to a."""
        result = p5_jeremiah_aidee.caesar_cipher('xyz', 3)
        self.assertEqual(result, 'abc')

    def test_caesar_cipher_preserves_nonletters(self):
        """Tests that spaces and punctuation are unchanged."""
        result = p5_jeremiah_aidee.caesar_cipher('Hello, World!', 3)
        self.assertEqual(result, 'Khoor, Zruog!')

    def test_caesar_decipher(self):
        """Tests Caesar cipher decryption."""
        result = p5_jeremiah_aidee.caesar_decipher(
            'Khoor Zruog', 3
        )
        self.assertEqual(result, 'Hello World')

    def test_cipher_and_decipher(self):
        """Tests encrypting and then decrypting a message."""
        message = 'Python Programming!'
        ciphertext = p5_jeremiah_aidee.caesar_cipher(message, 5)
        result = p5_jeremiah_aidee.caesar_decipher(ciphertext, 5)
        self.assertEqual(result, message)

    def test_letter_frequency(self):
        """Tests letter frequency counting."""
        result = p5_jeremiah_aidee.letter_frequency('Hello')

        self.assertEqual(result['h'], 1)
        self.assertEqual(result['e'], 1)
        self.assertEqual(result['l'], 2)
        self.assertEqual(result['o'], 1)

    def test_letter_frequency_ignores_case(self):
        """Tests that letter frequency ignores capitalization."""
        result = p5_jeremiah_aidee.letter_frequency('AaBbA')

        self.assertEqual(result['a'], 3)
        self.assertEqual(result['b'], 2)

    def test_letter_frequency_ignores_nonletters(self):
        """Tests that numbers and punctuation are ignored."""
        result = p5_jeremiah_aidee.letter_frequency('A! A2 B?')

        self.assertEqual(result['a'], 2)
        self.assertEqual(result['b'], 1)


if __name__ == '__main__':
    unittest.main()