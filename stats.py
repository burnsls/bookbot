
def get_num_words(book_string):
    num_words = len(book_string.split())
    return num_words

def count_characters(book_string):
    """Counts the number of times each character appears in the book."""
    character_count = {}
    for char in book_string:
        if char.isalpha():
            char = char.lower()
            character_count[char] = character_count.get(char, 0) + 1
    return character_count

def sorted_character_count(character_count):
    """Returns a sorted list of characters and their counts."""
    return sorted(character_count.items(), key=lambda item: item[1], reverse=True)