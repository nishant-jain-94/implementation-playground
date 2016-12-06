import numpy as np 

def mean(X):
	"""Returns the mean of the array. 

	Input:

	X - Refers to the matrix

	Output: Returns a scalar
	"""
	flattend_matrix = X.flatten()
	mean = np.sum(flattend_matrix) / len(flattend_matrix)
	return mean


X = np.arange(9)

assert (X.mean() == mean(X)), "np.mean is equal to the mean function"
