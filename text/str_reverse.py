"""Reverses a string"""

def str_reverse(string):
    """Takes a string and reverses it"""
    return string[::-1]

if __name__ == "__main__":
    import sys
    print(str_reverse(sys.argv[1]))
