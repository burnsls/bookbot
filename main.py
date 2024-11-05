def main():
    book_path = "books/frankenstein.txt"
    book_contents = get_book_contents(book_path)
    word_count = count_words(book_contents)
    char_count = character_count(book_contents)
    sorted_chars = sort_chars(char_count)
    print_report(book_path, word_count, sorted_chars)
    


def get_book_contents(book_path):
        with open("books/frankenstein.txt") as f:
            file_contents = f.read()
        return file_contents
    
def count_words(book_contents):
    words_list = book_contents.split()
    return len(words_list)

def character_count(book_contents):
    char_count = {}
    for char in book_contents:
        lowered_char = char.lower()
        if lowered_char in char_count:
            char_count[lowered_char] += 1
        else:
            char_count[lowered_char] = 1
    return char_count

def sort_on(dict):
    return dict["num"]

def sort_chars(char_dict):
    sorted_list = []
    for ch in char_dict:
        sorted_list.append({"char": ch, "num": char_dict[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list
    

def print_report(book_path, word_count, sorted_chars):
    print(f"--- Begin report of {book_path} ---")
    print(f"{word_count} words found in the document\n")
    for item in sorted_chars:
        if item["char"].isalpha():
            print(f"The {item['char']} character was found {item['num']} times")
    print(f"\n--- End report ---")

main()