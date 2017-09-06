"""Finds all the prime factors of the given number"""
import math

def prime_factors(number):
    factors = []
    while int(number) & int(1) == 0:
        factors.append(2)
        factors.append(number)
        number = int(number/2)
    for i in range(3, int(math.sqrt(number))+1, 2):
        while int(number) % int(i) == 0:
            factors.append(int(i))
            factors.append(number)
            number = int(number/i)
    if number > 2:
        factors.append(number)
    factors.sort()
    return factors

if __name__ == "__main__":
    import sys
    print(prime_factors(int(sys.argv[1])))
