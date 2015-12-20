from abc import abstractmethod
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
		self.possibleOrientations = [p for p in self.possibleOrientations 
										if not p.contains_direction(direction)]

	def eliminate_not_direction(self, direction):
		self.possibleOrientations = [p for p in self.possibleOrientations
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
		self.possibleOrientations = []
		self.done = False
		self.orientation = None
		self.possibleOrientations.append(Orientation(down, right))
		self.possibleOrientations.append(Orientation(down, left))
		self.possibleOrientations.append(Orientation(up, right))
		self.possibleOrientations.append(Orientation(up, left))


class LongPiece(Piece):
	def __init__(self):
		self.possibleOrientations = []
		self.done = False
		self.orientation = None
		self.possibleOrientations.append(Orientation(up, down))
		self.possibleOrientations.append(Orientation(left, right))


class EndPiece(Piece):
	def __init__(self):
		self.possibleOrientations = []
		self.done = False
		self.orientation = None
		self.possibleOrientations.append(Orientation(up))
		self.possibleOrientations.append(Orientation(down))
		self.possibleOrientations.append(Orientation(left))
		self.possibleOrientations.append(Orientation(right))


class ProngPiece(Piece):
	def __init__(self):
		self.possibleOrientations = []
		self.done = False
		self.orientation = None
		self.possibleOrientations.append(Orientation(left, up, right))
		self.possibleOrientations.append(Orientation(up, right, down))
		self.possibleOrientations.append(Orientation(right, down, left))
		self.possibleOrientations.append(Orientation(down, left, up))

