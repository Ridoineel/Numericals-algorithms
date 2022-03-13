#! /usr/bin/env python3

from numpy.linalg import solve
from polyno import Poly

from utils.functions import *

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

				if x_k == x_i:
					print("Erreur: Surjection, deux points différents ont les mm x")
					exit()

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

cache = dict()
def cn(points):
	""" newtone polynomial coefficient 

	"""

	if len(points) == 1:
		y = points[0][1]

		return y

	if hashList(points) not in cache:
		x_0 = points[0][0]
		x_p = points[-1][0]

		a_i = (cn(points[:-1]) - cn(points[1:]))/(x_0 - x_p)

		cache[hashList(points)] = a_i

		return a_i
	else:
		return cache[hashList(points)]

def newton(points):
	n = len(points)
	x_0 = points[0][0]

	P = Poly() # P(x) = 0
	tmp_poly = Poly({0:1}) # tmp_poly(x) = 1

	for i in range(n):
		x_i = points[i][0]
		a_i = cn(points[:i + 1])
		
		P += a_i*tmp_poly

		# multiplicate last tmp_poly with (x - x_i)
		tmp_poly *= Poly({1:1, 0: -x_i}) # (x - x_i)
	
	return P

def moindreCarre(points, deg):
	n = len(points)

	if n <= deg:
		return -1

	P = [[] for i in range(deg + 1)] # matrix
	B = [0]*(deg + 1)   # vector 

	# Matrix P
	for i in range(deg*2, deg - 1, -1):
		for j in range(deg + 1):
			k = i - j
			S = sum(x**k for x, y in points)
			
			P[j].append(S)

	# Vector B
	for i in range(deg + 1):
		B[i] = sum(x**(deg - i) * y for x, y in points)

	A = solve(P, B)

	# polynomial according to vector A
	reversed_A = A[::-1]
	deg_coef = dict(enumerate(reversed_A))

	P = Poly(deg_coef)

	return P


def main():
	pass

if __name__ == '__main__':
	main()
	