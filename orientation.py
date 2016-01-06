class Orientation(object):
	def __init__(self, args):
		self.directions = set(args)

	def get_name(self):
		return ','.join([d.get_name() for d in self.directions])

	def contains_direction(self, direction):
		return direction in self.directions

	def equals(self, other):
		return self.directions == other.directions

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

class UpRight(Direction):
	def get_name(self):
		return 'UR'

class DownRight(Direction):
	def get_name(self):
		return 'DR'

class UpLeft(Direction):
	def get_name(self):
		return 'UL'

class DownLeft(Direction):
	def get_name(self):
		return 'DL'