from utils.functions import *
from matrix import Matrix

def gauss(A, B):
	""" Gauss algorithm to solve AX = B (algebraic systems)

		value to retur in order:
			° -1: line(A) != line(B)
			° 0: A is not invertible matrix
			° Vector X (list): if success
	"""

	if len(A) != len(B):
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
			° -1: line(A) != line(B)
			° 0: A is not invertible matrix
			° Vector X (list): if success
	"""

	if len(A) != len(B):
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
			° -1: line(A) != line(B)
			° 0: A is not invertible matrix
			° Vector X (list): if success
	"""

	if len(A) != len(B):
		return -1

	length_A = len(A)
	X = [None for i in range(length_A)]
	Y = list()

	# get crout decomposition of A
	decomp = A.decompose(method="crout")
	if decomp == 0:
		return 0

	L, U, O = decomp

	# Change B according to O
	B = [B[i] for i in O]

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

def jaccobi(A, B, n_iter=10):
	n = len(A)

	X = [0 for i in range(n)]
	Xk = X.copy()

	for k in range(n_iter):
		for i in range(n):
			S = sum(A[i][j]*Xk[j] for j in range(n) if j != i)
			X[i] = (B[i] - S)/A[i][i]

		# print(k, X, Xk)
		Xk = X.copy()

	return X

def gaussSeidel(A, B, n_iter=10):
	n = len(A)

	X = [0 for i in range(n)]
	Xk = X.copy()

	for k in range(n_iter):
		for i in range(n):
			S1 = sum(A[i][j]*X[j] for j in range(i))
			S2 = sum(A[i][j]*Xk[j] for j in range(i + 1, n))
			
			X[i] = (B[i] - S1 - S2)/A[i][i]

		Xk = X.copy()

	return X

def main():
	# verify if not A.isSquareMatrix() or not isVector(B)
	res = gaussSeidel(Matrix([
			[6, 2, 1],
			[1, 2, 0],
			[3, 0, 1],
		]),
			[5, -1, -2], 100
		)

	print(res)

if __name__ == "__main__":
	main()