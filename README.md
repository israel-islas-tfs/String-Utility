# String Utility Library

A small Python project that demonstrates Test-Driven Development (TDD) with a
string utility that capitalizes words.

## Project Goal

Build a library function that capitalizes words while preserving empty strings,
spacing, punctuation, numbers, and other special characters.

## Run The Tests

```powershell
python -m unittest discover
```

## Run The Terminal Menu

```powershell
python -m string_utility.cli
```

## TDD Flow

1. Write tests for the behavior you want.
2. Run the tests and watch them fail.
3. Write the smallest amount of code to pass the tests.
4. Refactor while keeping the tests green.

This project includes tests for:

- Empty strings
- Single and multiple words
- Existing capitalization
- Extra spaces
- Punctuation and special characters
- Numbers mixed with words
