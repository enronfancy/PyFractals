import numpy as np
import matplotlib.pyplot as plt

x = y = np.arange(-70, 70, 1)
x, y = np.meshgrid(x,y)

def drawCircle(centerX, centerY, radius):
	plt.contour(x, y, (x-centerX) ** 2 + (y-centerY) ** 2, [radius*radius])


def drawCircles(curDepth, center, radius, maxDepth = 10):
	if curDepth > maxDepth:
		return

	curDepth += 1
	print 'CurDepth:', curDepth

	left = center - radius
	right = center + radius 

	drawCircle(center, 0, radius)

	drawCircles(curDepth, left, radius / 2.0, maxDepth)
	drawCircles(curDepth, right, radius / 2.0, maxDepth)


drawCircles(0, 0, 50, 6)
plt.axis('scaled')
plt.show()