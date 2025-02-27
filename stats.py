def get_num_words(text):
    """
    Counts the number of words in a given text.

    :param text: The text to count words in
    :return: The number of words in the text
    """
    words = text.split()
    return len(words)

def count_words(text):
    """
    Counts the number of words in a given text.

    :param text: The text to count words in
    :return: The number of words in the text
    """
    words = text.split()
    return len(words)

def count_characters(text):
    """
    Counts the number of times each character appears in the text.

    :param text: The text to count characters in
    :return: A dictionary with characters as keys and their counts as values
    """
    text = text.lower()
    char_count = {}
    for char in text:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count

def sort_char_counts(char_counts):
    """
    Takes a dictionary of characters and their counts and returns a sorted list of dictionaries.
    Each dictionary has a single key-value pair, where the key is the character and the value is the count.
    The list is sorted from greatest to least by the count, and includes the percentage of each character to the total count.

    :param char_counts: A dictionary with characters as keys and their counts as values
    :return: A sorted list of dictionaries
    """
    total_count = sum(char_counts.values())
    sorted_char_counts = sorted(char_counts.items(), key=lambda item: item[1], reverse=True)
    return [{char: (count, f"{(count / total_count) * 100:.2f}%")} for char, count in sorted_char_counts]