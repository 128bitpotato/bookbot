def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    word_count = count_words(text)
    character_count = count_characters(text)
    report = gen_report(character_count, book_path, word_count)
    print(f"Report: {report}")

def gen_report(dict, book, word):
    char_list = [{"char": key, "count": value} for key, value in dict.items() if key.isalpha()]
    def sort_on(char_list):
        return char_list["count"]
    print(f"--- Begin report of {book} ---")
    print(f"""{word} words found in the document
          """)
    for char in sorted(char_list, reverse=True, key=sort_on):
        print(f"The '{char['char']}' character was found {char['count']} times")
    print("""
          --- End report ---""")
    
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