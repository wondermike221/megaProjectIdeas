"""Counts words"""

def count_words(string):
    """Returns the # of words in a particular string"""
    words = string.split(' ')
    filtered_words = [x for x in words if x != '']
    return len(filtered_words)


if __name__ == "__main__":
    import sys
    print(count_words(sys.argv[1]))
