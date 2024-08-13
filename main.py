def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    word_count = count_words(text)
    character_count = count_characters(text)
    # print(text)
    print(f"Word count: {word_count}")
    print(f"Character count: {character_count}")
    
    
def get_book_text(path):    
    with open(path) as f:
        return f.read()

def count_words(text):
    words = text.split()
    count = 0
    for word in words:
        count += 1
    return count

# Short count_words function
#
# def get_num_words(text):
#    words = text.split()
#    return len(words)

def count_characters(text):
    dict = {}
    for character in text.lower():
        if character in dict:
            dict[character] += 1
        else:
            dict[character] = 1
    return dict


main()