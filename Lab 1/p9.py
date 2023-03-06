def submatrix_sum(matrix, coord_list):
    # Create a sum matrix
    n, m = len(matrix), len(matrix[0])
    sum_matrix = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            sum_matrix[i][j] = sum_matrix[i - 1][j] + sum_matrix[i][j - 1] - sum_matrix[i - 1][j - 1] + matrix[i - 1][
                j - 1]

    sums = []
    # Calculate submatrix sum using formula
    for coord in coord_list:
        coord1, coord2 = coord
        x1, y1 = coord1
        x2, y2 = coord2
        sums.append(sum_matrix[x2 + 1][y2 + 1] - sum_matrix[x2 + 1][y1] - sum_matrix[x1][y2 + 1] + sum_matrix[x1][y1])
    return sums


def test_submatrix_sum():
    # Test case 1
    matrix1 = [[1, 2, 3],
               [4, 5, 6],
               [7, 8, 9]]
    coord1 = (0, 0)
    coord2 = (2, 2)
    assert submatrix_sum(matrix1, [(coord1, coord2)]) == [45]

    # Test case 2
    matrix2 = [[1, 1], [1, 1]]
    coord3 = (0, 0)
    coord4 = (1, 1)
    assert submatrix_sum(matrix2, [(coord3, coord4)]) == [4]

    # Test case 3
    matrix3 = [[1, 2, 3],
               [4, 5, 6],
               [7, 8, 9]]
    coord5 = (1, 0)
    coord6 = (2, 1)
    assert submatrix_sum(matrix3, [(coord5, coord6)]) == [24]

    # Test case 4
    matrix4 = [[1, 2],
               [3, 4],
               [5, 6]]
    coord7 = (1, 0)
    coord8 = (2, 1)
    assert submatrix_sum(matrix4, [(coord7, coord8)]) == [18]

    # Test case 5
    matrix5 = [[0, 2, 5, 4, 1],
               [4, 8, 2, 3, 7],
               [6, 3, 4, 6, 2],
               [7, 3, 1, 8, 3],
               [1, 5, 7, 9, 4]]
    coord9 = (1, 1)
    coord10 = (3, 3)
    coord11 = (2, 2)
    coord12 = (4, 4)
    assert submatrix_sum(matrix5, [(coord9, coord10), (coord11, coord12)]) == [38, 44]
    print("All test cases pass")


test_submatrix_sum()
