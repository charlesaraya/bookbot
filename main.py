from stats import get_num_words, get_num_chars, sort_num_chars

def get_book_text(filepath):
    with open(filepath, 'r') as f:
        file_contents = f.read()
    return file_contents

def main():
    book_contents = get_book_text('books/frankenstein.txt')
    print(get_num_words(book_contents))
    num_chars = get_num_chars(book_contents)
    print(sort_num_chars(num_chars))

main()