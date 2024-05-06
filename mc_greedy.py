import heapq
import random

# Calculate a heuristic based on how many people are left to cross
def heuristic(state):
    left_missionaries, left_cannibals, right_missionaries, right_cannibals, boat_position = state
    return left_missionaries + left_cannibals  # Total people left on the left side

# Function to generate possible moves and resulting new states
def get_possible_moves(state):
    left_missionaries, left_cannibals, right_missionaries, right_cannibals, boat_position = state
    possible_moves = []

    # Define possible transitions for moves
    transitions = [
        (1, 0),  # One missionary
        (2, 0),  # Two missionaries
        (0, 1),  # One cannibal
        (0, 2),  # Two cannibals
        (1, 1),  # One missionary and one cannibal
    ]

    # Generate the new states based on valid transitions
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

        # Ensure the move doesn't lead to cannibals outnumbering missionaries
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

# Greedy Best-First Search (GBFS) for solving the Missionaries and Cannibals problem
def gbfs(start, goal):
    # Priority queue for GBFS with the heuristic cost
    queue = []
    heapq.heappush(queue, (heuristic(start), start, []))  # (heuristic, state, path)

    visited = set()  # To track visited states to avoid cycles

    while queue:
        _, current_state, path = heapq.heappop(queue)

        if current_state == goal:
            return path  # Solution found

        if current_state not in visited:
            visited.add(current_state)

            # Explore possible moves from the current state
            for new_state in get_possible_moves(current_state):
                if new_state not in visited:
                    new_path = path + [new_state]
                    heapq.heappush(queue, (heuristic(new_state), new_state, new_path))

    return None  # No solution found

# Example usage
if __name__ == "__main__":
    # Starting state with all on the left side
    start_state = (3, 3, 0, 0, 'left')
    # Goal state with all on the right side
    goal_state = (0, 0, 3, 3, 'right')

    # Solve the Missionaries and Cannibals problem using GBFS
    solution = gbfs(start_state, goal_state)

    if solution:
        print("Greedy Best-First Search Solution:")
        for step, state in enumerate(solution):
            print(f"Step {step}: {state}")
    else:
        print("No solution found.")