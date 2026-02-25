def count_occurrences(phrase: str, letter: str) -> int:

    """
    Count occurrences of a letter in a phrase (case insensitive).
    """
    if not letter:
        return 0
    return phrase.lower().count(letter.lower())
