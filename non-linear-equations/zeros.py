from utils.functions import derivative

def dichotomie(f, a, b, prec=0.00001):
	if f(a) * f(b) > 0:
		return None

	while abs(a - b) > prec:
		if f(a) == 0: return a
		if f(b) == 0: return b

		m = (a + b)/2

		if f(a) * f(m) < 0:
			b = m
		else:
			a = m

	# exp = -int(log10(prec)/log10(10))

	# return float(format(a, f".{exp}f"))

	return a

def secante(f, a, b, n=1000):
	if f(a) * f(b) > 0:
		return None

	# swap a and b if f(b) <= 0 and f(a) > 0
	if (f(b) <= 0 and f(a) > 0):
		a, b = b, a

	result = a

	for i in range(n):
		if f(b) == 0: return b
		if f(result) == 0: return result

		next_value = result - f(result) * (b - result)/(f(b) - f(result))

		if result != next_value:
			result = next_value
		else:
			break

	return result

def newton(f, x0, n=1000, interval=[float("-inf"), float("inf")]):
	if f(interval[0]) * f(interval[1]) > 0:
		return None

	result = x0

	for i in range(n):
		if derivative(f, result) == 0:
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

		if result != next_value:
			result = next_value
		else:
			break

	if result > interval[1] or result < interval[0]:
		return None
	else:
		return result

def pointsFixes(g, x0, n=1000, epsilon=10e-6):
	# if abs(derivative(g, x0)) > 1:
	# 	return "No convergence: |F'(x0)| > 1"

	for i in range(n):
		x1 = g(x0)
		x2 = g(x1)

		if x0 == x1 == x2: 
			# invariant, so return x0
			return x0

		if x2 - 2*x1 + x0 == 0:
			x0 = x2
			continue

		xe = x0 - ((x1 - x0)**2)/(x2 - 2*x1 + x0)

		if xe == 0 or abs(xe - x0)/abs(xe) < epsilon:
			return xe
		else:
			x0 = xe

	return None