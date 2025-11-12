import sys
from stats import get_num_words, character_frequencies, sorted_frequencies

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def main():
    #book_path = "books/frankenstein.txt"
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    character_counts = character_frequencies(text)
    sorted_character_counts = sorted_frequencies(character_counts)
    for character in sorted_character_counts:
            if character['char'].isalpha():
                print(f"{character['char']}: {character['num']}")
    print("============= END ===============")    


if __name__ == "__main__":
    main()