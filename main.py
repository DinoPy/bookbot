def main():
    book = load_book("./books/frankenstein.txt")
    print(count_words(book))
    char_count(book)


def load_book(path):
    with open(path, "r") as book:
        return book.read()


def count_words(book):
    return len(book.split())


def char_count(book):
    pass


main()
