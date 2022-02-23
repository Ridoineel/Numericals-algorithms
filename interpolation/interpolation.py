import os
import sys

sys.path.append("/home/ridoineel/Dev/Polynomials")

from polynomials import Poly

from utils.functions import prod
from utils.graph import graph

def lagrange(points):
	n = len(points)
	L = [None for i in range(n)]
	P = Poly()

	for i in range(n):
		x_i = points[i][0]
		tmp_poly = Poly({0:1})

		for pt in points:
			if pt != points[i]:
				x_k = pt[0] # k != i

				# x - x_k -> Poly({0:-x_k, 1:1})
				num = Poly({0:-x_k, 1:1})

				# so, (x - x_k)/(x_i - x_k) -> num/(x_i - x_k)
				# 
				tmp_poly *= num/(x_i - x_k)

		L[i] = tmp_poly

	# With L polynomials, calculate (search) P
	for i in range(n):
		y_i = points[i][1]
		P += y_i * L[i]

	return P

def newton(points):
	pass

def main():
	points = [(0, -1), (-1, 0), (1, 0)]

	f = lagrange(points)


	f_ndarray = lambda values: [f.eval(i) for i in values]
	graph(f_ndarray, -5, 5)

if __name__ == '__main__':
	main()