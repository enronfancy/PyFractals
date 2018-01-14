from math import *  
from turtle import *  
from graphics import *  


win = GraphWin("Snow", 400, 400)

# p = Point(100, 100)
# circ = Circle(p, 100)

p1 = Point(100, 100)
p2 = Point(300, 100)
p3 = Point(200, 273.20508075688772935274463415059)

# lines = [Line(p1, p2)]
lines = [Line(p1, p2), Line(p2, p3), Line(p3, p1)]

def recursiveLine(inputLines, curDepth = 0, maxDepth = 5):
	print "into recur:", curDepth
	if curDepth > maxDepth:
		return inputLines

	resLines = []

	for line in inputLines:
		p1 = line.getP1()
		p2 = line.getP2()
		middleX = p1.getX() / 2.0 + p2.getX() / 2.0
		middleY = p1.getY() / 2.0 + p2.getY() / 2.0

		middleX1 = p1.getX() / 3.0 + p2.getX() * 2.0 /3.0
		middleX2 = p1.getX() * 2.0  / 3.0 + p2.getX()/3.0

		middleY1 = p1.getY() / 3.0 + p2.getY() * 2.0 /3.0
		middleY2 = p1.getY() * 2.0  / 3.0 + p2.getY()/3.0

		direction = Point(p1.getX() - p2.getX(), p1.getY() - p2.getY())

		normal = Point(-direction.getY(), direction.getX())

		normal = normal.normalize()

		length = direction.length() / 3.0
		lastPoint = Point( normal.getX() *  0.866025 * length + middleX, normal.getY() * 0.866025 * length + middleY)

		resLines.append(Line(Point(middleX1, middleY1), p2))
		resLines.append(Line(lastPoint, Point(middleX1, middleY1)))
		resLines.append(Line(Point(middleX2, middleY2), lastPoint))
		resLines.append(Line(p1, Point(middleX2, middleY2)))

	return recursiveLine(resLines, curDepth + 1, maxDepth)

resLines = recursiveLine(lines, 0, 5)


for line in resLines:
	line.draw(win)

done()
