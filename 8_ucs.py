import heapq

# Define the goal state
goal_state = tuple(range(1, 9)) + (0,)

# Define a function to find the possible moves from a given state
def find_moves(state):
    moves = []
    empty_idx = state.index(0)
    if empty_idx not in [0, 1, 2]:  # Up
        new_state = list(state)
        new_state[empty_idx], new_state[empty_idx - 3] = new_state[empty_idx - 3], new_state[empty_idx]
        moves.append((tuple(new_state), "Up"))
    if empty_idx not in [0, 3, 6]:  # Left
        new_state = list(state)
        new_state[empty_idx], new_state[empty_idx - 1] = new_state[empty_idx - 1], new_state[empty_idx]
        moves.append((tuple(new_state), "Left"))
    if empty_idx not in [2, 5, 8]:  # Right
        new_state = list(state)
        new_state[empty_idx], new_state[empty_idx + 1] = new_state[empty_idx + 1], new_state[empty_idx]
        moves.append((tuple(new_state), "Right"))
    if empty_idx not in [6, 7, 8]:  # Down
        new_state = list(state)
        new_state[empty_idx], new_state[empty_idx + 3] = new_state[empty_idx + 3], new_state[empty_idx]
        moves.append((tuple(new_state), "Down"))
    return moves

# Define a function to calculate the cost of a move
def move_cost(state1, state2):
    return 1  # Uniform cost for each move

# Uniform Cost Search algorithm
def uniform_cost_search(initial_state):
    frontier = [(0, initial_state, [])]  # Priority queue sorted by path cost
    explored = set()  # Set to keep track of explored states

    while frontier:
        path_cost, current_state, path = heapq.heappop(frontier)
        if current_state == goal_state:
            return path

        explored.add(current_state)

        for move, move_dir in find_moves(current_state):
            if move not in explored:
                new_cost = path_cost + move_cost(current_state, move)
                new_path = path + [(move_dir, move)]
                heapq.heappush(frontier, (new_cost, move, new_path))

    return None  # No solution found

# Function to print state
def print_state(state):
    for i in range(3):
        print(state[i * 3:i * 3 + 3])

# Example usage
if __name__ == "__main__":
    initial_state = (1, 2, 3, 0, 4, 6, 7, 5, 8)  # Example initial state
    solution = uniform_cost_search(initial_state)
    if solution:
        print("Start State:")
        print_state(initial_state)
        step_count = 0
        for step, (direction, state) in enumerate(solution, 1):
            step_count += 1
            print("\nStep", step_count, ":", direction)
            print_state(state)
        print("\nCost to solve the Eight Puzzle Problem:", len(solution))
    else:
        print("No solution found.")