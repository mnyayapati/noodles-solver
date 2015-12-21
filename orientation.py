class Orientation(object):
	def __init__(self, *args):
		self.directions = []
		for arg in args:
			self.directions.append(arg)

	def get_name(self):
		return ''.join([d.get_name() for d in self.directions])

	def contains_direction(self, direction):
		return direction in self.directions

class Direction(object):
	pass

class Left(Direction):
	def get_name(self):
		return 'L'

class Right(Direction):
	def get_name(self):
		return 'R'

class Up(Direction):
	def get_name(self):
		return 'U'

class Down(Direction):
	def get_name(self):
		return 'D'