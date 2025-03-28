# Author: Damian Zukowski

import random

class Coin():
    def __init__(self):
        self.sideup = "Heads"


    def toss_the_coin(self):

        chance = random.randint(0, 1000)

        if chance > 0 and chance <= 450:            # chance 45:100
            self.sideup = "Heads"
        elif chance > 450 and chance <= 900:        # chance 45:100
            self.sideup = "Tails"
        elif chance > 900 and chance <= 950:        # chance 5:100
            self.sideup = "The coin is upright!"
        elif chance > 950 and chance <= 980:        # chance 3:100
            self.sideup = "The coin dropped on the ground and disappeared in the rabbit hole!"
        else:                                       # chance 2:100
            self.sideup = "The coin defied gravity and got lost in a wormhole!"


    def get_sideup(self):
        return self.sideup
    

def main():
    my_coin = Coin()

    print("This side is up: ", my_coin.get_sideup())

    print("Tossing the coin..")
    my_coin.toss_the_coin()

    print("The outcome: ", my_coin.get_sideup())


main()
