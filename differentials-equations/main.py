from diffequa import *
from utils.functions import graphic


def main():
	f = lambda t, y: t*y + 1.5
	y0 = 0
	
	X, Y = euler(f, y0)

	graphic(X, Y, name="Euler")

if __name__ == '__main__':
	main()