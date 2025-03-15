def get_book_text(filepath):
    with open(filepath, 'r') as file:
        return file.read()
    
def get_num_words(text):
    words = text.split()
    return len(words)

def get_characters(text):
    characters = {}
    for character in text.lower():
        if character in characters:
            characters[character] += 1
        else:
            characters[character] = 1
    return characters


def analyze(filepath):
    text = get_book_text(filepath)
    num_words = get_num_words(text)
    character_list = list(get_characters(text).items())
    sorted_characters = sorted(character_list, key=lambda x: x[1], reverse=True)
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("---------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("---------- Character Count ----------")
    for char, count in sorted_characters:
        if char.isalpha():
            print(f"{char}: {count}")
    print("============= END ===============")