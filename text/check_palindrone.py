"""Palindrome checker"""

from str_reverse import str_reverse

def check_palindrome(string):
    """Returns true if string has palindrome, false otherwise."""
    if string == str_reverse(string):
        return True
    else:
        return False

if __name__ == "__main__":
    import sys
    if check_palindrome(sys.argv[1]):
        print("True")
    else:
        print("False")
