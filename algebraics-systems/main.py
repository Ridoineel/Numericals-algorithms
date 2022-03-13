#! /usr/bin/env python3

import sys
from algsys import *
from utils.matrix import Matrix

sys.stdin = open("data/input.txt", "r")

func = {
	"Gauss": gauss, 
	"Gauss-Jordan": gaussJordan, 
	"LU": lu,
	"Cholesky": lambda A, B, raised: lu(A, B, raised=raised, decomp_method="cholesky"), 
	"JACCOBI": jacobi, 
	"Gauss-Seidel": gaussSeidel,
	"Thomas": thomas
}

def main():
	n = int(input())

	A = list()

	for i in range(n):
		A.append([float(j) for j in input().split()])
	
	A = Matrix(A)

	B = [float(i) for i in input().split()]
	
	for name, algo in func.items():
		# print(A)
		X = algo(Matrix(A.copy()), B.copy(), raised=0)

		print(f"{name}: {X}")
		print()

if __name__ == '__main__':
	main()