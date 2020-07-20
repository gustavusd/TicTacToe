from Board import Board


class AI(Board):
    def __init__(self, game_state):
        super(AI, self).__init__(game_state)

    def move(self):
        move = self.best_move()
        self.game_state[move[0]][move[1]] = 'o'

    def best_move(self):
        best = -1000
        curr = 0
        move = [-1] * 2

        for i in range(3):
            for j in range(3):
                if self.game_state[i][j] == '-':
                    self.game_state[i][j] = 'o'
                    curr = self.minimax(0, False)
                    self.game_state[i][j] = '-'
                    if curr > best:
                        best = curr
                        move[0] = i
                        move[1] = j
        return move

    def minimax(self, depth, isMax):
        score = 0
        if self.check_winner() == 'o':
            score += 10
            return score
        if self.check_winner() == 'x':
            score -= 10
            return score
        if not self.movesLeft():
            return 0

        if isMax:
            bestVal = -1000
            for a in range(3):
                for b in range(3):
                    if self.game_state[a][b] == '-':
                        self.game_state[a][b] = 'o'
                        bestVal = max(bestVal, self.minimax(depth + 1, not isMax))
                        self.game_state[a][b] = '-'
            return bestVal
        else:
            bestVal = 1000
            for a in range(3):
                for b in range(3):
                    if self.game_state[a][b] == '-':
                        self.game_state[a][b] = 'x'
                        bestVal = min(bestVal, self.minimax(depth + 1, not isMax))
                        self.game_state[a][b] = '-'
            return bestVal
