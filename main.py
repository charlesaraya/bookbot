import sys

from stats import get_num_words, get_num_chars, sort_num_chars

def get_book_text(filepath):
    with open(filepath, 'r') as f:
        file_contents = f.read()
    return file_contents

def main():
    if len(sys.argv) == 2:
        filepath = sys.argv[1]
    print("============ BOOKBOT ============",
          f"Analyzing book found at {filepath}...",
          "----------- Word Count ----------")
    book_contents = get_book_text(filepath)
    print(get_num_words(book_contents))

    print("--------- Character Count -------")
    num_chars = get_num_chars(book_contents)
    sorted_num_chars = sort_num_chars(num_chars)
    for char, num in sorted_num_chars:
        if char.isalpha():
            print(f"{char}: {num}")
    print("============= END ===============")

main()