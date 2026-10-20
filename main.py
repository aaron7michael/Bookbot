import sys
from stats import chars_dict_to_sorted_list, get_book_text, get_char_counts, get_num_words, get_sorted_list

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    print('============ BOOKBOT ============')
    book_path = sys.argv[1]
    print(f'Analyzing book found at {book_path}...')

    book_text = get_book_text(book_path)

    print('----------- Word Count ----------')
    num_words = get_num_words(book_text)
    print(f'Found {num_words} total words')

    print('--------- Character Count -------')
    char_counts = get_char_counts(book_text)
    sorted_list = get_sorted_list(char_counts)
    for result in sorted_list:
        if result['char'].isalpha():
            print(f'{result["char"]}: {result["count"]}')


    print('--------- Character Count Alternate-------')
    sorted_list = chars_dict_to_sorted_list(char_counts)
    for result in sorted_list:
        if result[0].isalpha():
            print(f'{result[0]}: {result[1]}')

    print('============= END ===============')

if __name__=="__main__":
    main()
