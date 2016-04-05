"""
Monte Carlo Tic-Tac-Toe Player
"""

import random
import poc_ttt_gui
import poc_ttt_provided as provided

# Constants for Monte Carlo simulator
# You may change the values of these constants as desired, but
#  do not change their names.
NTRIALS = 1         # Number of trials to run
SCORE_CURRENT = 1.0 # Score for squares played by the current player
SCORE_OTHER = 1.0   # Score for squares played by the other player
     

def mc_trial(board, player):
    """
    This function takes a current board and the next player to move.
    The function should play a game starting with the given player 
    by making random moves, alternating between players
    """
    
    while board.check_win() == None:        
        empty_moves = board.get_empty_squares()
        random_move = random.choice(empty_moves)
        board.move(random_move[0], random_move[1], player)
        player = provided.switch_player(player)
        if board.check_win() != None:
            break
        
def mc_update_scores(scores, board, player):
    """
    Updates the scores
    """
    board_dim = range(board.get_dim())
    for row in board_dim:
        for col in board_dim:
            square = board.square(row, col)
            if board.check_win() == player:
                if square == player:
                    scores[row][col] += SCORE_CURRENT
                elif square == provided.EMPTY:
                    scores[row][col] += 0
                else:
                    scores[row][col] -= SCORE_OTHER
    
            elif board.check_win() == provided.DRAW:
                scores[row][col] += 0
                    
            elif board.check_win() == provided.switch_player(player):
                square = board.square(row, col)
                if square == player:
                    scores[row][col] -= SCORE_CURRENT
                elif square == provided.EMPTY:
                    scores[row][col] += 0
                else:
                    scores[row][col] += SCORE_OTHER
            
        
def get_best_move(board, scores):
    """
    Assigned highest score as best move
    """

    grid_value = {}
    empty_squares = board.get_empty_squares()
    best_scores = []
    
    for square in empty_squares:
        grid_value[square]=scores[square[0]][square[1]]
    
    for value in grid_value:          
        if grid_value[value] == max(grid_value.values()):
            best_scores.append(value)
            
    if len(best_scores)>0:
        return random.choice(best_scores)
            
 
def mc_move(board, player, trials):
    """
    Uses mc_trial, mc_update    
    make a move base on get_best_move
    """
  
    
    scores = [[0 for dummy_col in range(board.get_dim())] for dummy_row in range(board.get_dim())]
    for dummy_index in range(trials):
        shine = board.clone()
        mc_trial(shine, player)
        mc_update_scores(scores, shine, player)
    return get_best_move(board, scores)

# Test game with the console or the GUI.  Uncomment whichever 
# you prefer.  Both should be commented out when you submit 
# for testing to save time.

provided.play_game(mc_move, NTRIALS, False)        
poc_ttt_gui.run_gui(3, provided.PLAYERX, mc_move, NTRIALS, False)