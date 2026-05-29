"""Command-line menu for the String Utility Library."""

from colorama import Fore, init
from .capitalizer import capitalize_words

init(autoreset=True)


def show_menu() -> None:
    print(f"{Fore.YELLOW}\nString Utility Library")
    print(f"{Fore.YELLOW}1. Capitalize words")
    print(f"{Fore.YELLOW}2. Show examples")
    print(f"{Fore.YELLOW}3. Exit")


def show_examples() -> None:
    examples = [
        "",
        "hello world",
        "  mixed   SPACING  ",
        "hello, world!",
        "@hello #world 123test",
        "don't stop believing",
    ]

    print("\nExamples")
    for example in examples:
        print(f"{example!r} -> {capitalize_words(example)!r}")


def main() -> None:
    while True:
        show_menu()
        choice = input(f"{Fore.RED}Select an option: ").strip()

        if choice == "1":
            text = input(f"{Fore.RED}Enter a string to capitalize: ")
            print(f"Result: {capitalize_words(text)}")
        elif choice == "2":
            show_examples()
        elif choice == "3":
            print("Goodbye.")
            break
        else:
            print("Invalid option. Please choose 1, 2, or 3.")


if __name__ == "__main__":
    main()
