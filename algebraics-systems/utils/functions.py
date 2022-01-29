
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
			0: A is null matrix

	"""

	length_A = len(A)

	if not lower:
		RANGE_I = range(length_A - 1)
		RANGE_J = lambda i: range(i + 1, length_A)
	else:
		RANGE_I = range(length_A - 1, 0, -1)
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
			# not with extended values (:length_A)
			if not any(A[j][:length_A]):
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