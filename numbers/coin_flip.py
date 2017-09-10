"""flips coins and keeps track of stats"""

import random

class CoinFlip:
    stats = {}

    def __init__(self):
        self.stats['heads'] = 0
        self.stats['tails'] = 0
        user_input = 'f'
        self.menu()
        while user_input:
            if user_input == 'q':
                break
            if user_input == 'f':
                self.flip()
            if user_input == 's':
                print(self.stats)
            if user_input == '' or user_input is None:
                continue
            if user_input == 'm':
                self.menu()
            user_input = input('What next?: ')

    def flip(self):
        if random.randint(0, 1):
            print("Heads!")
            self.stats['heads'] += 1
        else:
            print("Tails!")
            self.stats['tails'] += 1

    def menu(self):
        print("'q' to quit\n'f' to flip\n's' to show stats\n'm' to show menu")
    

if __name__ == "__main__":
    flipper = CoinFlip()
