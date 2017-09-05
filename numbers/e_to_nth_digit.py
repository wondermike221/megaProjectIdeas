"""
Outputs e to the given digit.
Defaults to 50 digits
"""
import math

def e_to_nth_digit(digit=50):
    digit = int(digit)
    if digit > 200:
        digit = 200
    return sum(1 / float(math.factorial(i)) for i in range(digit))

if __name__ == "__main__":
    import sys
    print(e_to_nth_digit(sys.argv[1]))
