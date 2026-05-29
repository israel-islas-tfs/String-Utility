"""Command-line menu for the String Utility Library."""

from .capitalizer import capitalize_words


def show_menu() -> None:
    print("\nString Utility Library")
    print("1. Capitalize words")
    print("2. Show examples")
    print("3. Exit")


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
        choice = input("Select an option: ").strip()

        if choice == "1":
            text = input("Enter a string to capitalize: ")
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
