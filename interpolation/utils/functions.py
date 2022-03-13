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