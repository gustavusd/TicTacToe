from Board import Board
from Player import Player
from AI import AI


# As a precondition you must enter valid moves
def main():
    board = Board([[]])
    board.new_game()
    player = Player(board.game_state)
    ai = AI(board.game_state)
    board.who_start = input("Enter x: ")
    board.display_board()
    while board.check_winner() == '-' or board.movesLeft():
        if board.who_start == 'x':
            player.move(int(input("Enter the desired row location: ")), int(input("Enter the desired column location:"
                                                                                  " ")))
            ai.move()
            board.display_board()
        else:
            ai.move()
            player.move(int(input("Enter the desired row location: ")), int(input("Enter the desired column location:"
                                                                                  " ")))
            board.display_board()
    board.display_board()


main()
