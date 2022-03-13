
def pointsFixes(g, x0, n=100, eps=10e-4):
	# if abs(derivative(g, x0)) > 1:
	# 	return "No convergence: |F'(x0)| > 1"

	for i in range(n):
		# if not inDomain(g, x0):
		# 	x0 += 0.001
		# 	continue



		x1 = g(x0)

		# if not inDomain(g, x1):
		# 	x0 = x1 + 0.001
		# 	continue

		x2 = g(x1)

		return x2

		print()
		# print(x2)
		# print(x1)

		if (x0 - x1).any() == 0 and (x0 - x2).any() == 0: 
			# invariant, so return x0
			return x0

		if (x2 - 2*x1 + x0).any() == 0:
			x0 = x2
			continue

		xe = x0 - ((x1 - x0)**2)/(x2 - 2*x1 + x0)
		print(xe)
		x0 = xe

		# converge = True

		# for j in range(len(xe)):
		# 	if abs(xe[j] - x0[j])/abs(xe[j]) >= eps:
		# 		converge = False
		# 		break

		# if xe.any() == 0 or converge:
		# 	return xe
		# else:
		# 	x0 = xe

	return xe