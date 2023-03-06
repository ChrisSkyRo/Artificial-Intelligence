def get_non_repeated_words(input_string):
    """
    Returns a list of words that occur only once in the input string.

    Args:
    input_string: A string containing words separated by whitespace.

    Returns:
    A list of words that occur only once in the input string.
    """
    word_freq = {}
    for word in input_string.split():
        if word in word_freq:
            word_freq[word] += 1
        else:
            word_freq[word] = 1

    non_repeated_words = [word for word, freq in word_freq.items() if freq == 1]

    return non_repeated_words


def test_get_non_repeated_words():
    assert get_non_repeated_words("The quick brown fox jumps over the lazy dog") \
           == ["The", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog"]
    assert get_non_repeated_words("hello world") == ["hello", "world"]
    assert get_non_repeated_words("a a b b c c") == []
    assert get_non_repeated_words("this is a sentence with words that don't repeat") \
           == ["this", "is", "a", "sentence", "with", "words", "that", "don't", "repeat"]
    assert get_non_repeated_words("  ") == []
    assert get_non_repeated_words("") == []
    assert get_non_repeated_words("ana are ana are mere rosii ana") == ["mere", "rosii"]

    print("All tests passed!")


test_get_non_repeated_words()
