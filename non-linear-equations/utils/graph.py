import os
import numpy as np
import matplotlib.pyplot as plt
import sys

sys.path.append(os.path.dirname(__file__))

from functions import derivative

def graph(f, start=0, end=100, step=0.01, color="blue", deriv=False, points=[]):
	x = np.arange(start, end, step)
	x_abs = np.arange(start, end, step)
	points = np.array(points)

	# fig, ax = plt.subplots()
	# ax.set_ylim(-20, 20)

	# function f
	plt.plot(x, f(x), label="f(x)", c=color)

	# points
	if points.size:
		plt.scatter(points, f(points), label="f(x) = 0")

	# derivatve
	if deriv:
		plt.plot(x, derivative(f, x), label="f'(x)")

	# y = 0
	plt.plot(x_abs, [0] * len(x_abs), label="(D): y = 0")

	plt.legend()

	plt.show()

def all_tangente(f, a_set):
	plt.scatter(a_set, [f(i) for i in a_set], c="red")

	x = np.arange(0, 100, 0.01)

	for a in a_set:
		x = np.arange(0, 10, 0.01)
		plt.plot(x, tagente(f, x, a), c="red")

def main():
	f = lambda x: (x + 1)/(x - 1)

	graph(f, -10, 10)

if __name__ == "__main__":
	main()