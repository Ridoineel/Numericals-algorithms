#! /usr/bin/env python3

from utils.graph import graph
from utils.functions import getFunction, derivative, subIntervals
from utils.Class import *
from math import log10
import sys

#sys.stdin = open("tests/filesInput/main.txt")

def dichotomie(f, a, b, prec=0.00001):
	if f(a) * f(b) > 0:
		return None

	while abs(a - b) > prec:
		if f(a) == 0: return a
		if f(b) == 0: return b

		m = (a + b)/2

		if f(a) * f(m) < 0:
			b = m
		else:
			a = m

	# exp = -int(log10(prec)/log10(10))

	# return float(format(a, f".{exp}f"))

	return a

def secante(f, a, b, n=1000):
	if f(a) * f(b) > 0:
		return None

	# swap a and b if f(b) <= 0 and f(a) > 0
	if (f(b) <= 0 and f(a) > 0):
		a, b = b, a

	result = a

	for i in range(n):
		if f(b) == 0: return b
		if f(result) == 0: return result

		next_value = result - f(result) * (b - result)/(f(b) - f(result))

		if result != next_value:
			result = next_value
		else:
			break

	return result

def newton(f, x0, n=1000, interval=[float("-inf"), float("inf")]):
	if f(interval[0]) * f(interval[1]) > 0:
		return None

	result = x0

	for i in range(n):
		if derivative(f, result) == 0:
			k, j = interval # [k, j]

			if result < k or result > j:
				result = (k + j)/2
			else: # k <= result <= j
				if k <= result + 0.1 <= j:
					result += 0.1
				else:
					result -= 0.1

			continue

		next_value = result - f(result)/derivative(f, result)

		if result != next_value:
			result = next_value
		else:
			break

	if result > interval[1] or result < interval[0]:
		return None
	else:
		return result

def pointsFixes(g, x0, n=1000, epsilon=10e-6):
	for i in range(n):
		x1 = g(x0)
		x2 = g(x1)

		if x0 == x1 == x2: 
			# invariant, so return x0
			return x0

		if x2 - 2*x1 + x0 == 0:
			x0 = x2
			continue

		xe = x0 - ((x1 - x0)**2)/(x2 - 2*x1 + x0)

		if xe == 0 or abs(xe - x0)/abs(xe) < epsilon:
			return xe
		else:
			x0 = xe

	return None

def getData():
	try:
		a = float(input("a: "))
		b = float(input("b: "))
		x0 = float(input("x0: "))
		epsilon = float(input("ϵ (<= 10e-1): "))

		if epsilon > 0.1:
			raise ValueError("Error: epsilon must be <= 0.1")
		if (a <= b and (x0 < a or x0 > b)) or ( a > b and (x0 < b or x0 > a)):
			raise ValueError("Error: x0 must be in [a, b]")

	except ValueError as msg:
		print(Color.danger(f"Wrong data: {msg}"))
		print()

		return getData()

	return a, b, x0, epsilon

def main():
	print(Style.bold(Color.success("Search solution of f(x) = 0 in interval [a, b].")))
	print()

	f = getFunction()
	F = lambda x: f(x) + x
	# F = getFunction("F")

	a, b, x0, epsilon = getData();

	print()

	if a > b:
		print(f"Swap a and b: [{a}, {b}] -> [{b}, {a}]")
		print()
		a, b = b, a

	solutions = []
	intervals = subIntervals(f, a, b)

	if len(intervals) > 1:
		print(Color.warning(f"Subdivision of interval [{a}, {b}] to {intervals}"))
		print()

	for interval in intervals.copy():
		a1, b1 = interval

		if f(a1) * f(b1) <= 0:
			dichotomie_sol = dichotomie(f, a1, b1, epsilon) or f"No solution in [{a1}, {b1}]"
			newton_sol = newton(f, x0, interval=[a1, b1]) or f"No solution in [{a1}, {b1}] with x0={x0}"
			secante_sol = secante(f, a1, b1) or f"No solution in [{a1}, {b1}]"

			try:
				pf_sol = pointsFixes(F, x0) or f"No solution with x0={x0}"
			except:
				print(Color.danger("Error with points fixe: Domain error"))
				exit()

			solutions.append({
				"newton": newton_sol,
				"dichotomie": dichotomie_sol,
				"secante": secante_sol,
				"points fixes": pf_sol
			})
		else:
			intervals.remove(interval)

	print(intervals)

	# Print Solutions

	nb_sol = len(solutions)

	print("Number of solution: ", nb_sol)
	print()

	for i, solution in enumerate(solutions):
		print(Style.underline(f"Interval {i + 1}:"), f"({intervals[i][0]:.3f}, {intervals[i][1]:.3f})")

		for name, sol in solution.items():
			if sol.is_integer(): sol = int(sol)

			print(f"{name.capitalize()}: {sol}") 

		print()


	# GRAPHIC ZONE

	show_graphic = input("\nShow graphic ? (yes): ") or "yes"

	if show_graphic.lower() in ["yes", "y", "oui", "o"]:
		graph(f, a, b, points=[sol["newton"] for sol in solutions])

		# if len(intervals) > 1:
		# 	print("Close current graphical window to access next graphic\n")

		# for i, interval in enumerate(intervals):
		# 	a, b = interval

		# 	print(f"Graphic {i + 1} for interval [{a:.3f}, {b:.3f}]")
		# 	graph(f, a, b, points=[solutions[i]["newton"]])
	
if __name__ == "__main__":
	try:
		main()
	except KeyboardInterrupt:
		pass
	except:
		print(Color.danger("Error while programm runnning"))
		print(Color.danger("Veirify if [a, b] in Domain interval"))
