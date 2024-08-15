# ==============================================================
# import the Class GA
import Class_GA as ga
from typing import List


# ==============================================================
# Example usage: Solving Traveling Salesman Problem (TSP)
# Define the cities
cities = ['A', 'B', 'C', 'D']

# Define the weighted graph (distances) between cities
weights = {
    ('A', 'B'): 10, ('A', 'C'): 15, ('A', 'D'): 20,
    ('B', 'C'): 35, ('B', 'D'): 25,
    ('C', 'D'): 30
}

# ==============================================================
# Get the weight between two cities.
def get_weight(city1: str, city2: str) -> int:
    if city1 == city2:
        return 0
    if (city1, city2) in weights:
        return weights[(city1, city2)]
    if (city2, city1) in weights:
        return weights[(city2, city1)]
    raise ValueError(f"No weight defined for {city1} to {city2}")

# ==============================================================
# Calculate the fitness of a TSP solution.
# Fitness is the inverse of the total distance (shorter distance = higher fitness).
# param chromosome: List of city indices representing the route
# return: Fitness value (higher is better)
def tsp_fitness(chromosome: List[int]) -> float:
    total_distance = 0
    for i in range(len(chromosome)):
        city1 = cities[chromosome[i]]
        city2 = cities[chromosome[(i + 1) % len(chromosome)]]
        total_distance += get_weight(city1, city2)

    return 1 / total_distance


# ==============================================================
# Initialize and run the Genetic Algorithm
ga = ga.GeneticAlgorithm(
    population_size=100,
    chromosome_length=len(cities),
    fitness_func=tsp_fitness,
    mutation_rate=0.02,
    crossover_rate=0.8,
    elitism=0.1
)

best_solution = ga.evolve(generations=500)

# Decode and print the best solution
best_route = [cities[i] for i in best_solution]
print("Best TSP Route:", ' -> '.join(best_route + [best_route[0]]))  # Add starting city at the end to complete the loop

# Calculate and print the total distance
total_distance = sum(get_weight(best_route[i], best_route[(i + 1) % len(best_route)]) for i in range(len(best_route)))
print("Total Distance:", total_distance)

# Print the distances between each pair of cities in the route
print("\nDistances between cities in the route:")
for i in range(len(best_route)):
    city1 = best_route[i]
    city2 = best_route[(i + 1) % len(best_route)]
    distance = get_weight(city1, city2)
    print(f"{city1} -> {city2}: {distance}")