from stats import get_num_words, get_char_counts, sort_char_counts
import sys

print("Usage: python3 main.py <path_to_book>")

def get_book_text(file_path):
    with open(file_path) as book:
        text = book.read()
        return text

def main():
    book_path = sys.argv[1]
    text = get_book_text(book_path)
    word_count = get_num_words(text)
    char_counts = get_char_counts(text)
    sorted_list = sort_char_counts(char_counts)
    print(f"============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for item in sorted_list:
        print(f"{item["char"]}: {item["num"]}")
    # print(f"Found {word_count} total words")
    # print(char_counts)


main()
