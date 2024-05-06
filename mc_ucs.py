import heapq

# Generate valid moves from a given state
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

    # Generate new states from valid moves
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

# Uniform Cost Search (UCS) for solving the Missionaries and Cannibals problem
def ucs(start, goal):
    # Priority queue to track states by cost
    queue = []
    heapq.heappush(queue, (0, start, []))  # (cost, state, path)

    visited = set()  # Track visited states to avoid cycles

    while queue:
        cost, current_state, path = heapq.heappop(queue)

        if current_state == goal:
            return path  # Solution found, return the path

        if current_state not in visited:
            visited.add(current_state)

            # Explore possible moves
            for new_state in get_possible_moves(current_state):
                if new_state not in visited:
                    new_path = path + [new_state]
                    heapq.heappush(queue, (cost + 1, new_state, new_path))

    return None  # No solution found

# Example usage
if __name__ == "__main__":
    # Starting state: All missionaries and cannibals on the left
    start_state = (3, 3, 0, 0, 'left')
    # Goal state: All missionaries and cannibals on the right
    goal_state = (0, 0, 3, 3, 'right')

    # Use UCS to find a solution
    solution = ucs(start_state, goal_state)

    if solution:
        print("Uniform Cost Search Solution:")
        for step, state in enumerate(solution):
            print(f"Step {step}: {state}")
    else:
        print("No solution found.")