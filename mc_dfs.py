# Generate valid moves for a given state
def get_possible_moves(state):
    left_missionaries, left_cannibals, right_missionaries, right_cannibals, boat_position = state
    possible_moves = []

    # Possible transitions
    transitions = [
        (1, 0),  # One missionary
        (2, 0),  # Two missionaries
        (0, 1),  # One cannibal
        (0, 2),  # Two cannibals
        (1, 1),  # One missionary and one cannibal
    ]

    # Generate new states based on valid transitions
    for transition in transitions:
        m, c = transition  # Missionaries and cannibals to move
        if boat_position == 'left':
            new_left_m = left_missionaries - m
            new_left_c = left_cannibals - c
            new_right_m = right_missionaries + m
            new_right_c = right_cannibals + c
            new_boat_position = 'right'
        else:
            new_left_m = left_missionaries + m
            new_left_c = left_cannibals + c
            new_right_m = right_missionaries - m
            new_right_c = right_cannibals - c
            new_boat_position = 'left'

        # Validate the new state
        if (
            new_left_m >= 0
            and new_left_c >= 0
            and new_right_m >= 0
            and new_right_c >= 0
            and (new_left_m == 0 or new_left_m >= new_left_c)
            and (new_right_m == 0 or new_right_m >= new_right_c)
        ):
            possible_moves.append(
                (
                    new_left_m,
                    new_left_c,
                    new_right_m,
                    new_right_c,
                    new_boat_position,
                )
            )

    return possible_moves

# Depth-First Search (DFS) with backtracking
def dfs(state, goal, path, visited):
    if state == goal:
        return path  # Goal state found

    visited.add(state)  # Mark the current state as visited

    # Explore possible moves
    for new_state in get_possible_moves(state):
        if new_state not in visited:
            new_path = path + [new_state]
            result = dfs(new_state, goal, new_path, visited)
            if result:
                return result  # Solution found

    return None  # No solution found

# Example usage
if __name__ == "__main__":
    start_state = (3, 3, 0, 0, 'left')  # All on the left
    goal_state = (0, 0, 3, 3, 'right')  # All on the right

    visited = set()  # Set to track visited states
    path = [start_state]

    # Use DFS to solve the problem
    solution = dfs(start_state, goal_state, path, visited)

    if solution:
        print("Depth-First Search Solution:")
        for step, state in enumerate(solution):
            print(f"Step {step}: {state}")
    else:
        print("No solution found.")