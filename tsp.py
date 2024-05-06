import random


def distance(c1, c2):
    return ((c1[0] - c2[0]) ** 2 + (c1[1] - c2[1]) ** 2) ** 0.5


def route_distance(route, cities):
    return sum(
        distance(cities[route[i]], cities[route[i + 1]]) for i in range(len(route) - 1)
    )


def generate_population(pop_size, cities):
    return [random.sample(list(cities.keys()), len(cities)) for _ in range(pop_size)]


def crossover_and_mutate(p1, p2, mutation_rate=0.1):
    start, end = sorted(random.sample(range(len(p1)), 2))
    child = p1[start:end] + [c for c in p2 if c not in p1[start:end]]

    if random.random() < mutation_rate:
        idx1, idx2 = random.sample(range(len(child)), 2)
        child[idx1], child[idx2] = child[idx2], child[idx1]
        print(f"Mutation occurred: Swapped cities at indices {idx1} and {idx2}")

    return child


def evolve_population(population, cities):

    p1, p2 = random.sample(population, 2)

    child = crossover_and_mutate(p1, p2)

    worst_route = max(population, key=lambda route: route_distance(route, cities))
    population.remove(worst_route)
    population.append(child)


def run_genetic_algorithm(cities, pop_size, num_iterations):

    population = generate_population(pop_size, cities)

    for _ in range(num_iterations):
        evolve_population(population, cities)

    best_route = min(population, key=lambda route: route_distance(route, cities))
    best_distance = route_distance(best_route, cities)

    return best_route, best_distance


if __name__ == "__main__":
    cities = {"A": (0, 0), "B": (5, 2), "C": (6, 3), "D": (3, 4), "E": (2, 5)}
    pop_size = 50
    num_iterations = 100

    best_route, best_distance = run_genetic_algorithm(cities, pop_size, num_iterations)

    print("Best route:", best_route)
    print("Total distance:", best_distance)
