import random
import NextGen as ng
from NextGen import Stats

pop_n = [3333, 3333, 3]  # Number of: Humans, Drackonians, Gritiss
weights = [random.random() for i in range(5)]
stats = Stats()
stats.weights_summary(weights)
print_every = 10
population = ng.generate_population(pop_n)
for generation in range(4000):
	if generation % print_every == 0:
		print()
	stats.counting(population, generation, print_every=print_every)
	stats.creatures_summary(population, weights, generation, print_every=print_every)
	population = ng.evolve(population, weights)

