import heapq

# Heuristic function: number of people left on the starting side
def heuristic(state):
    left_missionaries, left_cannibals, _, _, _ = state
    return left_missionaries + left_cannibals  # Total people left to cross

# Generate valid moves from a given state
def get_possible_moves(state):
    left_missionaries, left_cannibals, right_missionaries, right_cannibals, boat_position = state
    possible_moves = []

    # Define possible transitions
    transitions = [
        (1, 0),  # One missionary
        (2, 0),  # Two missionaries
        (0, 1),  # One cannibal
        (0, 2),  # Two cannibals
        (1, 1),  # One missionary and one cannibal
    ]

    # Generate new states from valid transitions
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

        # Ensure the move doesn't violate the constraints
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

# A* Search for solving the Missionaries and Cannibals problem
def astar(start, goal):
    # Priority queue to track states with combined cost and heuristic
    queue = []
    heapq.heappush(queue, (0, 0, start, [start]))  # (total_cost, path_cost, state, path)

    visited = set()  # Set to track visited states to avoid cycles

    while queue:
        total_cost, path_cost, current_state, path = heapq.heappop(queue)

        if current_state == goal:
            return path  # Solution found, return the path

        if current_state not in visited:
            visited.add(current_state)

            # Explore possible moves
            for new_state in get_possible_moves(current_state):
                if new_state not in visited:
                    new_path_cost = path_cost + 1  # Increment path cost
                    total_cost = new_path_cost + heuristic(new_state)  # A* combines path cost and heuristic
                    new_path = path + [new_state]
                    heapq.heappush(queue, (total_cost, new_path_cost, new_state, new_path))

    return None  # No solution found

# Example usage
if __name__ == "__main__":
    # Starting state: All missionaries and cannibals on the left
    start_state = (3, 3, 0, 0, 'left')
    # Goal state: All missionaries and cannibals on the right
    goal_state = (0, 0, 3, 3, 'right')

    # Use A* Search to find a solution
    solution = astar(start_state, goal_state)

    if solution:
        print("A* Search Solution:")
        for step, state in enumerate(solution):
            print(f"Step {step}: {state}")
    else:
        print("No solution found.")