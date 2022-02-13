
def isSquareMatrix(A):
	if not A:
		return False

	nb_lines = len(A)

	for line in A:
		if type(line) != list or len(line) != nb_lines:
			return False

	return True

def isMatrix(A):
	if not A:
		return False

	nb_cols = len(A[0])

	for line in A:
		if type(line) != list or len(line) != nb_cols:
			return False

	return True

def join(A, B):
	""" Join vector B to matrix A """

	matrix = []

	# concatenate A and B -> matrix
	for i in range(len(A)):
		matrix.append(A[i] + [B[i]])

	return matrix

def triangulation(A, lower=False):
	""" Triangulation on extended square matrix A,
		it affect origin A 

		-> to lower triangular matrix if lower=True

		values to return:
			1: success
			0: A is not invertible matrix

	"""

	n = len(A)

	if not lower:
		RANGE_I = range(n - 1)
		RANGE_J = lambda i: range(i + 1, n)
	else:
		RANGE_I = range(n - 1, 0, -1)
		RANGE_J = lambda i: range(i - 1, -1, -1)
	
	for i in RANGE_I:
		pivot_line = A[i]
		pivot = pivot_line[i] # aii

		## if pivot=0: swap lines ##
		if not pivot:
			find = False

			for j in RANGE_J(i):
				if A[j][i] != 0:
					A[i], A[j] = A[j], A[i]
					find = True
					break

			if find:
				pivot_line = A[i]
				pivot = pivot_line[i] # aii
			else:
				return 0
		###

		for j in RANGE_J(i):
			secondary_line = A[j]
			sl_first = secondary_line[i]

			A[j] = [sl_i -(sl_first/pivot)*pl_i for (sl_i, pl_i) in zip(secondary_line, pivot_line)]

			# if any of line is null: [0, 0, ..., 0]
			# not with extended values (:n)
			if not any(A[j][:n]):
				return 0

	return 1

def diagonalization(A):
	""" Dagonalization on extended square matrix A 
		it affect origin A
		
		values return: report from triangulation function

	"""

	# do upper triangulation and lower triangulation on A
	res = triangulation(A)
	if res != 1: return res

	# print("Upper triangulation")
	# printMatrix(A)

	res = triangulation(A, lower=True)
	if res != 1: return res

	# print("Lower triangulation")
	# printMatrix(A)
	
	# divide Aii and Ai_-1 (extended value) by Aii
	for i in range(len(A)):
		A[i][-1] /= A[i][i]
		A[i][i] = 1.0

	# print("Diagonalization")
	# printMatrix(A)

	return 1

def crout(A):
	""" Crout decompositon on square matrix A
		Value to return:
			° Vectors L, U and O: if success
			° 0: if A is not invertible matrix

	""" 

	def permutation(i):
		# permutation of lines i and lines j (j > i) 
		# where L[j][i] != 0
		
		find = False

		for j in range(i + 1, n):
			if L[j][i] != i:
				L[i], L[j] = L[j], L[i]
				O[i], O[j] = O[j], O[i]
				A[i], A[j] = A[j], A[i]
				find = True
				break

		return find

	n = len(A)

	# Initialize L, U and O (O is permutation vector)
	L = [[0]*n for i in range(n)]
	U = [[0]*i + [1] + [0]*(n - i - 1)  for i in range(n)]
	O = list(range(n))

	# Find first column of L
	for i in range(n):
		L[i][0] = A[i][0]
	
	## permutation if the pivot is null
	if L[0][0] == 0 and not permutation(0):
		return 0
	
	# Find first line of U
	for i in range(n):
		U[0][i] = A[0][i]/L[0][0]
	
	for i in range(1, n):
		# pivot Lii
		L[i][i] = A[i][i] - sum(L[i][k]*U[k][i] for k in range(i))

		# column Li: L[j][i], j > i
		for j in range(i + 1, n):
			L[j][i] = A[j][i] - sum(L[j][k]*U[k][i] for k in range(j))

		## permutation if the pivot is null
		if L[i][i] == 0 and not permutation(i):
			return 0

		# line Ui: U[i][j], j > i
		for j in range(i + 1, n):
			U[i][j] = (A[i][j] - sum(L[i][k]*U[k][j] for k in range(i)))/L[i][i]

	# Lnn
	L[n - 1][n - 1] = A[n - 1][n - 1] - sum(L[n - 1][k]*U[k][n - 1] for k in range(n - 1))
	
	return L, U, O

def transpose(A):
	A = A.copy()

	for i in range(len(A)):
		for j in range(i + 1, len(A)):
			A[i][j], A[j][i] = A[j][i], A[i][j]

	return A

def printMatrix(A):
	if not isMatrix(A):
		return None

	for i in range(len(A)):
		print("|", *[a.rjust(5) for a in map(str, A[i])])
	
	print()