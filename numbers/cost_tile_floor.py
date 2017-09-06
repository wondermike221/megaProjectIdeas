""" Enter price per square foot and the width and length of floor to get full price"""

def find_tiling_price():
    price_per_foot = float(input("Enter the price per square foot: "))
    width = int(input("Enter the width of the floor plan: "))
    length = int(input("Enter the length of the floor plan: "))
    square_footage = width * length
    price = square_footage * price_per_foot
    print("The price to tile your floor is ${:.2f}".format(price))

if __name__ == "__main__":
    find_tiling_price()
