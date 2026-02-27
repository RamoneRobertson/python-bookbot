
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

def sort_on(dict_item):
    return dict_item["num"]


def sort_char_counts(char_count_dict):
    book_data = []
    for key, value in char_count_dict.items():
        if(key.isalpha()):
            book_data.append({"char": key, "num": value})

    book_data.sort(reverse=True, key=sort_on)
    return book_data
