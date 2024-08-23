import argparse
import os

def main():
    # Create argument parser
    parser = argparse.ArgumentParser()

    # Define the required positional argument for the file path
    parser.add_argument("book_path_arg", help="Type the book location")

    # Parse the command-line arguments
    args = parser.parse_args()
    
    book_path = args.book_path_arg

    # Check if the file path has a .txt extension
    if not book_path.endswith(".txt"):
        raise ValueError(f"Invalid file type: '{book_path}'. Please provide a .txt file.")
    
    # Check if the file exists
    if not os.path.isfile(book_path):
        raise FileNotFoundError(f"The file '{book_path}' does not exist or the path is incorrect.")

    text = get_book_text(book_path)

    word_count = count_words(text)
    character_count = count_characters(text)

    # Sorted list of dictionarys with key (character) and value (character count), only alphabet
    char_list = [{"char": key, "count": value} for key, value in character_count.items() if key.isalpha()]
    
#   --- REPORT ---
    print(f"--- Begin report of {book_path} ---")
    print(f"""{word_count} words found in the document
          """)
    for char in sorted(char_list, reverse=True, key=sort_on):
        print(f"The '{char['char']}' character was found {char['count']} times")
    print("""
          --- End report ---""")

#   --- FUNCTIONS ---    
def sort_on(char_list):
    return char_list["count"]
    
def get_book_text(path):    
    with open(path) as f:
        return f.read()

def count_words(text):
    words = text.split()
    return len(words)

def count_characters(text):
    dict = {}
    for character in text.lower():
        if character in dict:
            dict[character] += 1
        else:
            dict[character] = 1
    return dict


main()