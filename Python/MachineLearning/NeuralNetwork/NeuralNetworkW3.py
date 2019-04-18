import numpy as np

# sigmoid function
def nonlin(x,deriv=False):
	if(deriv==True):
		return x*(1-x)
	return 1/(1+np.exp(-x))
	
# input dataset
l0 = np.array([  [0,0,1],
               [0,1,1],
               [1,0,1],
               [1,1,1],
               [0,1,1]])

# output dataset
Y = np.array([[0, 0, 1, 1, 0]]).T

# seed random numbers to make calculation
# deterministic (just a good practice)
np.random.seed(1)

# initialize weights randomly with mean 0
synapse_0 = 2 * np.random.random((3, 4)) - 1
synapse_1 = 2 * np.random.random((4, 3)) - 1
synapse_2 = 2 * np.random.random((3, 1)) - 1

for iter in range(20000):

	# forward propagation
	l1 = nonlin(np.dot(l0 ,synapse_0))
	l2 = nonlin(np.dot(l1 ,synapse_1))
	l3 = nonlin(np.dot(l2 ,synapse_2))
	
	# error
	l3_error = Y - l3
	
	# gradient decent
	l3_delta = l3_error * nonlin(l3,deriv=True)
	
	
	# error
	l2_error = l3_delta.dot(synapse_2.T)
	
	# gradient decent
	l2_delta = l2_error * nonlin(l2,deriv=True)
	
	
	# error
	l1_error = l2_delta.dot(synapse_1.T)
	
	# gradient decent,
	l1_delta = l1_error * nonlin(l1,deriv=True)
	
	synapse_2 += l2.T.dot(l3_delta)
	synapse_1 += l1.T.dot(l2_delta)
	synapse_0 += l0.T.dot(l1_delta)
	
	if iter % 10000 == 0:
		print(l3_error)
		
print("Output After Training:")
print(l3)

