def find_duplicate(numbers):
    # Get the length of the input list
    n = len(numbers)

    # Perform XOR operation on all elements of the input list
    # to obtain the XOR sum of all the elements
    xor1 = 0
    for i in range(n):
        xor1 ^= numbers[i]

    # Perform XOR operation on all numbers from 1 to n-1
    # to obtain the XOR sum of all these numbers
    xor2 = 0
    for i in range(1, n):
        xor2 ^= i

    # The duplicate element is the XOR of xor1 and xor2
    return xor1 ^ xor2


def test_find_duplicate():
    assert find_duplicate([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10]) == 10
    assert find_duplicate([1, 2, 3, 4, 5, 5]) == 5
    assert find_duplicate([1, 2, 3, 4, 4]) == 4
    assert find_duplicate([1, 1, 2, 3, 4]) == 1
    assert find_duplicate([1, 2, 3, 4, 4, 5]) == 4
    assert find_duplicate([1, 2, 3, 3, 4, 5]) == 3
    assert find_duplicate([1, 1]) == 1
    assert find_duplicate([1, 2, 2]) == 2
    assert find_duplicate([1, 1, 2]) == 1
    assert find_duplicate([2, 2, 1]) == 2
    assert find_duplicate([1, 2, 3, 4, 2]) == 2

    print("All tests passed!")


test_find_duplicate()
