from math import *
import re
import os
import sys
import time

sys.path.append(os.path.dirname(__file__))

from Class import *

def derivative(f, x, precision=10e-4):
	if inDomain(f, x) and inDomain(f, x  + precision):
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
	expression = re.sub(rf"([0-9])([{''.join(utilVariables)}])", r"\1*\2", expression)

	try:
		f = eval(f"lambda {utilVarToString}: {expression}")
		f(1)
	except SyntaxError:
		print(Style.bold(Color.danger("L'expression est invalide")))
		print()

		return getFunction(func, nb_var)
	except NameError:
		print(Style.bold(Color.danger("L'expression est invalide")))
		print()

		return getFunction(func, nb_var)
	except:
		pass

	return f

def inDomain(f, x):
	try:
		f(x)
	except:
		return False
	else:
		return True

def subIntervals(f, a, b, step=0.00001):
	step = max(step, 0.00001)
	intervals = []
	i = a

	while i <= b:
		a1 = i 
		b1 = i + step

		if inDomain(f, a1) and inDomain(f, b1) and (f(a1) * f(b1) <= 0):
			intervals.append([a1, b1])

		i += step

	return intervals

## Fun
def extinction():
	os.system("clear")

	print(Style.bold(Color.primary("Désolé mec (meuf).")))
	print(Color.primary("Pour avoir saisie des données invalides, l'ordinateur va s'éteindre."))

	time.sleep(4.5)

	os.system("clear")

	for i in range(1, 6):
		text = Style.bold(Color.primary("dans: "))

		time_text = Color.warning(f"{i:02}s")

		if i != 5:
			time_text = Style.blink(time_text) 
		
		text += time_text

		print(text)

		if i == 5:
			time.sleep(2)
		else:
			time.sleep(1)

		os.system("clear")

	print(Style.bold(
			Color.success(
				"Merci de réesayer après avoir redémarrer l'ordinateur."
			)
		)
	)

	time.sleep(3)
	
	os.system("poweroff")


def main():
	g = lambda x: 3*x**2 + 1
	f = lambda x: x**2
	h = lambda x: x**3
	k = lambda x: x/2

	print(derivativeCompose([g, f, h, k], 2))

if __name__ == "__main__":
	main()