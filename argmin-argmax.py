import numpy as np

def argmin(X, axis=1):
	"""
	Returns the index of the minimum element along an axis
	"""
	if (axis == 1):
		flattend_matrix = X.flatten()
		Xmin = (flattend_matrix[0], 0)
		for i in range(len(flattend_matrix)):
			