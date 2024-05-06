import collections


def bfs(n, source, target, auxiliary):
    # Initial state with all disks on the source peg
    initial_state = (
        tuple(range(n, 0, -1)),
        (),
        (),
    )  # A has all disks, B and C are empty

    # Create a function to represent each state uniquely
    def state_key(state):
        return tuple(tuple(peg) for peg in state)

    # BFS queue holding tuples of (state, list of moves)
    queue = collections.deque([(initial_state, [])])
    # Set to track visited states
    visited = set()
    visited.add(state_key(initial_state))

    while queue:
        current_state, moves = queue.popleft()

        # If the final state is achieved (all disks on target peg)
        if current_state[pegs.index(target)] == tuple(range(n, 0, -1)):
            return moves

        # Explore possible moves
        for i in range(3):
            if not current_state[i]:  # No disks to move from this peg
                continue

            # Move the top disk from peg `i` to peg `j`
            for j in range(3):
                if i == j:
                    continue
                if current_state[j] and current_state[j][-1] < current_state[i][-1]:
                    continue  # Can't place larger disk on smaller disk

                # Make a new state by moving the top disk from `i` to `j`
                new_state = [list(peg) for peg in current_state]  # Deep copy
                disk = new_state[i].pop()  # Remove top disk from peg `i`
                new_state[j].append(disk)  # Add to peg `j`

                new_state = tuple(tuple(peg) for peg in new_state)  # Immutable
                if state_key(new_state) not in visited:
                    # Mark new state as visited and add to the queue
                    visited.add(state_key(new_state))
                    new_moves = moves + [
                        f"Move disk {disk} from {pegs[i]} to {pegs[j]}"
                    ]
                    queue.append((new_state, new_moves))

    return None  # If no solution found, which shouldn't happen


if __name__ == "__main__":
    num_disks = 3
    source, target, auxiliary = "A", "C", "B"
    pegs = (source, auxiliary, target)  # Peg order for convenience

    solution = bfs(num_disks, source, target, auxiliary)

    if solution:
        for step, move in enumerate(solution):
            print(f"Step {step + 1}: {move}")
    else:
        print("No solution found.")
