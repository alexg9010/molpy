import numpy as np

def distance(point1, point2):
	
	point1 = np.asarry(point1)
	point2 = np.asarry(point2)
	return np.linalg.norm(point1 - point2)
