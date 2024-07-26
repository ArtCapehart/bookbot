import operator

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
    total_letters = sum(letters_counted.values())
    letter_string = []
    # Sort the dictionary by value in descending order
    sorted_letters = sorted(letters_counted.items(), key=operator.itemgetter(1), reverse=True)
    rank = 1
    for i, (letter, count) in enumerate(sorted_letters):
        if letter.isalpha():
            percentage = (count / total_letters) * 100
            letter_string.append(f"Rank {rank}: the letter '{letter}' appears {count} times ({percentage:.2f}%)")
            rank += 1
    return letter_string


    
        

main()