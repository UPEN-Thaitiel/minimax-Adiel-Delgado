# number of rows and number of columns
BOARD_SIZE = 3
# this is the reward of winning a game
REWARD = 10


class TicTacToe:

    def __init__(self, board):
        self.board = board
        self.player = 'O'
        self.computer = 'X'

    def run(self):
        print("Computer starts...")

        while True:
            self.move_computer()
            self.move_player()

    def print_board(self):
        # Adjusted spacing to be a bit more consistent
        print(self.board[1] + ' | ' + self.board[2] + ' | ' + self.board[3])
        print('--+---+--')
        print(self.board[4] + ' | ' + self.board[5] + ' | ' + self.board[6])
        print('--+---+--')
        print(self.board[7] + ' | ' + self.board[8] + ' | ' + self.board[9])
        print('\n')

    def is_cell_free(self, position):
        if self.board[position] == ' ':
            return True
        return False

    def update_player_position(self, player, position):
        if self.is_cell_free(position):
            self.board[position] = player
            self.check_game_state()
        else:
            print("Can't insert there!")
            # This recursive call might lead to deep recursion on many errors.
            # A loop in move_player for input is often preferred.
            self.move_player()

    def check_game_state(self):
        self.print_board() # Print board first

        # It's generally better to check for win before draw
        if self.is_winning(self.player):
            print("Player wins!")
            exit()

        if self.is_winning(self.computer):
            print("Computer wins!")
            exit()

        if self.is_draw(): # Only a draw if no one has won and board is full
            print("Draw!")
            exit()


    def is_winning(self, player):
        # checking the diagonals (top left to bottom right)
        if self.board[1] == player and self.board[5] == player and self.board[9] == player:
            return True
        # checking the diagonals (top right to bottom left)
        if self.board[3] == player and self.board[5] == player and self.board[7] == player:
            return True

        # checking the rows and columns
        for i in range(BOARD_SIZE):
            # Rows
            if self.board[3*i+1] == player and self.board[3*i+2] == player and self.board[3*i+3] == player:
                return True
            # Columns
            if self.board[i+1] == player and self.board[i+4] == player and self.board[i+7] == player:
                return True
        return False

    def is_draw(self):
        # CORRECTED: Use self.board here
        for key in self.board.keys():
            if self.board[key] == ' ':
                return False
        return True

    def move_player(self):
        # Basic input validation, can be made more robust
        while True:
            try:
                position = int(input(f"Enter the position for '{self.player}' (1-9): "))
                if 1 <= position <= 9:
                    # update_player_position will handle if cell is free or not
                    # and will call self.move_player() again if not free.
                    self.update_player_position(self.player, position)
                    break # Exit loop if input is a valid number and position
                else:
                    print("Position must be between 1 and 9.")
            except ValueError:
                print("Invalid input. Please enter a number.")


    def move_computer(self):
        best_score = -float('inf')
        best_move = 0 # Initialize best_move

        # Check if there are any possible moves for the computer
        possible_moves = [pos for pos in self.board.keys() if self.is_cell_free(pos)]
        if not possible_moves:
            self.check_game_state() # Board is full or game already ended
            return

        # CORRECTED: Iterate over self.board.keys()
        for position in self.board.keys():
            if self.is_cell_free(position): # Ensure we only consider empty cells
                self.board[position] = self.computer
                # MODIFIED: Call minimax with the new signature (depth, is_maximizer)
                # is_maximizer is False because after computer's move, it's player's (minimizer's) turn
                score = self.minimax(0, False)
                # CORRECTED: Undo move on self.board
                self.board[position] = ' '

                if score > best_score:
                    best_score = score
                    best_move = position
        
        # If best_move is still 0 but there were possible moves, it implies all moves might be equally bad (e.g. leading to a loss)
        # or the first valid move is taken if all scores are -infinity (which shouldn't happen if draws are 0)
        # For a perfect AI, it will pick one. If no move improves score (e.g. all lead to loss), it will pick one of those.
        # If all cells were initially evaluated and best_move wasn't updated, pick the first possible one.
        if best_move == 0 and possible_moves: # Fallback if no move had a score > -inf (e.g. all lead to immediate loss)
            best_move = possible_moves[0]

        if best_move != 0: # Ensure a valid move was determined
            self.board[best_move] = self.computer
        
        self.check_game_state()


    def minimax(self, depth, is_maximizer):
        # - If computer wins, return positive score (REWARD - depth)
        if self.is_winning(self.computer):
            return REWARD - depth
        # - If player wins, return negative score (-REWARD + depth)
        if self.is_winning(self.player):
            return -REWARD + depth
        # - If draw, return 0
        if self.is_draw():
            return 0

        # - If maximizing (computer's turn), try to maximize score over all possible moves
        if is_maximizer:
            best_score = -float('inf')
            for position in self.board.keys():
                if self.is_cell_free(position):
                    self.board[position] = self.computer  # Make the move
                    score = self.minimax(depth + 1, False) # Recursive call for minimizer
                    self.board[position] = ' '           # Undo the move
                    best_score = max(score, best_score)
            return best_score
        # - If minimizing (player's turn), try to minimize score over all possible moves
        else: # Minimizer's turn
            best_score = float('inf')
            for position in self.board.keys():
                if self.is_cell_free(position):
                    self.board[position] = self.player   # Make the move
                    score = self.minimax(depth + 1, True)  # Recursive call for maximizer
                    self.board[position] = ' '           # Undo the move
                    best_score = min(score, best_score)
            return best_score

if __name__ == '__main__':
    board = {1: ' ', 2: ' ', 3: ' ',
             4: ' ', 5: ' ', 6: ' ',
             7: ' ', 8: ' ', 9: ' '}

    game = TicTacToe(board)
    game.run()