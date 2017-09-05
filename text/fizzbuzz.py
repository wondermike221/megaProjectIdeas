"""Fizzbuzz solution"""

def fizzbuzz(up_to):
    up_to = int(up_to)
    if up_to > 200:
        up_to = 200
    for i in range(up_to + 1):
        print(get_type(i))

def get_type(i):
    if i % 3 == 0 and i % 5 == 0:
        return "FizzBuzz"
    elif i % 5 == 0:
        return "Buzz"
    elif i % 3 == 0:
        return "Fizz"
    else:
        return i

if __name__ == "__main__":
    import sys
    fizzbuzz(sys.argv[1])
