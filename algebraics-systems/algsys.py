from utils.functions import *

def gauss(A, B):
	""" Gauss algorithm to solve AX = B (algebraic systems)

		value to retur in order:
			° -1: A isn't square matrix or 
				  B isn't vector or 
				  line(A) != line(B)
			° 0: A is null matrix
			° Vector X (list): if success
	"""

	if not isSquareMatrix(A) or type(B) != list or (len(A) != len(B)):
		return -1

	length_A = len(A)
	X = [None for i in range(length_A)]
	AB = join(A, B)

	
	# Do triangulation
	if triangulation(AB) == 0:
		return 0
	

	# GOING BACK UP and Calculate X (Xi)
	# Xi = (B'i - sum(A'ij*Xj))/A'ii : j > i

	for i in range(length_A - 1, -1, -1):
		Si = sum([AB[i][j]*X[j] for j in range(i + 1, length_A)])
		Bi = AB[i][-1]
		Ai = AB[i][i]

		X[i] = round((Bi - Si)/Ai, 8)

		# convert X float-integer to integer type : ex -1.0 -> -1
		if X[i].is_integer():
			X[i] = int(X[i])

	return X

def gaussJordan(A, B):
	""" Gauss-Jordan algorithm to solve AX = B (algebraic systems)

		value to return in order:
			° -1: A isn't square matrix or 
				  B isn't vector or 
				  line(A) != line(B)
			° 0: A is null matrix
			° Vector X (list): if success
	"""

	if not isSquareMatrix(A) or type(B) != list or (len(A) != len(B)):
		return -1

	length_A = len(A)
	X = []
	AB = join(A, B)

	# Do diagonalization
	if diagonalization(AB) == 0:
		return 0

	# Get X result: last of AB lines
	for line in AB:
		Xi = round(line[-1], 8)

		# convert Xi float-integer to integer type : ex -1.0 -> -1
		if Xi.is_integer():
			Xi = int(Xi)

		X.append(Xi)

	return X

def main():
	res = gaussJordan([
			[1, 0, 3],
			[-1, 2, 1],
			[2, 0, 5]
		], 
			[1, 2, 3]
		)

	print(res)

if __name__ == "__main__":
	main()