def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_word_count(book):
    words = book.split()
    return len(words)

def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    word_count = get_word_count(text)
    print(f"{word_count} words found in the document.")

main()