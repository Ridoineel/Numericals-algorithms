from utils.functions import *
from utils.matrix import Matrix
from utils.decorators import outputController

import numpy as np

# value to return in order (for all functions):
# 	° 0: A is not invertible matrix
# 	° 
#	-1: A is not square mat
#	-2: B is not vector
#	-3: len(A) != len(B)
#	0: A is not invertible matrix
#	1: A is not symetric
#	2: A is not defined positve
#	3: A is not dominant diagonal matrix
#	4: A is not tridiagonal matrix
# 	5: Lii = 0 while thomas running
#	Vector X (list): if success

@outputController
def gauss(A, B):
	""" Gauss algorithm to solve AX = B (algebraic systems)

	"""

	if not A.isSquareMatrix(): return -1
	if not isVector(B): return -2
	if len(A) != len(B): return -3

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

		X[i] = (Bi - Si)/Ai
		X[i] = round(X[i], 8)

	return X

@outputController
def gaussJordan(A, B):
	""" Gauss-Jordan algorithm to solve AX = B (algebraic systems)
	
	"""
	
	if not A.isSquareMatrix(): return -1
	if not isVector(B): return -2
	if len(A) != len(B): return -3

	length_A = len(A)
	X = []
	AB = join(A, B)

	# Do diagonalization
	if diagonalization(AB) == 0:
		return 0

	# Get X elements: last of AB lines
	for i in range(length_A):
		X.append(AB[i][-1])
		X[i] = round(X[i], 8)

	return X

@outputController
def lu(A, B, decomp_method="crout"):
	""" LU algorithm to solve AX = B (algebraic systems)

	"""

	if not A.isSquareMatrix(): return -1
	if not isVector(B): return -2
	if len(A) != len(B): return -3
	if not A.isInvertible(): return 0

	length_A = len(A)
	X = [None for i in range(length_A)]
	Y = list()

	# get crout decomposition of A
	decomp = A.decompose(method=decomp_method)

	if not isinstance(decomp, tuple):
		return decomp

	L, U, O = decomp

	# Change B according to O
	B = [B[i] for i in O]

	# Get Y elements by doing the descent
	for i in range(length_A):
		Si = sum([L[i][j]*Y[j] for j in range(i)])
		Bi = B[i]
		Lii = L[i][i]

		Y.append(round((Bi - Si)/Lii, 8))

	# Get X elements by doing the reascent
	for i in range(length_A - 1, -1, -1):
		Si = sum([U[i][j]*X[j] for j in range(i + 1, length_A)])
		Yi = Y[i]
		Uii = U[i][i]

		X[i] = (Yi - Si)/Uii
		X[i] = round(X[i], 8)

	return X

@outputController
def thomas(A, B):
	if not A.isSquareMatrix(): return -1
	if not isVector(B): return -2
	if len(A) != len(B): return -3
	if not A.istridiagonal(): return 4
	if not A.isInvertible(): return 0

	n = len(A)
	X = [0 for i in range(n)]
	# first elimination

	for i in range(1, n):
		if A[i-1][i-1] == 0:
			return 5
			# if A[i][i-1] != 0:
			# 	A[i-1], A[i] = A[i], A[i-1]
			# 	B[i-1], B[i] = B[i], B[i-1]
			# else:
			# 	return 0

		A[i][i] = A[i][i] - (A[i][i-1]/A[i-1][i-1])*A[i-1][i]
		B[i] = B[i] - (A[i][i-1]/A[i-1][i-1])*B[i-1]

		A[i][i - 1] = 0

	# X
	X[n-1] = B[n-1]/A[n-1][n-1]
	X[n-1] = round(X[n-1], 8)

	for i in range(n - 2, -1, -1):
		X[i] = (B[i] - A[i][i + 1]*X[i + 1])/A[i][i]
		X[i] = round(X[i], 8)

	return X

@outputController
def jacobi(A, B, n_iter=100):
	""" Jacobi algorithm to solve AX = B (algebraic systems)

	"""

	if not A.isSquareMatrix(): return -1
	if not isVector(B): return -2
	if len(A) != len(B): return -3
	if not A.isInvertible(): return 0

	# setBestPermutation(A, auxiliars_matrix=[B])

	if not A.isDominantDiagonal(): 
		return 3

	n = len(A)

	X = [0 for i in range(n)]
	Xk = X.copy()

	for k in range(n_iter):
		for i in range(n):
			S = sum(A[i][j]*Xk[j] for j in range(n) if j != i)
			
			X[i] = (B[i] - S)/A[i][i]
			X[i] = round(X[i], 8)

		# print(k, X, Xk)
		Xk = X.copy()

	return X

@outputController
def gaussSeidel(A, B, n_iter=20):
	""" Gauss-Seidel algorithm to solve AX = B (algebraic systems)

	"""

	if not A.isSquareMatrix(): return -1
	if not isVector(B): return -2
	if len(A) != len(B): return -3
	if not A.isInvertible(): return 0

	# setBestPermutation(A, auxiliars_matrix=[B])

	if not A.isDominantDiagonal():
		return 3

	n = len(A)

	X = [0 for i in range(n)]
	Xk = X.copy()

	for k in range(n_iter):
		for i in range(n):
			S1 = sum(A[i][j]*X[j] for j in range(i))
			S2 = sum(A[i][j]*Xk[j] for j in range(i + 1, n))
			
			X[i] = (B[i] - S1 - S2)/A[i][i]
			X[i] = round(X[i], 8)

		Xk = X.copy()

	return X

@outputController
def jacobi2(A, B, n_iter=20):
	""" Jacobi algorithm to solve AX = B (algebraic systems)

	"""

	if not A.isSquareMatrix(): return -1
	if not isVector(B): return -2
	if len(A) != len(B): return -3
	if not A.isInvertible(): return 0

	if not A.isDominantDiagonal(): 
		return 3

	n = len(A)

	D, L, U = A.decompose("DLU")

	# inverse of D
	for i in range(n):
		D[i][i] = 1/D[i][i]

	T = -D*(L + U)
	C = D*B
	X = [0 for i in range(n)]
	Xk = X.copy()

	g = lambda X: T.dot(X) + C
	
	X = np.array([[i] for i in X])
	T = np.array(T)
	C = np.array([[i] for i in C])


	for i in range(n_iter):
		X = g(Xk)

		Xk = X

	X = [round(i[0], 8) for i in X]

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