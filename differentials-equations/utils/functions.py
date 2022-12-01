import matplotlib.pyplot as plt

def graphic(X, Y, name="", show=True, **kwargs):
	ax = plt.axes()

	ax.set_xlabel("--> t")
	ax.set_ylabel("--> y")
	# ax.set_title("")

	plt.scatter(X, Y, label=name, **kwargs)
	plt.legend()

	if show:
		plt.show()