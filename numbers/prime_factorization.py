"""Finds all the prime factors of the given number"""
import math

def prime_factors(number):
    factors = []
    while number & 1 == 0:
        factors.append(2)
        factors.append(number)
        number = number/2
    for i in range(3, int(math.sqrt(number))+1, 2):
        while number % i == 0:
            factors.append(i)
            factors.append(number)
            number = number/i
    if number > 2:
        factors.append(number)
    factors.sort()
    return factors

if __name__ == "__main__":
    import sys
    print(prime_factors(int(sys.argv[1])))
