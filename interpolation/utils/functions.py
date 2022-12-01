import sys
from os.path import dirname, join

sys.path.append(dirname(dirname(__file__)))

_dirname = dirname(__file__)
_parent_dirname = dirname(_dirname)

def prod(L):
	product = 1

	for i in L:
		product *= i

	return product

def hashList(L):
	""" hash list type to String 
		mapping all list elements

	"""

	L_string = [str(i) for i in L]

	return ",".join(L_string)

def genGeoGebraData(points, newton_f, lagrange_f, moindrec_f):
	""" This function write 
		text data of functions (newton, lagrange, moindrec)
		in the file data/data_geogeb.txt
		
		example of the content of data/data_geogeb.txt:

			Newton(x) = x^3 - 1
			Lagrange(x) = x^3 - 1
			MoindreCarre(x) = 7x - 1
			Points = {(-3.0, -28.0), (-2.0, -9.0), (-1.0, -2.0), (0.0, -1.0), (1.0, 0.0), (2.0, 7.0), (3.0, 26.0)}
	"""
	
	points_toString = ", ".join([t.__str__() for t in points])
	points_toString = "Points = {" + points_toString + "}"

	data = list()

	data.append(f"Newton(x) = {newton_f}")
	data.append(f"Lagrange(x) = {lagrange_f}")
	data.append(f"MoindreCarre(x) = {moindrec_f}")
	data.append(points_toString)

	with open(join(_parent_dirname, "data/data_geogeb.txt"), "w") as file:
		for line in data:
			file.write(line + "\n\n")