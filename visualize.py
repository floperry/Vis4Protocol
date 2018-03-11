from importfile import *

plt.figure()
with open('data.txt', 'r') as f:
	for line in f:
		data = line.split()
		
		name = data[0]
		x, y = float(data[1]), float(data[2])
		size = float(data[3])

		plt.scatter(x, y, s=size/10, facecolors='none', edgecolors='r')
		plt.scatter(x, y, s=10, color='r')
		plt.text(x, y, name)
plt.show()
