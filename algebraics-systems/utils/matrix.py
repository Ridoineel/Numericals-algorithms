import sys
import os
import numpy as np

sys.path.append(os.path.dirname(__file__))

from functions import isMatrix, permutation, triangulation

#	0: A is not invertible matrix
#	1: A is not symetric
#	2: A is not defined positve


class Matrix(list):
	def extend(self, B):
		# extend A with matrix B
		A = self
		matrix = []

		if len(B) != len(A):
			raise ValueError("ddd")

		# concatenate A and B -> matrix
		for i in range(len(A)):
			A[i] += B[i]

	def det(self):
		return np.linalg.det(self)

	def decompose(self, method="crout"):
		methods = {
			"crout": self.crout,
			"cholesky": self.cholesky,
			"DLU": self.DLU
		}

		if method in methods:
			return methods[method]()

	def crout(self):
		""" Crout decompositon on square matrix A
			Value to return:
				° Vectors L, U and O: if success
				° 0: if A is not invertible matrix

		""" 

		A = self
		n = len(A)

		# Initialize L, U and O (O is permutation vector)
		L = Matrix([[0]*n for i in range(n)])
		U = Matrix([[0]*i + [1] + [0]*(n - i - 1)  for i in range(n)])
		O = list(range(n))

		# Find first column of L
		for i in range(n):
			L[i][0] = A[i][0]
		
		## permutation if the pivot is null
		if L[0][0] == 0 and not permutation(L, 0, auxiliars_matrix=[A, O]):
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
			if L[i][i] == 0 and not permutation(L, i, auxiliars_matrix=[A, O]):
				return 0

			# line Ui: U[i][j], j > i
			for j in range(i + 1, n):
				S = sum(L[i][k]*U[k][j] for k in range(i))
				U[i][j] = (A[i][j] - S)/L[i][i]

		# Lnn
		L[n - 1][n - 1] = A[n - 1][n - 1] - sum(L[n - 1][k]*U[k][n - 1] for k in range(n - 1))
		
		return L, U, O

	def cholesky(self):
		A = self
		n = len(A)

		if not A.isSymetric():
			return 1

		L = Matrix([[0]*n for i in range(n)])
		Lt = Matrix([[0]*n for i in range(n)])
		O = list(range(n))

		## permutation if the pivot is null
		if A[0][0] == 0 and not permutation(A, 0, auxiliars_matrix=[O]):
			return 0

		for i in range(n):
			# pivot
			S = sum(L[i][k]**2 for k in range(i))
			L[i][i] = (A[i][i] - S)**0.5
			Lt[i][i] = L[i][i]

			# if Lii is complex, 
			# A is not defined positive
			if isinstance(L[i][i], complex) or not L[i][i]:
				return 2
				

			# column i of L and line i of Lt
			for j in range(i + 1, n):
				S = sum(L[i][k]*L[j][k] for k in range(i))

				# Lji value
				L[j][i] = (A[i][j] - S)/L[i][i]

				#Lt_ij value
				Lt[i][j] = L[j][i]

		return L, Lt, O

	def DLU(self):
		A = self
		n = len(A)

		D = Matrix([[0]*n for i in range(n)])
		L = Matrix([[0]*n for i in range(n)])
		U = Matrix([[0]*n for i in range(n)])

		for i in range(n):
			for j in range(n):
				if i == j:
					D[i][i] = A[i][i]
				elif i < j:
					U[i][j] = A[i][j]
				else:
					L[i][j] = A[i][j]

		return D, L, U

	def transpose(self):
		A = self.copy()

		for i in range(len(A)):
			for j in range(i + 1, len(A)):
				A[i][j], A[j][i] = A[j][i], A[i][j]

		return A

	def print(self):
		if not isMatrix(self):
			return None

		for i in range(len(self)):
			print("|", *[a.rjust(5) for a in map(str, self[i])])
		
		print()

	def isSquareMatrix(self):
		A = self

		if not A:
			return False

		nb_lines = len(A)

		for line in A:
			if type(line) != list or len(line) != nb_lines:
				return False

		return True

	def isDominantDiagonal(self):
		A = self
		n = len(A)
		res = True

		i = 0
		while res and i < n:
			S = sum(abs(A[i][j]) for j in range(n) if j != i)

			if abs(A[i][i]) < S:
				res = False

			i += 1

		return res

	def istridiagonal(self):
		A = self
		n = len(A)
		res = True

		for i in range(n):
			# check if any value not in tridiagonal range 
			# is 0

			allisnull = bool()

			if i == 0:
				allisnull = not any(A[0][2:])
			elif i == n - 1:
				allisnull = not any(A[-1][:-2])
			else:
				allisnull = not any(A[i][:i - 1] + A[i][i + 2:])

			if not allisnull:
				res = False
				break

		return res

	def isSymetric(self):
		A = self
		n = len(A)
		res = True

		for i in range(n):
			for j in range(i + 1, n):
				if A[i][j] != A[j][i]:
					res = False
					break

		return res

	def isInvertible(self):
		A = [i.copy() for i in self]

		if triangulation(A):
			return True
		else:
			return False


	def isDefinedPositive(self):
		A = self
		n = len(A)

		

		# for i in range(n):
		# 	N = i 
		# 	for k in range(n):
		# 		pass
		# 	for j in range(n - N):
		# 		print((j, j), (N + j, N + j))
		# 		# print(i + 1, (j, i + j))

		return True

	def __add__(self, M):
		A = self
		n = len(A)

		S = Matrix([[0]*n for i in range(n)])

		# print(A)
		# print(M)
		for i in range(n):
			for j in range(n):
				S[i][j] = A[i][j] + M[i][j]

		return S

	def __radd__(self, M):
		return self.__add__(M)

	def __mul__(self, M):
		A = self
		n = len(A)
		col_A = len(A[0])



		S = Matrix([[0]*n for i in range(n)])

		if M.__class__.__name__ in ["int", "int64", "float", "float64"]:
			for i in range(n):
				for j in range(n):
					S[i][j] = A[i][j]*M
		elif isinstance(M, list) and not isinstance(M[0], list):
			S = [0]*n
			m = len(M)

			for i in range(n):
				s = 0
				for j in range(m):
					s += A[i][j] * M[j]

				S[i] = s

			return S
		else:	
			m = len(M)
			col_B = len(M[0])

			if col_A != m:
				raise ValueError("A nb columns != B nb lines")
			
			for i in range(n):
				for j in range(col_B):
					s = 0
					for k in range(m):
						s += A[i][k] * M[k][j]

					S[i][j] = s

		return S

	def __rmul__(self, M):
		return self.__mul__(M)

	def __neg__(self):
		return -1 * self

def main():
	A = Matrix([
		[1, -1, 2], 
		[-1, 5, -4],
		[2, -4, 6]
	])

	L, Lt, O = A.decompose(method="cholesky")

	L.print()
	Lt.print()

	

if __name__ == '__main__':
	main()
