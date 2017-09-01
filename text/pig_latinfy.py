"""Returns a pig latin version of a string given"""

def pig_latinfy(string):
    """pig-latin version of string"""
    pig_latin_modifier = "ay"
    first_letter = string[0]
    rest = string[1:]
    return "{}-{}{}".format(rest, first_letter, pig_latin_modifier)


if __name__ == "__main__":
    import sys
    print pig_latinfy(sys.argv[1])
