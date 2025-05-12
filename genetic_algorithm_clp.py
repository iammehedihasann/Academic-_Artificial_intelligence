import random

class Individual:
    def __init__(self, k, T):
        self.k, self.T = k, T
        # first two genes random 0–9, rest fixed 0
        ft = [random.randint(0, 9) for _ in range(min(2, k))]
        self.genes = ft + [0] * (k - len(ft))
        self.fitness = self.calc_fitness()

    def calc_fitness(self):
        # maximum diff between (g0+g1) and T is 18 → map to [0..18]
        return 18 - abs((self.genes[0] + self.genes[1]) - self.T)

class Population:
    def __init__(self, size, k, T):
        self.size = size
        self.individuals = [Individual(k, T) for _ in range(size)]

    def calculate_fitness(self):
        for ind in self.individuals:
            ind.fitness = ind.calc_fitness()

    def get_fittest(self):
        return max(self.individuals, key=lambda ind: ind.fitness)

    def get_second_fittest(self):
        return sorted(self.individuals, key=lambda ind: ind.fitness, reverse=True)[1]

    def get_least_fittest_index(self):
        return min(range(self.size), key=lambda i: self.individuals[i].fitness)

class GeneticAlgorithm:
    def __init__(self, T, k, pop_size=30, crossover_rate=0.8, mutation_rate=0.2):
        self.T, self.k = T, k
        self.pop = Population(pop_size, k, T)
        self.cr, self.mr = crossover_rate, mutation_rate
        self.generation = 0

    def selection(self):
        a, b = random.sample(self.pop.individuals, 2)
        return (a if a.fitness >= b.fitness else b,
                b if b.fitness > a.fitness else a)

    def crossover(self, p1, p2):
        if random.random() < self.cr and self.k > 1:
            # one-point crossover on the first two genes only
            pt = 1
            p1.genes[:pt], p2.genes[:pt] = p2.genes[:pt], p1.genes[:pt]

    def mutate(self, ind):
        # mutate only gene[0] or gene[1]
        for i in range(min(2, self.k)):
            if random.random() < self.mr:
                ind.genes[i] = random.randint(0, 9)

    def evolve(self, max_gens=500):
        self.pop.calculate_fitness()
        while self.generation < max_gens:
            best = self.pop.get_fittest()
            # perfect if fitness==18 ⇒ g0+g1 == T
            if best.fitness == 18:
                break

            # elitism: keep top 2
            new_inds = sorted(self.pop.individuals,
                              key=lambda ind: ind.fitness,
                              reverse=True)[:2]

            # fill rest of population
            while len(new_inds) < self.pop.size:
                p1, p2 = self.selection()
                c1 = Individual(self.k, self.T)
                c1.genes = p1.genes[:]
                c2 = Individual(self.k, self.T)
                c2.genes = p2.genes[:]
                self.crossover(c1, c2)
                self.mutate(c1)
                self.mutate(c2)
                c1.fitness = c1.calc_fitness()
                c2.fitness = c2.calc_fitness()
                new_inds += [c1, c2]

            self.pop.individuals = new_inds[:self.pop.size]
            self.pop.calculate_fitness()
            self.generation += 1

        return self.pop.get_fittest()

def main():
    T = int(input("T = "))
    k = int(input("k = "))
    ga = GeneticAlgorithm(T, k)
    sol = ga.evolve()
    print("Output:")
    print(" ".join(str(x) for x in sol.genes))

if __name__ == "__main__":
    main()
