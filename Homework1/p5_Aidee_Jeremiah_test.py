"""Unit tests for the Caesar cipher homework program."""

import unittest

import p5_Aidee_Jeremiah as p5


class CaesarCipherTest(unittest.TestCase):
    """Tests Caesar cipher, decipher, and frequency functions."""

    def test_caesar_cipher_preserves_case_and_spaces(self):
        self.assertEqual(
            p5.caesar_cipher("Abc XyZ", 2),
            "Cde ZaB",
        )

    def test_caesar_cipher_wraps_around_alphabet(self):
        self.assertEqual(
            p5.caesar_cipher("xyz", 3),
            "abc",
        )

    def test_caesar_decipher_restores_original_text(self):
        cyphertext = p5.caesar_cipher("Hello, World!", 5)

        self.assertEqual(
            p5.caesar_decipher(cyphertext, 5),
            "Hello, World!",
        )

    def test_letter_frequency_ignores_case_and_nonletters(self):
        frequency = p5.letter_frequency("AaBbC! 123")

        self.assertEqual(frequency["a"], 2)
        self.assertEqual(frequency["b"], 2)
        self.assertEqual(frequency["c"], 1)
        self.assertEqual(frequency["z"], 0)


if __name__ == "__main__":
    unittest.main()