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
        print(self.board[1] + '  | ' + self.board[2] + '  | ' + self.board[3])
        print('---+----+---')
        print(self.board[4] + '  | ' + self.board[5] + '  | ' + self.board[6])
        print('---+----+---')
        print(self.board[7] + '  | ' + self.board[8] + '  | ' + self.board[9])
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
            self.move_player()

    def check_game_state(self):
        self.print_board()

        if self.is_draw():
            print("Draw!")
            exit()

        if self.is_winning(self.player):
            print("Player wins!")
            exit()

        if self.is_winning(self.computer):
            print("Computer wins!")
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
            if self.board[3*i+1] == player and self.board[3*i+2] == player and self.board[3*i+3] == player:
                return True

            if self.board[i+1] == player and self.board[i+4] == player and self.board[i+7] == player:
                return True

        return False

    def is_draw(self):
        for key in board.keys():
            if self.board[key] == ' ':
                return False

        return True

    def move_player(self):
        position = int(input("Enter the position for 'O':  "))
        self.update_player_position(self.player, position)

    def move_computer(self):
        best_score = -float('inf')
        # best position (best next move) for the computer
        best_move = 0

        # the computer considers all the empty cells on the board and calculates the
        # minimax score (10, -10 or 0)
        for position in board.keys():
            if self.board[position] == ' ':
                self.board[position] = self.computer
                score = self.minimax(0, -float('inf'), float('inf'), False)
                board[position] = ' '

                if score > best_score:
                    best_score = score
                    best_move = position

        # make the next move according to the minimax algorithm result
        self.board[best_move] = self.computer
        self.check_game_state()


    def minimax(self, depth, alpha, beta, is_maximizer):
        # Recursive Minimax algorithm with alpha-beta pruning:
        # Base cases:
        #  - If computer has won, return REWARD - depth (prefer faster wins)
        if self.is_winning(self.computer):
            return REWARD - depth
        #  - If player has won, return -REWARD + depth (prefer slower losses)
        if self.is_winning(self.player):
            return -REWARD + depth
        #  - If draw, return 0
        if self.is_draw():
            return 0
        
        # Recursive step:
        #  - If is_maximizer (computer's turn):
        if is_maximizer:
            #   * Initialize best_score = -infinity
            best_score = -float('inf')
            #   * For each free cell:
            for position in self.board.keys():
                if self.is_cell_free(position):
                    #       - Place computer's mark temporarily
                    self.board[position] = self.computer
                    #       - Call minimax(depth+1, alpha, beta, False)
                    score = self.minimax(depth + 1, alpha, beta, False)
                    #       - Undo move
                    self.board[position] = ' '
                    #       - Update best_score with max(score, best_score)
                    best_score = max(score, best_score)
                    #       - Update alpha = max(alpha, best_score)
                    alpha = max(alpha, best_score)
                    #       - If alpha >= beta, prune remaining branches (break)
                    if alpha >= beta:
                        break
            #   * Return best_score
            return best_score
        #
        #  - Else (player's turn):
        else:
            #   * Initialize best_score = +infinity
            best_score = float('inf')
            #   * For each free cell:
            for position in self.board.keys():
                if self.is_cell_free(position):
                    #       - Place player's mark temporarily
                    self.board[position] = self.player
                    #       - Call minimax(depth+1, alpha, beta, True)
                    score = self.minimax(depth + 1, alpha, beta, True)
                    #       - Undo move
                    self.board[position] = ' '
                    #       - Update best_score with min(score, best_score)
                    best_score = min(score, best_score)
                    #       - Update beta = min(beta, best_score)
                    beta = min(beta, best_score)
                    #       - If alpha >= beta, prune remaining branches (break)
                    if alpha >= beta:
                        break
            #   * Return best_score
            return best_score

if __name__ == '__main__':
    board = {1: ' ', 2: ' ', 3: ' ',
             4: ' ', 5: ' ', 6: ' ',
             7: ' ', 8: ' ', 9: ' '}

    game = TicTacToe(board)
    game.run()