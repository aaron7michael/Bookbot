def get_book_text(path: str) -> str:
    with open(path) as file:
        return file.read()

def get_num_words(book_text: str) -> int:
    book_words = book_text.split()
    return len(book_words)

def get_char_counts(book_text: str) -> dict:
    char_counts = {}
    for char in book_text:
        l_char = char.lower()
        if l_char not in char_counts:
            char_counts[l_char] = 0

        char_counts[l_char] += 1
    return char_counts

def get_sorted_list(char_dict: dict[str, int]) -> list:
    sorted_list = []

    def sort_key(values):
        return values["count"]

    for char in char_dict.items():
        sorted_list.append({"char": char[0], "count": char[1]})

    sorted_list.sort(reverse=True, key=sort_key)
    return sorted_list

#Alternate implementation of get_sorted_list
def chars_dict_to_sorted_list(char_dict: dict[str, int]) -> list[tuple[str, int]]:

    char_counts = [ (item[0], item[1] ) for item in char_dict.items() ]

    return sorted(char_counts, key=lambda char_count: char_count[1])
