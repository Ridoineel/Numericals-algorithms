def isMatrix(A):
	if not A:
		return False

	nb_cols = len(A[0])

	for line in A:
		if type(line) != list or len(line) != nb_cols:
			return False

	return True

def isVector(A):
	if not isinstance(A, list):
		return False

	for i in A:
		if isinstance(i, list):
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

		## if pivot=0: swap line 
		## with line where max pivot != 0
		if pivot == 0:
			if permutation(A, start=i):
				# update pivot
				pivot_line = A[i]
				pivot = pivot_line[i] 
			else:
				return 0

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

def permutation(matrix, start: int, auxiliars_matrix=list()):
	""" Permutation of matrix <matrix> from start index to
		j index where matrix[j][i] not null

	"""

	A = matrix
	n = len(A)
	i = start
	L = auxiliars_matrix

	if A not in L:
		L.append(A)

	id_of_max = i

	# search index of max pivot absolute value
	for j in range(i + 1, n):
		if A[j][i] and A[j][i] > abs(A[id_of_max][i]):
			id_of_max = j

	if id_of_max != i:
		# permutation
		for mt in L:
			mt[i], mt[id_of_max] = mt[id_of_max], mt[i]
		return 1
	else:
		return 0