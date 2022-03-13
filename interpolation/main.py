import matplotlib.pyplot as plt
import sys

from interpolation import *
from utils.functions import genGeoGebraData

sys.stdin = open("data/input.txt", "r")

def main():
	n = int(input())

	points = [tuple(map(float, input().split())) for i in range(n)]
	p = 2
	
	f1 = lagrange(points)
	f2 = newton(points)
	f3 = moindreCarre(points, p)

	print(f"Lagrange: f(x) = {f1}")
	print(f"Newton: f(x) = {f2}")
	print(f"Moindre carré: f(x) = {f3} , p={p}")

	genGeoGebraData(points, newton_f=f2, lagrange_f=f1, moindrec_f=f3)

if __name__ == '__main__':
	main()