def get_book_text(path):
    with open(path) as file:
        return file.read()

def get_num_words(book_text):
    book_words = book_text.split()
    return len(book_words)

def get_char_counts(book_text):
    char_counts = dict()
    for char in book_text:
        l_char = char.lower()
        if l_char not in char_counts:
            char_counts[l_char] = 0
        
        char_counts[l_char] += 1
    return char_counts

def get_sorted_list(char_dict):
    sorted_list = list()

    def sort_key(values):
        return values["count"]
    
    for char in char_dict:
        sorted_list.append({"char": char, "count": char_dict[char]})
    
    sorted_list.sort(reverse=True, key=sort_key)
    return sorted_list