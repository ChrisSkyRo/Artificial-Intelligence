def count_ones(row):
    """
    Counts the number of 1s in a sorted binary list using binary search.

    Args:
        row: A list of 0s and 1s sorted in non-decreasing order.

    Returns:
        The number of 1s in the list.
    """
    left, right = 0, len(row)
    while left < right:
        mid = (left + right) // 2
        if row[mid] == 1:
            left = mid + 1
        else:
            right = mid
    return left


def max_ones_index(matrix):
    """
    Finds the index of the row with the most 1s in a binary matrix.

    Args:
        matrix: A list of lists of 0s and 1s sorted in non-decreasing order.

    Returns:
        The index of the row with the most 1s. If multiple rows have the same
        number of 1s, returns the index of the first such row.
    """
    max_count = 0
    max_index = 0
    for i, row in enumerate(matrix):
        count = count_ones(row)
        if count > max_count:
            max_count = count
            max_index = i
    return max_index


def test_max_ones_index():
    """
    Tests the max_ones_index function with some example inputs.
    """
    inputs = [
        ([[0, 0, 1], [0, 1, 1], [0, 0, 0]], 1),
        ([[0, 0, 0], [1, 1, 1], [0, 1, 1]], 1),
        ([[1, 1], [1, 1], [1, 1]], 0),
        ([[0, 0, 0, 1, 1], [0, 1, 1, 1, 1], [0, 0, 1, 1, 1]], 1),
    ]
    for matrix, expected_output in inputs:
        assert max_ones_index(matrix) == expected_output


# Run the test function
test_max_ones_index()
