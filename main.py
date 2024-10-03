def main():
    path = "frankenstein.txt"
    book = load_book(f"./books/{path}")
    count = count_words(book)
    print(f"--- Begin report of books/{path} ---")
    print(f"{count} words found in the document", end="\n")
    cc = char_count(book)
    print_char_count(cc)
    print("--- End report ---")


def load_book(path):
    with open(path, "r") as book:
        return book.read()


def count_words(book):
    return len(book.split())


def char_count(book):
    char_count = {}
    for char in book:
        c = char.lower()
        if c in char_count:
            char_count[c] += 1
        else:
            char_count[c] = 1

    return char_count


def print_char_count(char_count):
    for char in char_count:
        if char.isalpha():
            print(f"The '{char}' character was found {char_count[char]} times")


main()
