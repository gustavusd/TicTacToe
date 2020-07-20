class Board:
    def __init__(self, game_state):
        self.game_state = game_state
        self.who_start = ""

    def new_game(self):
        _list = [['-'] * 3 for i in range(3)]
        self.game_state = _list

    def display_board(self):
        print(self.game_state[0])
        print(self.game_state[1])
        print(self.game_state[2])
        print('------------------------------------------')

    def check_winner(self):
        for i in range(3):
            if self.game_state[i][0] == 'x' and self.game_state[i][1] == 'x' and self.game_state[i][2] == 'x':
                return 'x'
            if self.game_state[i][0] == 'o' and self.game_state[i][1] == 'o' and self.game_state[i][2] == 'o':
                return 'o'
            if self.game_state[0][i] == 'x' and self.game_state[1][i] == 'x' and self.game_state[2][i] == 'x':
                return 'x'
            if self.game_state[0][i] == 'o' and self.game_state[1][i] == 'o' and self.game_state[2][i] == 'o':
                return 'o'
        if self.game_state[0][0] == 'x' and self.game_state[1][1] == 'x' and self.game_state[2][2] == 'x':
            return 'x'
        if self.game_state[0][0] == 'o' and self.game_state[1][1] == 'o' and self.game_state[2][2] == 'o':
            return 'o'
        if self.game_state[0][2] == 'x' and self.game_state[1][1] == 'x' and self.game_state[2][0] == 'x':
            return 'x'
        if self.game_state[0][2] == 'o' and self.game_state[1][1] == 'o' and self.game_state[2][0] == 'o':
            return 'o'
        return '-'

    def movesLeft(self):
        for i in range(3):
            for j in range(3):
                if self.game_state[i][j] == '-':
                    return True
        return False
