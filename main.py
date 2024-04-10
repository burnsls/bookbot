def main():
    book_path = "books/frakenstein.txt"
    book_text = get_book_text(book_path)
    num_words = count_words(book_text)
    letter_count = count_letters(book_text)
    print_report(book_path, num_words, letter_count)

def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def count_words(text):
    return len(text.split())

def count_letters(text):
    char_count = {}
    lower_case_text = text.lower()
    for char in lower_case_text:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1        
    return char_count


def print_report(book_path, num_words, letter_count):
    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in document")
    list_of_chars = [{'char': key, 'count': value} for key, value in letter_count.items()]
    list_of_chars.sort(reverse=True, key=lambda x: x['count'])
    for item in list_of_chars:
        if item['char'].isalpha():
            print(f"The '{item['char']}' character was found {item['count']}")
        
main()