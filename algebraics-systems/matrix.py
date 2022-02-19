from utils.functions import isMatrix, permutation

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

	def decompose(self, method="crout"):
		if method == "crout":
			return self.crout()
		elif method == "cholesky":
			return self.cholesky()

	def crout(self):
		""" Crout decompositon on square matrix A
			Value to return:
				° Vectors L, U and O: if success
				° 0: if A is not invertible matrix

		""" 

		A = self
		n = len(A)

		# Initialize L, U and O (O is permutation vector)
		L = [[0]*n for i in range(n)]
		U = [[0]*i + [1] + [0]*(n - i - 1)  for i in range(n)]
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
			if L[i][i] == 0 and not permutation(L, 0, auxiliars_matrix=[A, O]):
				return 0

			# line Ui: U[i][j], j > i
			for j in range(i + 1, n):
				U[i][j] = (A[i][j] - sum(L[i][k]*U[k][j] for k in range(i)))/L[i][i]

		# Lnn
		L[n - 1][n - 1] = A[n - 1][n - 1] - sum(L[n - 1][k]*U[k][n - 1] for k in range(n - 1))
		
		return L, U, O

	def cholesky(self):
		pass

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

def main():
	A = Matrix([[1, 2, 3], [1, 2, 4]])
	B = Matrix([[4, 5, 6], [0, 0, 0]])

	A.extend(B)

	A.print()

if __name__ == '__main__':
	main()
