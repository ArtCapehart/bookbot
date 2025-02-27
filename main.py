from stats import count_words, count_characters, sort_char_counts
import sys  # Importing necessary functions from stats.py

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


def main():
    """
    Main function that reads the contents of frankenstein.txt and prints the number of words in the book.
    """
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
        for char, count in char_count.items():  # Extract the character and its count from each dictionary
            if char.isalpha():  # Check if the character is an alphabetic character
                print(f"{char}: {count}")  # Print the character and its count

if __name__ == "__main__":
    main()  # Execute the main function