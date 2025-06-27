from stats import count_words, count_characters, sorted_count
import sys

def get_book_text (filepath):
    with open(filepath) as f:
        return f.read()

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    path = sys.argv[1]
    text = get_book_text(path)
    count = count_words(text)
    characters = count_characters(text)
    sortedCharacters = sorted_count(characters)
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {count} total words")
    print("--------- Character Count -------")
    for c in sortedCharacters:
        if c["char"].isalpha():
            print(f"{c["char"]}: {c["num"]}")

main()