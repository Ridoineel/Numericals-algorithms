#! /usr/bin/env python3

from zeros import *
from utils.functions import getFunction, subIntervals, inDomain
from utils.Class import *
from math import log10
import sys

def main(useFile=False):
	if useFile:
		sys.stdin = open("tests/filesInput/main.txt")

	print(Style.underline(
			Style.bold(
				Color.success(
					"		Résolution d'une équation de la forme f(x)=0"
				)
			)
		)
	)

	print()

	print(Color.success("Saisir les fonctions f et F (x=F(x)):"))
	f = getFunction()
	F = getFunction("F")

	a, b, x0, eps = getData();

	print()
	
	intervals = subIntervals(f, a, b, step=eps*10)
	
	solutions = {
		"dichotomie": set(),
		"secante": set(),
		"newton": set(),
		"points fixes": set()
	}
	
	### Dichotomie and secante ###

	for interval in intervals.copy():
		a1, b1 = interval

		if f(a1) * f(b1) <= 0:
			dich_sol = dichotomie(f, a1, b1, eps)
			sec_sol = secante(f, a1, b1)

			if dich_sol != None:
				dich_sol = round(dich_sol, 8)

				if float(dich_sol).is_integer():
					dich_sol = int(dich_sol)

				solutions["dichotomie"].add(dich_sol)
			
			if sec_sol != None:
				sec_sol = round(dich_sol, 8)
				
				if float(sec_sol).is_integer():
					sec_sol = int(sec_sol)

				solutions["secante"].add(sec_sol)

	##############################

	## Newton and Points Fixes ##

	N = 100
	newton_sol = newton(f, x0, N, eps) 
	pf_sol = pointsFixes(F, x0, N, eps)

	if newton_sol == None:
		newton_sol = Color.warning("Convergence non atteinte.")
	else:
		newton_sol = round(newton_sol, 8)

		if float(newton_sol).is_integer():
			newton_sol = int(newton_sol)

	if pf_sol == None:
		pf_sol = Color.warning("Convergence non atteinte.")
	else:
		pf_sol = round(pf_sol, 8)
				
		if float(pf_sol).is_integer():
			pf_sol = int(pf_sol)


	solutions["newton"].add(newton_sol)
	solutions["points fixes"].add(pf_sol)

	#############################

	# Print Solutions

	for name, sols in solutions.items():
		if not sols: 
			sols = "Aucune solution trouvé"
		else:
			sols = " et ".join(map(str, sorted(sols)))

		print(f"{Style.bold(name.capitalize())}: {sols}") 
		print()

def getData():
	print(Color.success("\nSaisir les données a, b, x0 et epsilon (critère d'arrêt)"))
	
	try:
		a = float(input(Style.bold("a: ")))
		b = float(input(Style.bold("b: ")))
		x0 = float(input(Style.bold("x0: ")))
		eps = float(input(Style.bold("ϵ (precision, <= 0.1): ")))
		
		print()

		if eps > 0.1:
			raise ValueError("ϵ doit être inférieur à 0.1")

	except ValueError as msg:
		print(Color.danger(f"\nErreur lors de la saisie des données: {msg}"))
		print()

		return getData()

	if a > b:
		print(Color.warning(f"Attention l'interval saisie est [{a}, {b}] !"))
		
		confirm = input( f"Vouliez vous continuer avec [{b}, {a}] ?: ")
		confirm = confirm.lower() in ["yes", "y", "o", "oui"]

		if confirm:
			# swap a and b
			a, b = b, a
		else:
			return getData()

	return a, b, x0, eps

if __name__ == "__main__":
	main(1)