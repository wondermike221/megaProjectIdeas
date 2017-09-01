"""Vowel Count"""

def vowel_count(string):
    #TODO
    return string

def _output_vowel_stats(string):
    vowel_stats = vowel_count(string)
    print vowel_stats
    #TODO

if __name__ == "__main__":
    import sys
    _output_vowel_stats(sys.argv[1])
