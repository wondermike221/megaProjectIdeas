"""Vowel Count"""

def vowel_count(string):
    """Returns a dict where each vowel in the alphabet exists as a key and contains the count of the vowels"""
    vowels = ('a', 'e', 'i', 'o', 'u', 'y')
    vowels_count = {'a':0, 'e':0, 'i':0, 'o':0, 'u':0, 'y':0}
    for x in string:
        if x in vowels:
            vowels_count[x] += 1
    return vowels_count

if __name__ == "__main__":
    import sys
    print(vowel_count(sys.argv[1]))
