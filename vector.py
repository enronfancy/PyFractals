import math

class vector2:
	def __init__(self, x = 0.0, y = 0.0):
		self.x = float(x)
		self.y = float(y)

	def __str__(self):
		return "vector2( %s, %s )" % (self.x,  self.y)

	def length(self):
		return math.sqrt(self.x**2 + self.y**2)

	def normalize(self):
		return vector2(self.x / self.length(), self.y / self.length())

	def add(self, other):
		return vector2(self.x + other.x, self.y + other.y)

	def dec(self, other):
		return vector2(self.x - other.x, self.y - other.y)

	def mul(self, factor):
		return vector2(self.x * factor, self.y * factor)

	def div(self, div):
		return vector2(self.x / div, self.y / div)


if __name__ == "__main__":
	print "Test:"

	a = vector2(1, 2)
	b = vector2(3, 4)

	print a.length(), b.length()
	print a.add(b)
	print a.dec(b)
	print a.mul(2)
	print a.div(2)
