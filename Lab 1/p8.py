def generate_binary(n):
    """
    Generate the binary representation of integers from 1 to n, inclusive.

    Args:
    n -- an integer representing the upper bound of the range (inclusive)

    Yields:
    binary -- a string representing the binary representation of each integer in the range
    """

    # iterate over the range 1 to n
    for i in range(1, n+1):
        # convert the integer to binary and remove the '0b' prefix
        binary = bin(i)[2:]
        # yield the binary representation of the integer
        yield binary


def test_generate_binary():
    # Test case 1
    assert list(generate_binary(5)) == ['1', '10', '11', '100', '101']

    # Test case 2
    assert list(generate_binary(10)) == ['1', '10', '11', '100', '101', '110', '111', '1000', '1001', '1010']

    # Test case 3
    assert list(generate_binary(1)) == ['1']

    # Test case 4
    assert list(generate_binary(0)) == []

    # Test case 5
    assert list(generate_binary(4)) == ['1', '10', '11', '100']

    print("All test cases pass")


test_generate_binary()
