import random

def conflicts(board, row, col):
    """
    Calculate the number of conflicts for a queen placed at a given position.
    """
    count = 0
    for i in range(len(board)):
        if i != row:
            if board[i] == col or abs(i - row) == abs(board[i] - col):
                count += 1
    return count

def evaluate(board):
    """
    Evaluate the total number of conflicts in the current board state.
    """
    total_conflicts = 0
    for row in range(len(board)):
        total_conflicts += conflicts(board, row, board[row])
    return total_conflicts

def random_board(size):
    """
    Generate a random initial board state.
    """
    return [random.randint(0, size-1) for _ in range(size)]

def local_search(size, max_iter=1000):
    """
    Local search algorithm to solve the N-Queens problem.
    """
    board = random_board(size)
    for _ in range(max_iter):
        current_conflicts = evaluate(board)
        if current_conflicts == 0:
            return board  # Solution found
        # Select a queen with conflicts
        row = random.randint(0, size-1)
        col = board[row]
        current_conflicts -= conflicts(board, row, col)
        min_conflicts = float('inf')
        best_move = col
        for new_col in range(size):
            if new_col != col:
                new_conflicts = conflicts(board, row, new_col)
                if new_conflicts < min_conflicts:
                    min_conflicts = new_conflicts
                    best_move = new_col
        if min_conflicts < current_conflicts:
            board[row] = best_move
    return None  # No solution found within max_iter

# Example usage
size = 8  # Change this to desired board size
solution = local_search(size)
if solution:
    print("Solution found:")
    for row in solution:
        print(" . " * row + " Q " + " . " * (size - row - 1))
else:
    print("No solution found within maximum iterations.")