def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    word_count = count_words(text)
    character_count = count_characters(text)
    # print(text)
    print(word_count)
    print(character_count)
    
    
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
    lowered_string = text.lower()
    words = lowered_string.split()
    for w in words:
        for c in w:
            if c in dict:
                dict[c] += 1
            else:
                dict[c] = 1
    return dict
        


main()