from dice import Dice

class Player:
    def __init__(self):
        self.pos = 0
        self.dice = Dice()

    def __next__(self,):
        self.pos += self.roll()
