def dot_product(vector1, vector2):
    """
    Calculates the dot product of two vectors.

    Args:
    vector1: A list or tuple representing the first vector.
    vector2: A list or tuple representing the second vector.

    Returns:
    The dot product of the two vectors.
    """
    if not hasattr(vector1, "__len__"):
        return vector1 * vector2

    if len(vector1) != len(vector2):
        raise ValueError("Vectors must have the same number of dimensions.")

    dot_prod = 0
    for x, y in zip(vector1, vector2):
        dot_prod += dot_product(x, y)

    return dot_prod


def test_dot_product():
    """
    Tests the dot_product function.
    """
    assert dot_product([1, 2, 3], [4, 5, 6]) == 32
    assert dot_product([1, 0, 2, 0, 3], [1, 2, 0, 3, 1]) == 4
    assert dot_product([0, 0, 0], [1, 2, 3]) == 0
    assert dot_product([1, 2, 3], [0, 0, 0]) == 0
    assert dot_product([1, 2], [3, 4]) == 11
    assert dot_product([[[5]], [[5]], [[7]]], [[[0]], [[2]], [[0]]]) == 10
    assert dot_product([[1], [2], [1]], [[0], [3], [0]]) == 6
    try:
        dot_product([1, 2, 3], [4, 5])
        assert False
    except ValueError:
        pass

    print("All tests passed!")


test_dot_product()
