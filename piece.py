from orientation import *

left = Left()
right = Right()
up = Up()
down = Down()

class Piece(object):
	def eliminate_left(self):
		self.eliminate_direction(left)

	def eliminate_right(self):
		self.eliminate_direction(right)

	def eliminate_up(self):
		self.eliminate_direction(up)

	def eliminate_down(self):
		self.eliminate_direction(down)

	def eliminate_not_left(self):
		self.eliminate_not_direction(left)

	def eliminate_not_right(self):
		self.eliminate_not_direction(right)

	def eliminate_not_up(self):
		self.eliminate_not_direction(up)

	def eliminate_not_down(self):
		self.eliminate_not_direction(down)

	def eliminate_direction(self, direction):
		self.possible_orientations = [p for p in self.possible_orientations 
										if not p.contains_direction(direction)]

	def eliminate_not_direction(self, direction):
		self.possible_orientations = [p for p in self.possible_orientations
										if p.contains_direction(direction)]

	def contains_left(self):
		if self.orientation == None:
			return False
		return self.orientation.contains_direction(left)

	def contains_right(self):
		if self.orientation == None:
			return False
		return self.orientation.contains_direction(right)

	def contains_up(self):
		if self.orientation == None:
			return False
		return self.orientation.contains_direction(up)

	def contains_down(self):
		if self.orientation == None:
			return False
		return self.orientation.contains_direction(down)

class CornerPiece(Piece):
	def __init__(self):
		self.possible_orientations = []
		self.done = False
		self.orientation = None
		self.possible_orientations.append(Orientation([down, right]))
		self.possible_orientations.append(Orientation([down, left]))
		self.possible_orientations.append(Orientation([up, right]))
		self.possible_orientations.append(Orientation([up, left]))


class LongPiece(Piece):
	def __init__(self):
		self.possible_orientations = []
		self.done = False
		self.orientation = None
		self.possible_orientations.append(Orientation([up, down]))
		self.possible_orientations.append(Orientation([left, right]))


class EndPiece(Piece):
	def __init__(self):
		self.possible_orientations = []
		self.done = False
		self.orientation = None
		self.possible_orientations.append(Orientation([up]))
		self.possible_orientations.append(Orientation([down]))
		self.possible_orientations.append(Orientation([left]))
		self.possible_orientations.append(Orientation([right]))


class ProngPiece(Piece):
	def __init__(self):
		self.possible_orientations = []
		self.done = False
		self.orientation = None
		self.possible_orientations.append(Orientation([left, up, right]))
		self.possible_orientations.append(Orientation([up, right, down]))
		self.possible_orientations.append(Orientation([right, down, left]))
		self.possible_orientations.append(Orientation([down, left, up]))

