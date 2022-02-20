from utils.functions import *
from utils.matrix import Matrix
from utils.decorators import outputController

# value to return in order (for all functions):
# 	° -1: A is not square matrix or
# 		  B is not vector or
# 		  line(A) != line(B)
# 	° 0: A is not invertible matrix
# 	° Vector X (list): if success

@outputController
def gauss(A, B):
	""" Gauss algorithm to solve AX = B (algebraic systems)

	"""

	if not A.isSquareMatrix() or not isVector(B) or len(A) != len(B):
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

@outputController
def gaussJordan(A, B):
	""" Gauss-Jordan algorithm to solve AX = B (algebraic systems)
	
	"""

	if not A.isSquareMatrix() or not isVector(B) or len(A) != len(B):
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

@outputController
def lu(A, B, decomp_method="crout"):
	""" LU algorithm to solve AX = B (algebraic systems)

	"""

	if not A.isSquareMatrix() or not isVector(B) or len(A) != len(B):
		return -1

	length_A = len(A)
	X = [None for i in range(length_A)]
	Y = list()

	# get crout decomposition of A
	decomp = A.decompose(method=decomp_method)
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

@outputController
def jaccobi(A, B, n_iter=20):
	""" Jaccobi algorithm to solve AX = B (algebraic systems)

	"""

	if not A.isSquareMatrix() or not isVector(B) or len(A) != len(B):
		return -1

	n = len(A)

	X = [0 for i in range(n)]
	Xk = X.copy()

	for k in range(n_iter):
		for i in range(n):
			## permutation if pivot A[i][i]=0 ##
			if A[i][i] == 0 and not permutation(A, start=i, auxiliars_matrix=[B]):
				return 0

			S = sum(A[i][j]*Xk[j] for j in range(n) if j != i)
			X[i] = round((B[i] - S)/A[i][i], 8)

		# print(k, X, Xk)
		Xk = X.copy()

	return X

@outputController
def gaussSeidel(A, B, n_iter=20):
	""" Gauss-Seidel algorithm to solve AX = B (algebraic systems)

	"""

	if not A.isSquareMatrix() or not isVector(B) or len(A) != len(B):
		return -1

	n = len(A)

	X = [0 for i in range(n)]
	Xk = X.copy()

	for k in range(n_iter):
		for i in range(n):
			## permutation if pivot A[i][i]=0 ##
			if A[i][i] == 0 and not permutation(A, start=i, auxiliars_matrix=[B]):
				return 0
	
			S1 = sum(A[i][j]*X[j] for j in range(i))
			S2 = sum(A[i][j]*Xk[j] for j in range(i + 1, n))
			
			X[i] = round((B[i] - S1 - S2)/A[i][i], 8)

		Xk = X.copy()

	return X

def main():
	# verify if not A.isSquareMatrix() or not isVector(B)
	X = lu(Matrix([
			[0, 2, 1],
			[1, 2, 0],
			[0, 1, 0],
		]),
			[5, -1, -2]
		)


	print(X)

if __name__ == "__main__":
	main()