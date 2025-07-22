from stats import get_num_words
from stats import count_characters
from stats import sorted_character_count
import sys

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    filepath = sys.argv[1]
    book_text = get_book_text(filepath)
    num_words = get_num_words(book_text)
    character_count = count_characters(book_text)
    sorted_counts = sorted_character_count(character_count)
    
    print(f"============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}")
    print(f"----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print(f"--------- Character Count -------")
    for char, count in sorted_counts:
        print(f"{char}: {count}")
    print(f"============= END ===============")
    
main()