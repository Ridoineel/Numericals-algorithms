
def euler(f, y0, T=5, h=0.01):
	""" 1st order differential equation 

		y_{n + 1} = y_{n} + h*f(t_{n}, y_{n})

	"""

	y = y0
	X = [0]
	Y = [y0]

	t = 0
	while t < T:
		y = y + h*f(t, y)

		X.append(t)
		Y.append(y)

		t += h

	return X, Y

def modifEuler(f, y0, T=100, h=0.2):
	""" 2nd order differential equation 
		with modified euler method

		y_{n+1} = y_{n} + h*f(t_{n + 1/2}, y_{n} + (1/2)f(t_{n}, y_{n}))

	"""
	
	y = y0
	X = [0]
	Y = [y0]

	t = 0
	while t < T:
		K = f(t + h/2, y + f(t, y)/2)

		y = y + K

		X.append(t)
		Y.append(y)

		t += h

	return X, Y

def heun(f, y0, T=100, h=0.2):
	""" 2nd order differential equation,
		with heun method.

		y_{n+1} = y_{n} + (h/2)(f(t_{n}, y_{n}) + f(t_{n + 1}, y_{n} + h*f(t_{n}, y_{n}))

	"""
	
	y = y0
	X = [0]
	Y = [y0]

	t = 0
	while t < T:
		K1 = f(t, y)
		K2 = f(t + h, y + h*K1)

		y = y + h*(K1 + K2)/2

		X.append(t)
		Y.append(y)

		t += h

	return X, Y

def rungeKunta(f, y0, T=100, h=0.01, method="heun"):
	""" 2nd order differential equation 
		using heun and modified euler methods

	"""
	
	methods = {
		"heun": heun,
		"modifEuler": modifEuler
	}

	if method in methods:
		func = methods[method]

		return func(f, y0, T, h)

	return -1

def simpson(f, y0, T=100, h=0.01):
	""" 4th order differential equation:
		Simpson integration
		
		y_{n+1} = y_{n} + (h/6)(K1 + 2K2 + 2K3 + K4)

		K1 = f(t_{n}, y_{n})
		K2 = f(t_{n} + h/2, y_{n} + h*K1/2)
		K3 = f(t_{n} + h/2, y_{n} + h*K2/2)
		K4 = f(t_{n + 1}, y_{n} + h*K3)

	"""

	y = y0
	X = [0]
	Y = [y0]

	t = 0
	while t < T:
		K1 = f(t, y)
		K2 = f(t + h/2, y + h*K1/2)
		K3 = f(t + h/2, y + h*K2/2)
		K4 = f(t + h, y + h*K3)

		y = y + h*(K1 + 2*K2 + 2*K3 + K4)/6

		X.append(t)
		Y.append(y)

		t += h

	return X, Y

def main():
	pass


if __name__ == '__main__':
	main()