def tower_of_hanoi(n, source, auxiliary, destination):
    if n == 1:
        print(f"Move disk 1 from {source} to {destination}")
        return

    # Move n-1 disks from source to auxiliary
    tower_of_hanoi(n - 1, source, destination, auxiliary)

    # Move the remaining disk from source to destination
    print(f"Move disk {n} from {source} to {destination}")

    # Move n-1 disks from auxiliary to destination
    tower_of_hanoi(n - 1, auxiliary, source, destination)


# Example usage
# n = int(input("Enter no. of discs: "))  # Number of disks
tower_of_hanoi(3, "A", "B", "C")
