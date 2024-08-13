def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    word_count = count_words(text)
    character_count = count_characters(text)
    report = gen_report(character_count)
    # print(f"Word count: {word_count}")
    # print(f"Character count: {character_count}")
    print(f"Report: {report}")
    
    
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

def gen_report(dict):
    char_list = [{"char": key, "count": value} for key, value in dict.items() if key.isalpha()]
    return char_list

main()