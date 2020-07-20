from Board import Board


class Player(Board):
    def __init__(self, game_state):
        super(Player, self).__init__(game_state)

    def move(self, row, column):
        self.game_state[row][column] = 'x'