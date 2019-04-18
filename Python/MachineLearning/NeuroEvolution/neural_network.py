import numpy as np
import neuro_evolution as ne

def squish(x, derivative=False):
	return 1 / (1 + np.exp(-x))

X = np.array([[1, 1, 0],
              [0, 1, 1],
              [1, 0, 1],
              [1, 1, 1],])

Y = np.array([[1, 0, 1, 1]]).T

weights = ne.train(X, Y, epochs=200, pop_size=200, test_data=[0, 1, 0], correct=0)

print(weights)
print(squish(np.dot(X, weights)))
