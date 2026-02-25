
def get_num_words(text):
    return len(text.split())

def get_char_counts(text):
    char_counts = {}
    for char in text:
        if char.lower() not in char_counts:
            char_counts[char.lower()] = 1
        else:
            char_counts[char.lower()] += 1

    return char_counts

def print_report(char_count_dict):
    book_data = []
    for key, value in char_count_dict.items():
        new_dict = {"char": key, "num": value}
        book_data.append(new_dict)

    book_data.sort(key=sort_on)


    print(book_data)
