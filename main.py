def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_word_count(text):
    words = text.split()
    return len(words)

def get_character_count(text):
    character_count = {}
    lowered_text = text.lower()

    for character in lowered_text:
        if character.isalpha():
            if character in character_count:
              character_count[character] += 1
            else:
                character_count[character] = 1
    
    return character_count



def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    character_count = get_character_count(text)
    word_count = get_word_count(text)
    character_list = [{letter: number} for letter, number in character_count.items()]
    character_list.sort(reverse=True, key=lambda x: list(x.values())[0])
    
    print(f"--- Begin report of {book_path} ---")
    print(f"{word_count} words found in the document.\n")
    for dict in character_list:
        for key, value in dict.items():
            print(f"The {key} character was found {value} times")
    print("--- End report ---")

main()
