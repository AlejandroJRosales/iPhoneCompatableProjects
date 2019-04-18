import random
import numpy as np


pop_keep = .8
prob_crossover = 0.6
prob_mutation = 0.2
tournament_size = 4


def non_lin(x, derivative=False):
	if derivative:
		return x * (1 - x)
	return 1 / (1 + np.exp(-x))
	
	
def propagate(inp, target, weights):
	out = non_lin(np.dot(inp, weights))
	return target - out
	
	
def run_test(test_data, correct, weights):
	print("\nTest Data: ", test_data)
	print("\nCorrect: ", correct)
	print("Predicted: ", round(non_lin(np.dot(test_data, weights))[0], 8))
	
	
def generate_population(genes_per_ch, pop_size):
	individuals = []
	for i in range(0, pop_size):
		individuals.append(2 * np.random.random((genes_per_ch, 1)) - 1)
	return individuals
	
	
def calc_fitness(inp, target, population):
	pop_fitness = []
	for individual in population:
		fitness = 0
		total_error = propagate(inp, target, individual)
		for error in total_error:
			fitness += abs(error)
		pop_fitness.append(fitness)
	return pop_fitness
	
	
def select_fittest(population, pop_fitness, genes_per_ch, pop_size):
	fitter_population = []
	for i in range(int(pop_size * .1)):
		fitter_population.append(population[pop_fitness.index(min(pop_fitness))])
	for i in range(0, int(len(population) * pop_keep)):
		r = random.randint(0, len(pop_fitness) - 1)
		best = pop_fitness[r]
		best_player = population[r]
		for member in range(0, tournament_size):
			competitor_index = random.randint(0, len(pop_fitness) - 1)
			if pop_fitness[competitor_index] < best:
				best_player = population[competitor_index]
		fitter_population.append(best_player)
	for a in range(len(population) - len(fitter_population)):
		fitter_population.insert(random.randint(0, len(fitter_population)), 2 * np.random.random((genes_per_ch, 1)) - 1)
	return fitter_population
	
	
def crossover(population, genes_per_ch, pop_size):
	for individual in range(int((len(population) - 2))):
		if random.random() <= prob_crossover:
			parent1 = population.pop(individual)
			parent2 = population.pop(individual + 1)
			r = random.randint(0, genes_per_ch)
			child1 = []
			child2 = []
			for i in range(r):
				child1.append(parent1[i])
			for i in range(genes_per_ch - r):
				child2.append(parent2[i])
			for i in range(genes_per_ch - len(child1)):
				child1.append(parent2[i])
			for i in range(genes_per_ch - len(child2)):
				child2.append(parent1[i])
			population.insert(random.randint(0, pop_size), np.array(child1))
			population.insert(random.randint(0, pop_size), np.array(child2))
	return population
	
	
def mutation(population, genes_per_ch):
	for individual in range(int((len(population) - 1))):
		if random.random() <= prob_mutation:
			ch = population.pop(individual)
			for i in range(0, random.randint(0, genes_per_ch)):
				r = random.randint(0, 1)
				index = random.randint(0, genes_per_ch - 1)
				get_chr = ch[index]
				mutate = random.randint(0, int(abs(max(ch) * 10000))) / 1000
				if r == 0:
					ch[index] = get_chr * mutate
				else:
					if mutate == 0:
						ch[index] = get_chr / random.random()
					else:
						ch[index] = get_chr / mutate
			population.append(ch)
		return population
		
		
def breed(population, genes_per_ch, pop_size):
	return mutation(crossover(population, genes_per_ch, pop_size), genes_per_ch)
	
	
def train(inp, target, epochs=200, pop_size=200, test_data=[], correct=0):
	genes_per_ch = len(inp[0])
	population = generate_population(genes_per_ch, pop_size)
	for generation in range(0, epochs + 1):
		pop_fitness = calc_fitness(inp, target, population)
		if generation % 50 == 0:
			best = 10000
			best_player = []
			worst = 0
			total = 0
			for player in range(len(pop_fitness)):
				if pop_fitness[player] < best:
					best = pop_fitness[player]
					best_player = population[player]
				if pop_fitness[player] > worst:
					worst = pop_fitness[player]
				total += pop_fitness[player]
			print("[G %3d] score=(%4f, %4f, %4f) weights: " %
			(generation, best, total / pop_size, worst), end="")
			for weight in best_player:
				print(weight, end=" ")
			print("")
		population = breed(select_fittest(population, pop_fitness, genes_per_ch, pop_size), genes_per_ch, pop_size)
	if len(test_data) != 0:
		run_test(test_data, correct, best_player)
	return best_player
