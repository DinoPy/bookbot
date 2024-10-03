def main():
    book = load_book("./books/frankenstein.txt")
    print(count_words(book))
    print(char_count(book))


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


main()
