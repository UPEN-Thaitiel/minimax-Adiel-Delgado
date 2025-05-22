BOARD_SIZE = 3
REWARD = 10

class TicTacToe:
    def __init__(self, board):
        # Challenge 1: Initialize the board as a dictionary with keys 1-9 all set to ' '
        # Set player symbol to 'O' and computer symbol to 'X'
        self.board = board
        self.player = 'O'
        self.computer = 'X'

    def run(self):
        # Challenge 11: Create the main game loop
        # - Computer starts first
        # - Alternate between computer and player moves
        # - After each move, check if the game has ended (win or draw)
        # - If game ended, exit the loop and print result
        pass

    def print_board(self):
        # Challenge 2: Print the board in 3 rows and 3 columns
        # For example:
        # X | O |  
        # --+---+--
        #   | X | O
        # --+---+--
        # O |   | X
        print(self.board[1] +'|'+ self.board[2] + '|' + self.board[3])
        print('--+--+--')
        print(self.board[4] +'|'+ self.board[5] + '|' + self.board[6])
        print('--+--+--')
        print(self.board[7] +'|'+ self.board[8] + '|' + self.board[9])
        print('--+--+--')
        print('\n')
        pass

    def is_cell_free(self, position):
        # Challenge 3: Return True if the cell at 'position' is empty (' ')
        # Otherwise, return False
        if self.board == ' ':
            return True
        return False
        pass

    def update_player_position(self, player, position):
        # Challenge 4: If the cell at 'position' is free, place 'player' symbol there
        # If the cell is occupied, print an error and ask the player to input again
        # After updating the board, check if the game ended (win or draw)
        if self.is_cell_free(position):
            self.board(position) = player
        else:
            print("ERROR: Cannot Insert Here!")
            self.move_player
        pass

    def is_winning(self, player):
        # Challenge 5: Check if 'player' has 3 in a row horizontally, vertically, or diagonally
        # Return True if winning condition met, False otherwise
        pass

    def is_draw(self):
        # Challenge 6: Return True if no empty cells remain on the board (all positions filled)
        # and no player has won
        pass

    def check_game_state(self):
        # Challenge 7: Print the board and check if the game ended
        # If player or computer won, print the winner and exit
        # If draw, print 'Draw!' and exit
        pass

    def move_player(self):
        # Challenge 8: Ask the human player to enter a position (1-9)
        # Validate input is an integer within range and the cell is free
        # Update the board with player's move
        pass

    def move_computer(self):
        # Challenge 9: Iterate over all free cells on the board
        # For each cell, simulate placing computer's symbol and calculate minimax score
        # Choose the cell with the highest minimax score and place the computer's symbol there
        # After the move, check if the game ended
        pass

    def minimax(self, depth, is_maximizer):
        # Challenge 10: Implement recursive minimax algorithm:
        # - If computer wins, return positive score (REWARD - depth)
        # - If player wins, return negative score (-REWARD + depth)
        # - If draw, return 0
        # - If maximizing (computer's turn), try to maximize score over all possible moves
        # - If minimizing (player's turn), try to minimize score over all possible moves
        pass


if __name__ == '__main__':
    # Challenge 1: Initialize empty board dictionary with keys 1 to 9 set to ' '
    board = {pos: ' ' for pos in range(1, 10)}

    game = TicTacToe(board)
    # Challenge 11: Start the game loop
    game.run()
