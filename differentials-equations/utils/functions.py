
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