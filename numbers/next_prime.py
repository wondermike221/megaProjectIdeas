"""
Will print out the next prime number and wait for input.
"""

def next_prime():
    user_input = 'Y'
    prime = 1
    while user_input != 'n' and user_input != 'N':
        user_input = input('Another? (Y/N): ')
        prime += 1
        while not is_prime(prime):
            prime += 1
        print(prime)

def is_prime(x):
    if x < 2:
        return False
    for i in range(2, x):
        if x % i == 0:
            return False
    return True

if __name__ == "__main__":
    next_prime()
