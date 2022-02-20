#! /usr/bin/env python3

from zeros import *
from utils.graph import graph
from utils.functions import getFunction, subIntervals
from utils.Class import *
from math import log10
import sys

def getData():
	try:
		a = float(input("a: "))
		b = float(input("b: "))
		x0 = float(input("x0: "))
		epsilon = float(input("ϵ (<= 10e-1): "))

		if epsilon > 0.1:
			raise ValueError("Error: epsilon must be <= 0.1")
		

	except ValueError as msg:
		print(Color.danger(f"Wrong data: {msg}"))
		print()

		return getData()

	return a, b, x0, epsilon

def main(useFile=False):
	if useFile:
		sys.stdin = open("tests/filesInput/main.txt")

	print(Style.bold(Color.success("Search solution of f(x) = 0 in interval [a, b].")))
	print()

	f = getFunction()
	# F = lambda x: f(x) + x
	F = getFunction("F")

	a, b, x0, epsilon = getData();

	print()

	if a > b:
		print(f"Swap a and b: [{a}, {b}] -> [{b}, {a}]")
		print()
		a, b = b, a

	solutions = []
	intervals = subIntervals(f, a, b)

	# if len(intervals) > 1:
	# 	print(Color.warning(f"Subdivision of interval [{a}, {b}] to {intervals}"))
	# 	print()

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

	# Print Solutions

	nb_sol = len(solutions)

	print("Number of solutions: ", nb_sol)
	print()

	for i, solution in enumerate(solutions):
		print(Style.underline(f"Interval {i + 1}:"), f"({intervals[i][0]:.3f}, {intervals[i][1]:.3f})")

		for name, sol in solution.items():
			print(f"{name.capitalize()}: {sol}") 

		print()


	# GRAPHIC ZONE

	show_graphic = input("\nShow graphic ? (yes): ") or "yes"

	if show_graphic.lower() in ["yes", "y", "oui", "o"]:
		try:
			graph(f, a, b, points=[sol["newton"] for sol in solutions])
		except:
			pass

if __name__ == "__main__":
	try:
		main()
	except KeyboardInterrupt:
		pass
	except:
		print(Color.danger("Error while programm runnning"))
		print(Color.danger("Veirify if [a, b] in function Domain interval"))