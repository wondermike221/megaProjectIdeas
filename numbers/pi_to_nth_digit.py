"""Calculates pi to the given digit"""

from decimal import Decimal, getcontext

def pi_to_nth_digit(digits):
    """
    Returns pi to the nth digit, limited to 100 digits
    *Note rounds last digit up
    """
    digits = int(digits)
    if digits > 100:
        digits = 100
    getcontext().prec=digits
    pi_to_n = sum(1/Decimal(16)**k *
        (Decimal(4)/(8*k+1) -
        Decimal(2)/(8*k+4) -
        Decimal(1)/(8*k+5) -
        Decimal(1)/(8*k+6)) for k in range(100))
    return pi_to_n




if __name__ == "__main__":
    import sys
    print(pi_to_nth_digit(sys.argv[1]))
