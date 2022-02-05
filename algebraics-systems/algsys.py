from utils.functions import *

def gauss(A, B):
	""" Gauss algorithm to solve AX = B (algebraic systems)

		value to retur in order:
			° -1: A isn't square matrix or 
				  B isn't vector or 
				  line(A) != line(B)
			° 0: A is not invertible matrix
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
	

	# Get X elements by doing the reascent
	for i in range(length_A - 1, -1, -1):
		Si = sum([AB[i][j]*X[j] for j in range(i + 1, length_A)])
		Bi = AB[i][-1]
		Ai = AB[i][i]

		X[i] = round((Bi - Si)/Ai, 8)

		# # convert X float-integer to integer type : ex -1.0 -> -1
		if type(X[i]) == float and X[i].is_integer():
			X[i] = int(X[i])

	return X

def gaussJordan(A, B):
	""" Gauss-Jordan algorithm to solve AX = B (algebraic systems)

		value to return in order:
			° -1: A isn't square matrix or 
				  B isn't vector or 
				  line(A) != line(B)
			° 0: A is not invertible matrix
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

	# Get X elements: last of AB lines
	for i in range(length_A):
		X.append(round(AB[i][-1], 8))

		# # convert Xi float-integer to integer type : ex -1.0 -> -1
		if type(X[i]) == float and X[i].is_integer():
			X[i] = int(X[i])

	return X

def lu(A, B):
	""" LU algorithm to solve AX = B (algebraic systems)

		value to return in order:
			° -1: A isn't square matrix or 
				  B isn't vector or 
				  line(A) != line(B)
			° 0: A is not invertible matrix
			° Vector X (list): if success
	"""

	if not isSquareMatrix(A) or type(B) != list or (len(A) != len(B)):
		return -1

	length_A = len(A)

	L, U = crout(A)

	Y = list()
	X = [None for i in range(length_A)]

	# Get Y elements by doing the descent
	for i in range(length_A):
		Si = sum([L[i][j]*Y[j] for j in range(i)])
		Bi = B[i]
		Lii = L[i][i]

		Y.append(round((Bi - Si)/Lii, 8))

		# convert Y float-integer to integer type : ex -1.0 -> -1
		if type(Y[i]) == float and Y[i].is_integer():
			Y[i] = int(Y[i])

	# Get X elements by doing the reascent
	for i in range(length_A - 1, -1, -1):
		Si = sum([U[i][j]*X[j] for j in range(i + 1, length_A)])
		Yi = Y[i]

		X[i] = round(Yi - Si, 8)

		# # convert X float-integer to integer type : ex -1.0 -> -1
		if type(X[i]) == float and X[i].is_integer():
			X[i] = int(X[i])

	return X

def main():
	res = lu([
			[1, 2, 1],
			[0, 1, 0],
			[0, 2, 1]
		], 
			[3, 2, 1]
		)

	print(res)

if __name__ == "__main__":
	main()