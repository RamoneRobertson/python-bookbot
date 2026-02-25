from stats import get_num_words, get_char_counts, print_report

def get_book_text(file_path):
    with open(file_path) as book:
        text = book.read()
        return text

def main():
    text = get_book_text("./books/frankenstein.txt")
    word_count = get_num_words(text)
    char_counts = get_char_counts(text)
    # print(f"Found {word_count} total words")
    # print(char_counts)
    print_report(char_counts)

main()
