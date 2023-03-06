import math


# This function calculates the Euclidean distance between two points defined by their (x, y) coordinates.
def distance_between_points(x1, y1, x2, y2):
    distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    return distance


# This function tests the distance_between_points function with various test cases.
def test_distance_between_points():
    assert distance_between_points(0, 0, 3, 4) == 5.0
    assert distance_between_points(1, 5, 4, 1) == 5.0
    assert distance_between_points(-1, -1, 2, 3) == 5.0
    assert distance_between_points(0, 0, 0, 0) == 0.0
    assert distance_between_points(1, 1, 1, 1) == 0.0
    assert distance_between_points(1, 1, 4, 5) == 5.0

    print("All tests passed!")


# Call the test_distance_between_points function to run the tests.
test_distance_between_points()
