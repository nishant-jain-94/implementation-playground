import numpy as np 

def min(X):
	"""Return the minimum value of the matrix X. """
	
	flattend_matrix = X.flatten()
	Xmin = flattend_matrix[0]
	for i in range(len(flattend_matrix)):
		if (Xmin > flattend_matrix[i]):
			Xmin = flattend_matrix[i]
	return Xmin

def max(X):
	"""Returns the maximum value of the Matrix X. """
	
	flattend_matrix = X.flatten()
	Xmax = flattend_matrix[0]
	for i in range(len(flattend_matrix)):
		if (Xmax < flattend_matrix[i]):
			Xmax = flattend_matrix[i]
	return Xmax

# X refers to the matrix
X = np.arange(9).reshape(3, 3)

assert (X.min() == min(X)), "np.min equals min function"
assert (X.max() == max(X)), "np.max equals max function"

