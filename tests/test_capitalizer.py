import unittest

from string_utility import capitalize_words


class CapitalizeWordsTests(unittest.TestCase):
    def test_empty_string_returns_empty_string(self):
        self.assertEqual(capitalize_words(""), "")

    def test_single_word_is_capitalized(self):
        self.assertEqual(capitalize_words("hello"), "Hello")

    def test_multiple_words_are_capitalized(self):
        self.assertEqual(capitalize_words("hello world"), "Hello World")

    def test_existing_capitalization_is_normalized(self):
        self.assertEqual(capitalize_words("hELLo WoRLD"), "Hello World")

    def test_extra_spaces_are_preserved(self):
        self.assertEqual(capitalize_words("  hello   world  "), "  Hello   World  ")

    def test_punctuation_is_preserved(self):
        self.assertEqual(capitalize_words("hello, world!"), "Hello, World!")

    def test_special_characters_are_preserved(self):
        self.assertEqual(capitalize_words("@hello #world"), "@Hello #World")

    def test_numbers_are_preserved(self):
        self.assertEqual(capitalize_words("123 hello 456world"), "123 Hello 456World")

    def test_apostrophes_inside_words_are_supported(self):
        self.assertEqual(capitalize_words("don't stop"), "Don't Stop")

    def test_non_string_input_raises_type_error(self):
        with self.assertRaises(TypeError):
            capitalize_words(None)


if __name__ == "__main__":
    unittest.main()
