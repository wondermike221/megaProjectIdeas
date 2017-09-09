"""converts binary to decimal and vice versa"""

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description='Convert numbers from binary to decimal and vice versa')
    parser.add_argument('number')
    parser.add_argument('-bin', '--bin', action='store_true', help='change from binary to decimal (default: from decimal to binary')
    args = parser.parse_args()
    if args.bin:
        print(int(args.number, 2))
    else:
        print("{0:b}".format(int(args.number)))
