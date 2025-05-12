import random

def fitness(individual):
    n = len(individual)
    non_attacking_pairs = 0
    max_pairs = n * (n-1)//2
    attaking_pairs = 0
    for i in range(n):
        for j in range(i+1, n):
            if abs(individual[i] - individual[j]) == abs(i - j):
                attaking_pairs +=1

    non_attacking_pairs = max_pairs - attaking_pairs
    return non_attacking_pairs


def create_individual(n):
    individual = list(range(n))
    random.shuffle(individual)
    return individual

def create_population(size , n):
    return [create_individual(n) for _ in range(size)]


def tournament_selection(population, scores, k=3):
    selected = random.sample(list(zip(population,scores)),k)
    selected.sort(key=lambda x: x[1], reverse=True)
    return selected[0][0]

def crossover(parent1, parent2):
    size = len(parent1)
    child = [None]*size
    start, end = sorted(random.sample(range(size), 2))
    child[start:end+1] = parent1[start:end+1]
    p2_idx = 0
    for i in range(size):
        if child[i] is None:
            while parent2[p2_idx] in child:
                p2_idx += 1
            child[i] = parent2[p2_idx]
    return child



def mutate(individual, mutation_rate=0.1):
    individual = individual[:]
    if random.random() < mutation_rate:
        idx1, idx2 = random.sample(range(len(individual)), 2)
        individual[idx1], individual[idx2] = individual[idx2], individual[idx1]
    return individual


def print_board(individual):
    n = len(individual)
    for row in range(n):
        line = ['.']*n
        line[individual[row]] = 'Q'
        print(' '.join(line))
    print()

def genetic_algorithm(n, population_size=100, generations=1000, mutation_rate=0.1):
    population = create_population(population_size, n)
    max_fitness = n*(n-1)//2
    for gen in range(generations):
        scores = [fitness(ind) for ind in population]

        if max_fitness in scores:
            solution = population[scores.index(max_fitness)]
            print(f"Solution found at generation {gen}:")
            print_board(solution)
            return solution

        new_population = []
        for _ in range(population_size):
            parent1 = tournament_selection(population, scores, k=5)
            parent2 = tournament_selection(population, scores, k=5)
            child = crossover(parent1, parent2)
            child = mutate(child, mutation_rate)
            new_population.append(child)
        population = new_population

        if gen % 100 == 0:
            best_score = max(scores)
            print(f"Generation {gen}: Best fitness = {best_score}")

    print("No solution found")
    return None


if __name__ == "__main__":
    N = 8
    print(f"Solving {N}-Queens problem using Genetic Algorithm...\n")
    genetic_algorithm(N)


