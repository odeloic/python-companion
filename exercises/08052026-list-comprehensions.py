"""
Problem: Word Length Filter

Given a list of words and a minimum length, return a new list containing only
the words that meet the minimum length, each transformed to title case.

Examples:
    filter_words(["apple", "hi", "banana", "ok", "kiwi"], 4)
    → ["Apple", "Banana", "Kiwi"]

    filter_words(["hello", "world", "a", "python"], 5)
    → ["Hello", "World", "Python"]

    filter_words([], 3)
    → []

Acceptance criteria:
- Result contains only words with len >= min_length
- Each word in the result is title-cased
- Implemented as a single list comprehension (no loops)
- Original list is not modified
"""


def filter_words(words: list[str], min_length: int) -> list[str]:
    """
    Filter and transform words by minimum length.

    Args:
        words: list of lowercase strings
        min_length: minimum number of characters (inclusive)

    Returns:
        List of title-cased words that meet the length requirement
    """
    return [word.title() for word in words if len(word) > min_length]


if __name__ == "__main__":
    print(filter_words(["apple", "hi", "banana", "ok", "kiwi"], 4))
    print(filter_words(["hello", "world", "a", "python"], 5))
    print(filter_words([], 3))
