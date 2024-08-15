
# ==============================================================
# Importing the libraries
# ==============================================================
import random
from typing import List, Callable

# ==============================================================
# Making the class of GA
# ==============================================================
"""
Initialize the Genetic Algorithm.

:param population_size: Number of individuals in the population
:param chromosome_length: Length of each chromosome
:param fitness_func: Function to evaluate fitness of a chromosome
:param mutation_rate: Probability of mutation for each gene
:param crossover_rate: Probability of crossover between two parents
:param elitism: Proportion of best individuals to carry over to next generation
"""
# ==============================================================
class GeneticAlgorithm:
    def __init__(self, population_size: int, chromosome_length: int,
                 fitness_func: Callable, mutation_rate: float = 0.01,
                 crossover_rate: float = 0.8, elitism: float = 0.1):

        # ========================================
        # setting the value of population size
        self.population_size = population_size

        # ========================================
        # setting the value of chromosome_length
        self.chromosome_length = chromosome_length

        # ========================================
        # setting the fitness_func
        self.fitness_func = fitness_func

        # ========================================
        # setting the value of mutation_rate
        self.mutation_rate = mutation_rate

        # ========================================
        # setting the value of crossover_rate
        self.crossover_rate = crossover_rate

        # ========================================
        # setting the value of elite in population
        self.elitism = elitism

        # ========================================
        # Initialize population with random permutations
        self.population = [self.generate_chromosome() for _ in range(population_size)]

    # ==============================================================
    # Generate a random permutation as a chromosome.
    def generate_chromosome(self) -> List[int]:
        return random.sample(range(self.chromosome_length), self.chromosome_length)

    # ==============================================================
    # Calculate the fitness of a chromosome using the provided fitness function.
    def calculate_fitness(self, chromosome: List[int]) -> float:
        return self.fitness_func(chromosome)

    # ==============================================================
    # Select a parent using tournament selection.
    def select_parent(self, population: List[List[int]]) -> List[int]:
        tournament_size = 3
        tournament = random.sample(population, tournament_size)
        return max(tournament, key=self.calculate_fitness)

    # ==============================================================
    # Perform ordered crossover between two parents.
    def crossover(self, parent1: List[int], parent2: List[int]) -> List[int]:

        # ========================================
        # checking the probability of crossover
        if random.random() < self.crossover_rate:

            start, end = sorted(random.sample(range(self.chromosome_length), 2))
            child = [-1] * self.chromosome_length
            child[start:end] = parent1[start:end]
            remaining = [item for item in parent2 if item not in child]

            for i in range(self.chromosome_length):
                if child[i] == -1:
                    child[i] = remaining.pop(0)

            # return child
            return child

        # else return parent1
        return parent1

    # ==============================================================
    # Perform swap mutation on a chromosome.
    def mutate(self, chromosome: List[int]) -> List[int]:
        # ========================================
        # checking the probability of mutation
        if random.random() < self.mutation_rate:

            i, j = random.sample(range(self.chromosome_length), 2)

            chromosome[i], chromosome[j] = chromosome[j], chromosome[i]

        # return
        return chromosome

    # ==============================================================
    # Evolve the population for a specified number of generations.
    #
    # :param generations: Number of generations to evolve
    # :return: Best chromosome found
    def evolve(self, generations: int) -> List[int]:

        for _ in range(generations):
            # Calculate fitness for all chromosomes
            fitnesses = [self.calculate_fitness(chrom) for chrom in self.population]

            # Sort population by fitness (descending order)
            sorted_population = [x for _, x in sorted(zip(fitnesses, self.population), reverse=True)]

            # Apply elitism
            elite_size = int(self.elitism * self.population_size)
            new_population = sorted_population[:elite_size]

            # Generate new individuals
            while len(new_population) < self.population_size:
                parent1 = self.select_parent(sorted_population)
                parent2 = self.select_parent(sorted_population)
                child = self.crossover(parent1, parent2)
                child = self.mutate(child)
                new_population.append(child)

            self.population = new_population

        # Return the best chromosome from the final population
        return max(self.population, key=self.calculate_fitness)

