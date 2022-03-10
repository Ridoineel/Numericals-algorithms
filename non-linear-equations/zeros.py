from utils.functions import derivative, inDomain

def dichotomie(f, a, b, prec=0.00001):
	if f(a) * f(b) > 0:
		return None

	zero_prec  = 10e-7

	while abs(a - b) > prec:
		if f(a) == 0: return a
		if f(b) == 0: return b

		m = (a + b)/2

		if not inDomain(f, m):
			return None

		if f(a) * f(m) < 0:
			b = m
		else:
			a = m

	if -zero_prec  <= f(a) <= zero_prec :
		return a

def secante(f, a, b, n=100, eps=10e-6):
	if f(a) * f(b) > 0:
		return None

	# swap a and b if f(b) <= 0 and f(a) > 0
	if (f(b) <= 0 and f(a) > 0):
		a, b = b, a

	converge = False
	zero_prec = 10e-7
	result = a

	for i in range(n):
		if f(b) == 0: return b
		if f(result) == 0: return result

		next_value = result - f(result) * (b - result)/(f(b) - f(result))

		if next_value == 0 or abs(next_value - result)/abs(next_value) < eps:
			result = next_value
			converge = True
			break
		else:
			result = next_value


	if converge and -zero_prec <= f(result) <= zero_prec:
		return result

def newton(f, x0, n=100, eps=10e-6, interval=[float("-inf"), float("inf")]):
	# if f(interval[0]) * f(interval[1]) > 0:
	# 	return None

	converge = False
	zero_prec = 10e-7
	result = x0

	for i in range(n):
		if not inDomain(f, result) or derivative(f, result) == 0:
			k, j = interval # [k, j]

			if result < k or result > j:
				result = (k + j)/2
			else: # k <= result <= j
				if k <= result + 0.1 <= j:
					result += 0.1
				else:
					result -= 0.1

			continue

		next_value = result - f(result)/derivative(f, result)

		if next_value == 0 or abs(next_value - result)/abs(next_value) < eps:
			result = next_value
			converge = True
			break
		else:
			result = next_value

	if converge and -zero_prec <= f(result) <= zero_prec:
		return result

def pointsFixes(g, x0, n=100, eps=10e-6):
	# if abs(derivative(g, x0)) > 1:
	# 	return "No convergence: |F'(x0)| > 1"

	for i in range(n):
		if not inDomain(g, x0):
			x0 += 0.001
			continue

		x1 = g(x0)

		if not inDomain(g, x1):
			x0 = x1 + 0.001
			continue

		x2 = g(x1)

		if x0 == x1 == x2: 
			# invariant, so return x0
			return x0

		if x2 - 2*x1 + x0 == 0:
			x0 = x2
			continue

		xe = x0 - ((x1 - x0)**2)/(x2 - 2*x1 + x0)
		
		if xe == 0 or abs(xe - x0)/abs(xe) < eps:
			return xe
		else:
			x0 = xe