import sys
import os

sys.path.append(os.path.dirname(__file__))

from Class import Color, Style
from functions import printMatrix, printAandB

#	-1: A is not square mat
#	-2: B is not vector
#	-3: len(A) != len(B)
#	0: A is not invertible matrix
#	1: A is not symetric
#	2: A is not defined positve
#	3: A is not dominant diagonal matrix
#	4: A is not tridiagonal matrix
# 	5: Lii = 0 while thomas running
#	Vector X (list): if success


def outputController(func):
	def inner(A, B, raised=True, **kwargs):
		X = func(A, B, **kwargs)

		if isinstance(X, list):
			X = [0.0 if i == -0.0 else i for i in X]

			return X
		else:
			err_code = X
			error_messages = {
				-1: "A n'est pas une matrice carrée.",
				-2: "B n'est pas un vecteur.",
				-3: "Le nombre de ligne de A est différent de celle de B.",
				0: "A n'est pas une matrice inversible.",
				1: "A n'est pas une matrice symétrique.",
				2: "A n'est pas définie positive.",
				3: "A n'est pas diagonale dominante.",
				4: "A n'est pas une matrice tridiagonale.",
				5: "Lii == 0 a été rencontré dans la résolution \n avec l'algorithme de Thomas"
			}

			msg = error_messages[err_code]

			if raised:
				raise ValueError(msg)
			else:
				return Color.danger(msg)
			

	return inner