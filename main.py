from stats import count_words

def get_book_text(filepath):
    with open(filepath, 'r') as f:
        file_contents = f.read()
    return file_contents

def main():
    book_contents = get_book_text('books/frankenstein.txt')
    print(count_words(book_contents))

main()