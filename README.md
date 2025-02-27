# bookbot

BookBot is my first [Boot.dev](https://www.boot.dev) project!

# How to Use the Book Analysis Tool

## Overview
This tool reads the contents of a text file (book), counts the number of words, and provides a detailed analysis of character frequencies, including the percentage of each character relative to the total number of characters.

## Prerequisites
- Python 3.x installed on your system
- A directory named `books` containing text files (.txt) for analysis

## Files
- `main.py`: The main script to run the analysis
- `stats.py`: Contains functions for counting words and characters, and sorting character counts

## Functions

### `main.py`
- `get_book_text(filepath)`: Reads the contents of a file and returns it as a string.
- `list_books(directory)`: Lists all the books in the given directory and prints their paths.
- `main()`: Main function that lists all books and their paths, then reads the contents of a selected book and prints the number of words and character analysis.

### `stats.py`
- `count_words(text)`: Counts the number of words in a given text.
- `count_characters(text)`: Counts the number of times each character appears in the text.
- `sort_char_counts(char_counts)`: Takes a dictionary of characters and their counts and returns a sorted list of dictionaries. Each dictionary has a single key-value pair, where the key is the character and the value is the count and percentage of the total count.

## Usage

1. **List Available Books**
   - When you run `main.py`, it will list all the available books in the `books` directory.
   - Example:
     ```
     Available books:
     frankenstein.txt: books/frankenstein.txt
     dracula.txt: books/dracula.txt
     ```

2. **Run the Analysis**
   - To run the analysis on a specific book, provide the path to the book as a command-line argument.
   - Example:
     ```sh
     python3 main.py books/frankenstein.txt
     ```

3. **Output**
   - The script will print the total number of words in the book.
   - It will also print the character counts and their percentages in the format `char: (count @ percentage)`.
   - Example:
     ```
     Found 78456 total words
     e: (119351 @ 9.64%)
     t: (87456 @ 7.06%)
     ...
     ```

## Example

1. **List Books**
   ```sh
   python3 main.py
2. Analyze a Book
  python3 main.py books/frankenstein.txt
