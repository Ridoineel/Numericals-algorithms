from itertools import combinations

def isMatrix(A):
	if not A:
		return False

	if not isinstance(A[0], list):
		return False

	nb_cols = len(A[0])

	for L in A:
		if not isinstance(L, list) or len(L) != nb_cols:
			return False

		for i in L:
			if not isinstance(i, int) and not isinstance(i, float):
				return False

	return True

def isVector(B):
	if not isinstance(B, list):
		return False

	for i in B:
		if not isinstance(i, int) and not isinstance(i, float):
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

def permutation(matrix, start: int, auxiliars_matrix=[], withmax=True):
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

			if not withmax:
				break

	# printMatrix(A)
	# printMatrix([auxiliars_matrix])
	if id_of_max != i:
		# permutation
		for mt in L:
			mt[i], mt[id_of_max] = mt[id_of_max], mt[i]
		return 1
	else:
		return 0

def setBestPermutation(A, auxiliars_matrix=[]):
	""" best permutation of A 
		where all pivot != 0

	"""

	def isRight(A):
		result = True

		for i in range(len(A)):
			if A[i][i] == 0:
				result = False
				break

		return result

	n = len(A)
	L = [A] + auxiliars_matrix
	"""
	for i, j in combinations(range(n), 2):
		# if pivots not null
		if isRight(A):
			break


		for M in L:
			M[i], M[j] = M[j], M[i]

		# print(f"{i} <--> {j}")
		# printMatrix(A)

	"""
	for i in range(n):
		if A[i][i] == 0:
			for j in range(i + 1, n):
				if A[i][j] != 0:
					for M in L:
						M[i], M[j] = M[j], M[i]

					break

def printMatrix(A):
	if not isMatrix(A):
		return None

	for i in range(len(A)):
		print("|", *[a.rjust(5) for a in map(str, A[i])])
	
	print()

def printAandB(A, B):
	""" A is square matrix and B is vector """
	
	length_a = len(A)
	length_b = len(B)
	adjust_size = 4

	print("A".center(length_a*adjust_size), end="  ")
	print("B".center(adjust_size*3))
	print("-"*(length_a*adjust_size + adjust_size*3))

	for i in range(max(length_a, length_b)):
		if i < len(A):
			# print(*A[i], "|", end=" ")
			print(*[a.ljust(adjust_size) for a in map(str, A[i])], end="| ")
		if i < len(B):
			print(str(B[i]).rjust(adjust_size))
		print()