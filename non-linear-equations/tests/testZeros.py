import unittest
import os
import sys
from math import *

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from zeros import *

output = True

class TestPointsFixes(unittest.TestCase):
	def test1(self):
		g = lambda x: exp(-x)
		eps = 10e-6
		sol = 0.5671433
		solFromG = pointsFixes(g, 0.1, 100, eps)

		if output:
			print("test1: ", solFromG)

		self.assertTrue(sol - eps <= solFromG <= sol + eps)

	def test2(self):
		g = lambda x: 1/x
		eps = 10e-6
		sol = [-1, 1]
		solFromG1 = pointsFixes(g, -0.1, 100, eps)
		solFromG2 = pointsFixes(g, 0.1, 100, eps)

		if output:
			print("test2: ", solFromG1, solFromG2)
		
		self.assertTrue(sol[0] - eps <= solFromG1 <= sol[0] + eps  and
						sol[1] - eps <= solFromG2 <= sol[1] + eps)

	def test3(self):
		g = lambda x: (x - 1)/(x + 1)
		eps = 10e-6
		sol = 0.5671433
		solFromG = pointsFixes(g, 0.1, 1000, eps)

		if output:
			print("test3: ", solFromG)

		self.assertTrue(solFromG == None)

	def test4(self):
		g = lambda x: sqrt(2*x + 3)
		eps = 10e-6
		sol = [-1, 3]
		solFromG1 = pointsFixes(g, 4, 100, eps)

		if output:
			print("test4: ", solFromG1)
		
		self.assertTrue(sol[0] - eps <= solFromG1 <= sol[0] + eps  or 
						sol[1] - eps <= solFromG1 <= sol[1] + eps)

	def test5(self):
		g = lambda x: (x**2 - 3)/2
		eps = 10e-6
		sol = [-1, 3]
		solFromG1 = pointsFixes(g, 4, 100, eps)

		if output:
			print("test5: ", solFromG1)
		
		self.assertTrue(sol[0] - eps <= solFromG1 <= sol[0] + eps  or 
						sol[1] - eps <= solFromG1 <= sol[1] + eps)

	def test6(self):
		g = lambda x: 3/(x - 2)
		eps = 10e-6
		sol = [-1, 3]
		solFromG1 = pointsFixes(g, 4, 100, eps)

		if output:
			print("test6: ", solFromG1)
		
		self.assertTrue(sol[0] - eps <= solFromG1 <= sol[0] + eps  or 
						sol[1] - eps <= solFromG1 <= sol[1] + eps)

class TestNewton(unittest.TestCase):

	def test1(self):
		f = lambda x: x**2 - 1
		x0 = 0
		sol = [-1, 1]
		solFromFunc = newton(f, x0, 1000)

		if output:
			print("test1: ", solFromFunc)
		
		self.assertIn(solFromFunc, sol)

	def test2(self):
		f = lambda x: (x - 1)/(x + 1)
		x0 = 3
		sol = 1
		solFromFunc = newton(f, x0, 1000)

		if output:
			print("test2: ", solFromFunc)
		
		self.assertEqual(solFromFunc, sol)

# unittest.main()
