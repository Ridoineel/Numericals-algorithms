import sys
import os

sys.path.append(os.path.dirname(__file__))

from Class import Color, Style
from functions import printMatrix, printAandB

def outputController(func):
	def inner(A, B, **kwargs):
		X = func(A, B, **kwargs)
		
		if X == -1:
			print(Color.danger("Data error, verify A and B"))
			print()

			printAandB(A, B)
			exit(1)
		elif X == 0:
			print(Color.danger("A is not invertible matrix"))
			print()

			printAandB(A, B)
			exit(1)
		else:
			return X

	return inner