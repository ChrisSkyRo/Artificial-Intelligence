def replace_zeros(matrix):
    n = len(matrix)
    m = len(matrix[0])
    visited = set()

    def dfs(i, j):
        visited.add((i, j))
        for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            ni, nj = i + di, j + dj
            if 0 <= ni < n and 0 <= nj < m and matrix[ni][nj] == 0 and (ni, nj) not in visited:
                dfs(ni, nj)

    # Find all groups of 0 that reach the border
    border_zeros = set()
    for i in range(n):
        if matrix[i][0] == 0:
            dfs(i, 0)
        if matrix[i][m - 1] == 0:
            dfs(i, m - 1)
    for j in range(m):
        if matrix[0][j] == 0:
            dfs(0, j)
        if matrix[n - 1][j] == 0:
            dfs(n - 1, j)

    # Replace all groups of 0 that don't reach the border with '1'
    for i in range(1, n - 1):
        for j in range(1, m - 1):
            if matrix[i][j] == 0 and (i, j) not in visited:
                matrix[i][j] = 1

    return matrix


def test_replace_zeros():
    mat = [[1, 1, 1, 1, 0, 0, 1, 1, 0, 1],
           [1, 0, 0, 1, 1, 0, 1, 1, 1, 1],
           [1, 0, 0, 1, 1, 1, 1, 1, 1, 1],
           [1, 1, 1, 1, 0, 0, 1, 1, 0, 1],
           [1, 0, 0, 1, 1, 0, 1, 1, 0, 0],
           [1, 1, 0, 1, 1, 0, 0, 1, 0, 1],
           [1, 1, 1, 0, 1, 0, 1, 0, 0, 1],
           [1, 1, 1, 0, 1, 1, 1, 1, 1, 1]]

    result = [[1, 1, 1, 1, 0, 0, 1, 1, 0, 1],
              [1, 1, 1, 1, 1, 0, 1, 1, 1, 1],
              [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
              [1, 1, 1, 1, 1, 1, 1, 1, 0, 1],
              [1, 1, 1, 1, 1, 1, 1, 1, 0, 0],
              [1, 1, 1, 1, 1, 1, 1, 1, 0, 1],
              [1, 1, 1, 0, 1, 1, 1, 0, 0, 1],
              [1, 1, 1, 0, 1, 1, 1, 1, 1, 1]]

    assert replace_zeros(mat) == result


test_replace_zeros
