def count_words(text):
    words = text.split()
    number_of_words = len(words)
    return number_of_words

def get_book_text(file_path):
    try:
        with open(file_path, 'r') as file:
            book_text = file.read()
        return book_text
    except FileNotFoundError:
        print(f"The file {file_path} does not exist. Please check the file name and path.")
        return None

# Prompt the user to enter the file path/name
book_file = input("Enter the path to your book file: ")

# Get the text of the book
book_text = get_book_text(book_file)

# Ensure we have the text before counting words
if book_text:
    # Count the words in the book text
    word_count = count_words(book_text)
    
    # Print the result
    print(f"The book contains {word_count} words.")