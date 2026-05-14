"""
Problem: Run-Length Encoding

Given a list of values, return a list of (value, count) tuples that
compresses consecutive repeated elements.

Examples:
    [1, 1, 2, 3, 3, 3]        → [(1, 2), (2, 1), (3, 3)]
    ["a", "a", "b", "a"]      → [("a", 2), ("b", 1), ("a", 1)]
    [True]                     → [(True, 1)]

Acceptance criteria:
    - Non-consecutive duplicates are treated as separate runs.
    - An empty list returns an empty list.
    - Works for any list of comparable values.
"""


def run_length_encode(values: list) -> list[tuple]:
    """
    Compress a list by grouping consecutive identical elements.

    Args:
        values: A list of any comparable values.

    Returns:
        A list of (value, count) tuples representing consecutive runs.
    """
    if not values:
        return []
    result = []
    current = values[0]
    count = 1
    for value in values[1:]:
        if value == current:
            count += 1
        else:
            result.append((current, count))
            current = value
            count = 1
    result.append((current, count))
    return result


if __name__ == "__main__":
    print(run_length_encode([1, 1, 2, 3, 3, 3]))  # [(1, 2), (2, 1), (3, 3)]
    print(run_length_encode(["a", "a", "b", "a"]))  # [("a", 2), ("b", 1), ("a", 1)]
    print(run_length_encode([]))  # []
