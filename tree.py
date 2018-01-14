from math import *  
from turtle import *  
from graphics import *  
from vector import *


win = GraphWin("Snow", 400, 400)


def rotate(d, angle):
	realAngle = angle / 180.0 * math.pi
	x = d.x * math.cos(realAngle) - d.y * math.sin(realAngle)
	y = d.x * math.sin(realAngle) + d.y * math.cos(realAngle)

	return vector2(x, y)


def toLine(input):
	return Line(Point(input[0].x, input[0].y),
				Point(input[1].x, input[1].y))



def fractalTree(inputLines, angle = 30, curDepth = 0, maxDepth = 5):
	if curDepth >= maxDepth:
		return inputLines	
	resLines = []
	for line in inputLines:
		length = (line[0].dec(line[1])).length() / 1.5
		direction = vector2(line[1].x - line[0].x, line[1].y - line[0].y)
		direction = direction.normalize()

		dirLeft = rotate(direction, -angle)
		dirRight = rotate(direction, angle)

		resLines.append( (line[1], line[1].add(dirLeft.mul(length))) )
		resLines.append( (line[1], line[1].add(dirRight.mul(length))) )

		l = toLine(line)
		l.draw(win)

	fractalTree(resLines, angle, curDepth+1, maxDepth)

inputLines = [(vector2(200, 0),vector2(200, 100))]
fractalTree(inputLines, 30, 0, 10)
print 'Done'
done()
