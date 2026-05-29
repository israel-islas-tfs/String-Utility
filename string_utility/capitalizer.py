"""Functions for capitalization-related string utilities."""

import re


_WORD_PATTERN = re.compile(r"[A-Za-z]+(?:'[A-Za-z]+)?")


def capitalize_words(text: str) -> str:
    """Capitalize each word in text while preserving surrounding characters.

    A word is treated as a sequence of letters, optionally containing one
    apostrophe, so common contractions like "don't" become "Don't".
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    def capitalize_match(match: re.Match[str]) -> str:
        word = match.group(0)
        return word[0].upper() + word[1:].lower()

    return _WORD_PATTERN.sub(capitalize_match, text)
