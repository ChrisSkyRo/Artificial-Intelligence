def majority_element(nums):
    """
    Finds the element in a list of integers that appears more than n/2 times, where n is the length of the list.

    Args:
    numbers: A list of integers.

    Returns:
    The majority element in the list.
    """
    count = 0
    candidate = None

    for num in nums:
        if count == 0:
            candidate = num
        if num == candidate:
            count += 1
        else:
            count -= 1

    return candidate


def test_majority_element():
    assert majority_element([1, 2, 3, 3, 3, 3, 4, 5]) == 3
    assert majority_element([1, 1, 2, 2, 2]) == 2
    assert majority_element([1, 1, 1, 1]) == 1
    assert majority_element([1]) == 1
    assert majority_element([2, 8, 7, 2, 2, 5, 2, 3, 1, 2, 2]) == 2

    print("All tests passed!")


test_majority_element()
