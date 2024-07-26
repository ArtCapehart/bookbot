def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    letters_counted = letter_counter(text)
    letters_listed = letter_lister(letters_counted)
    print(f"{num_words} words found in the document")
    print("\n".join(letters_listed))

     


def get_num_words(text):
    words = text.split()
    return len(words)


def get_book_text(path):
    with open(path) as f:
        return f.read()


def letter_counter(text):
    lower_text = text.lower()
    letter_dict = {}
    for letter in lower_text:
        if letter in letter_dict: 
            letter_dict[letter] += 1
        else: 
            letter_dict[letter] = 1
    return letter_dict

def letter_lister(letters_counted):
    letter_string = [] 
    for key, value in letters_counted.items():
        if key.isalpha() == True: 
            letter_string.append(f"the letter '{key}' is counted {value} times.")
    letter_string.sort()
    return letter_string


    
        

main()