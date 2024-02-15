from snake import Snake
snake_locations = [(98,74),(26,14),(57,31),(88,58),(76,43)]

class Board:
    def __init__(self):
        self.board = [[None for _ in range(10)] for _ in range(10)]
        self.snakes = []

    def set_snakes(self):
        for sl in snake_locations:
            self.snakes.append(Snake(*sl))
        
        while self.snakes:
            s = self.snakes.pop()
            l = s.get_source()
            row, col = l//10, l%10
            self.board[row][col] = s

        