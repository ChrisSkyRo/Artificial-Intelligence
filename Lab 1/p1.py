# This function takes a string input and returns the longest word in the string.
# If the input string is empty or contains only whitespace, it returns None.
def find_max_word(input_string):
    # Split the input string into a list of words by whitespace.
    words = input_string.strip().split()

    # Check if the words list is not empty.
    if words:
        # Return the maximum word in the list, which is determined by the default alphabetical ordering of strings.
        return max(words)
    else:
        # If the words list is empty, return None.
        return None


# This function tests the find_max_word() function with various test cases.
# Each test case consists of an input string and the expected output (the longest word in the string).
def test_find_max_word():
    test_cases = [
        ("", None),
        ("   ", None),
        ("hello world", "world"),
        ("the quick brown fox jumps over the lazy dog", "the"),
        ("alpha beta gamma delta epsilon", "gamma"),
        ("Ana are mere rosii si galbene", "si")
    ]
    # Iterate over each test case and assert that the find_max_word() function returns the expected output.
    for input_str, expected_output in test_cases:
        assert find_max_word(input_str) == expected_output


# Call the test_find_max_word() function to run the tests.
test_find_max_word()