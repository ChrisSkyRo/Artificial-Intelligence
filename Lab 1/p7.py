import heapq


def k_largest_elements(array, k):
    """
        Returns the kth largest element in a list of integers.

        Parameters:
        array (list): A list of integers.
        k (int): An integer specifying the kth largest element to return.

        Returns:
        int: The kth largest element in the list.

        """
    heap = []
    for num in array:
        if len(heap) < k:
            heapq.heappush(heap, num)
        else:
            heapq.heappushpop(heap, num)
    return heap[0]


def test_k_largest_elements():
    # Test case 1
    assert k_largest_elements([1, 3, 5, 7, 9, 2, 4, 6, 8], 3) == 7

    # Test case 2
    assert k_largest_elements([5, 4, 3, 2, 1], 1) == 5

    # Test case 3
    assert k_largest_elements([1, 1, 1, 1], 2) == 1

    # Test case 4
    assert k_largest_elements([7, 4, 6, 3, 9, 1], 2) == 7

    print("All test cases pass")


test_k_largest_elements()
