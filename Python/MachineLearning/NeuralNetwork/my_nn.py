import numpy as np

L0 = np.array([[0, 0, 1], [1, 0, 0], [0, 1, 0]])

Y = np.array([[0, 1, 0]]).T

synapse_0 = 2 * np.random.random((3, 4)) - 1
synapse_1 = 2 * np.random.random((4, 3)) - 1
synapse_2 = 2 * np.random.random((3, 1)) - 1

L1 = 1/(1+np.exp(-np.dot(L0, synapse_0)))
L2 = 1/(1+np.exp(-np.dot(L1, synapse_1)))
L3 = 1/(1+np.exp(-np.dot(L2, synapse_2)))

print(L3) 
