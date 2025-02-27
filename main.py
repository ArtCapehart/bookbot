from stats import count_words, count_characters, sort_char_counts
import sys
import os  # Importing necessary functions from stats.py

def get_book_text(filepath):
    """
    Reads the contents of a file and returns it as a string.

    :param filepath: Path to the file
    :return: Contents of the file as a string
    """
    with open(filepath, 'r', encoding='utf-8') as file:
        book_text = file.read()  # Open and read the file, storing contents in book_text

    # Print debug info before returning
    print(f"Loaded text from {filepath}: {book_text[:500]}... (length: {len(book_text)})")
    return book_text

def list_books(directory):
    """
    Lists all the books in the given directory and prints their paths.

    :param directory: Path to the directory containing the books
    """
    print("Access Syntax: python3 main.py/books/<book_name.txt>")
    print("Available books:")
    for filename in os.listdir(directory):
        if filename.endswith(".txt"):
            print(f"{filename}: {os.path.join(directory, filename)}")

def main():
    """
    Main function that lists all books and their paths, then reads the contents of a selected book and prints the number of words in the book.
    """
    books_directory = 'books'
    list_books(books_directory)  # List all books and their paths

    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
        
    book_path = sys.argv[1]  # Get the book path from command line arguments
    book_text = get_book_text(book_path)  # Read the contents of the book file
    num_words = count_words(book_text)  # Count the number of words in the book text
    print(f"Found {num_words} total words")  # Print the total number of words

    char_counts = count_characters(book_text)  # Count the number of times each character appears in the text
    sorted_char_counts = sort_char_counts(char_counts)  # Sort the character counts from greatest to least
    
    for char_count in sorted_char_counts:  # Iterate over each dictionary in the sorted list
        for char, (count, percentage) in char_count.items():  # Extract the character, its count, and percentage from each dictionary
            if char.isalpha():  # Check if the character is an alphabetic character
                print(f"{char}: ({count} @ {percentage})")  # Print the character, its count, and percentage

if __name__ == "__main__":
    main()  # Execute the main function