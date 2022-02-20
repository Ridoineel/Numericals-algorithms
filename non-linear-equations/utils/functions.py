from math import *
import numpy as np
import re
import os
import sys

cos = np.cos
sin = np.sin
tan = np.tan

sys.path.append(os.path.dirname(__file__))

from Class import *

def derivative(f, x, precision=10e-10):
	return (f(x + precision) - f(x))/precision

def tagente(f, x, a):
	return derivative(f, a)*(x - a) + f(a)

def functionsEval(func_list, x):
	""" return f1°f2°...°fn (x) """

	value = x

	for func in reversed(func_list):
		value = func(value)

	return value

def derivativeCompose(func_list, x):
	""" derivativeation of f1°f2°...°fn (x) """

	if len(func_list) == 2:
		# f1°f2
		f1, f2 = func_list

		return derivative(f2, x) * derivative(f1, f2(x))
	else:
		# f1°f2°f3°...°fn
		f1 = func_list[0]
		others_func = func_list[1:]

		return derivativeCompose(others_func, x) * derivative(f1, functionsEval(others_func, x))

def getFunction(func="f", nb_var=1):
	variables = ["x", "y", "z", "k", "m", "t"]
	utilVariables = variables[:nb_var]
	utilVarToString = ", ".join(utilVariables)

	expression = input(Style.bold(f"{func}({utilVarToString}): "))

	# replace ^ by **
	expression = expression.replace("^", "**")

	# replace ln by log10
	expression = expression.replace("ln", "log10")

	# replace implicit multiplication to explicit multiplication: 
	# ex: 12x + 2y -> 12*x + 2*y
	expression = re.sub(rf"([0-9])({''.join(utilVariables)})", r"\1*\2", expression)

	try:
		f = eval(f"lambda {utilVarToString}: {expression}")
		f(1)
	except SyntaxError:
		print(Style.bold(Color.danger("Incorrect expression !: Invalid Syntax")))
		print()

		return getFunction(func, nb_var)
	except NameError:
		print(Style.bold(Color.danger("Incorrect expression !")))
		print()

		return getFunction(func, nb_var)

	return f

def subIntervals(f, a, b, pas=0.001, eps=10e-4):
	intervals = []
	i = a

	while i <= b:
		if -eps <= derivative(f, i) <= eps:
			if not intervals: # intervals is emptys
				if i != a:
					intervals.append((a, i))
			elif i != intervals[-1][1] + pas:
					# add (last of last interval + pas, i)
					new_inter = (intervals[-1][1] + pas, i)

					intervals.append(new_inter)
					
		i += pas

	if intervals and intervals[-1][1] + pas != b:
		# add last with b
		intervals.append((intervals[-1][1] + pas, b))
	else:
		intervals = [(a, b)]

	return intervals


def main():
	g = lambda x: 3*x**2 + 1
	f = lambda x: x**2
	h = lambda x: x**3
	k = lambda x: x/2

	print(derivativeCompose([g, f, h, k], 2))

if __name__ == "__main__":
	main()