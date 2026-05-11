"""
Problem: Run-Length Encoding

Given a string, return a list of (character, count) tuples representing
consecutive runs of the same character.

Examples:
    "aaabbc"   -> [("a", 3), ("b", 2), ("c", 1)]
    "aabbaa"   -> [("a", 2), ("b", 2), ("a", 2)]
    "abcd"     -> [("a", 1), ("b", 1), ("c", 1), ("d", 1)]

Acceptance criteria:
- Empty string returns an empty list.
- Each tuple contains the character and how many times it appears consecutively.
- Adjacent identical runs must be kept separate (e.g. "aabbaa" yields two "a" entries).
"""


def run_length_encode(s: str) -> list[tuple[str, int]]:
    """
    Encode a string as consecutive character runs.

    Args:
        s: The input string (may be empty).

    Returns:
        A list of (char, count) tuples, one per consecutive run.
    """
    raise NotImplementedError


if __name__ == "__main__":
    # print(run_length_encode("aaabbc"))   # [("a", 3), ("b", 2), ("c", 1)]
    # print(run_length_encode("aabbaa"))   # [("a", 2), ("b", 2), ("a", 2)]
    # print(run_length_encode("abcd"))     # [("a", 1), ("b", 1), ("c", 1), ("d", 1)]
    # print(run_length_encode(""))         # []
    pass
