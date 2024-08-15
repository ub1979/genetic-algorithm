# Genetic Algorithm Class

This repository contains a Python implementation of a Genetic Algorithm (GA) class and an example application solving the Traveling Salesman Problem (TSP).

## Contents

1. `Class_GA.py`: Contains the `GeneticAlgorithm` class, a flexible implementation of a genetic algorithm.
2. `TS_example.py`: Demonstrates how to use the `GeneticAlgorithm` class to solve a Traveling Salesman Problem.

## How to Use

### Requirements

- Python 3.6 or higher
- No additional libraries required

### Running the TSP Example

1. Clone this repository:
   ```
   git clone https://github.com/yourusername/ga-tsp-solver.git
   cd ga-tsp-solver
   ```

2. Run the TSP example:
   ```
   python TS_example.py
   ```

This will execute the genetic algorithm to find an optimal solution for the TSP defined in the script.

### Using the GeneticAlgorithm Class

To use the `GeneticAlgorithm` class for your own problems:

1. Import the class:
   ```python
   from Class_GA import GeneticAlgorithm
   ```

2. Define your fitness function. It should take a chromosome (list of integers) as input and return a fitness score (float).

3. Initialize the GA:
   ```python
   ga = GeneticAlgorithm(
       population_size=100,
       chromosome_length=your_chromosome_length,
       fitness_func=your_fitness_function,
       mutation_rate=0.02,
       crossover_rate=0.8,
       elitism=0.1
   )
   ```

4. Evolve the population:
   ```python
   best_solution = ga.evolve(generations=500)
   ```

5. Interpret the result based on your problem domain.

## Customization

- Modify the `mutation_rate`, `crossover_rate`, and `elitism` parameters to fine-tune the algorithm's performance.
- Adjust the `population_size` and number of `generations` based on your problem's complexity and computational resources.
- For problems other than permutation-based ones like TSP, you may need to modify the `generate_chromosome`, `crossover`, and `mutate` methods in the `GeneticAlgorithm` class.

## Contributing

Contributions to improve the algorithm or add new features are welcome. Please feel free to submit pull requests or open issues for any bugs or enhancements.

## License

This project is open-source and available under the MIT License.
