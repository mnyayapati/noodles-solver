from orientation import *

left = Left()
right = Right()
up = Up()
down = Down()
up_right = UpRight()
up_left = UpLeft()
down_right = DownRight()
down_left = DownLeft()

class Piece(object):
	def eliminate_up(self):
		self.eliminate_direction(up)

	def eliminate_down(self):
		self.eliminate_direction(down)

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

	def contains_up(self):
		if self.orientation == None:
			return False
		return self.orientation.contains_direction(up)

	def contains_down(self):
		if self.orientation == None:
			return False
		return self.orientation.contains_direction(down)


class HexagonPiece(Piece):
	def eliminate_up_right(self):
		self.eliminate_direction(up_right)

	def eliminate_down_right(self):
		self.eliminate_direction(down_right)

	def eliminate_up_left(self):
		self.eliminate_direction(up_left)

	def eliminate_down_left(self):
		self.eliminate_direction(down_left)

	def eliminate_not_up_right(self):
		self.eliminate_not_direction(up_right)

	def eliminate_not_down_right(self):
		self.eliminate_not_direction(down_right)

	def eliminate_not_up_left(self):
		self.eliminate_not_direction(up_left)

	def eliminate_not_down_left(self):
		self.eliminate_not_direction(down_left)

	def contains_up_right(self):
		if self.orientation == None:
			return False
		return self.orientation.contains_direction(up_right)

	def contains_down_right(self):
		if self.orientation == None:
			return False
		return self.orientation.contains_direction(down_right)

	def contains_up_left(self):
		if self.orientation == None:
			return False
		return self.orientation.contains_direction(up_left)

	def contains_down_left(self):
		return self.orientation.contains_direction(down_left)


class RectanglePiece(Piece):
	def eliminate_left(self):
		self.eliminate_direction(left)

	def eliminate_right(self):
		self.eliminate_direction(right)

	def eliminate_not_left(self):
		self.eliminate_not_direction(left)

	def eliminate_not_right(self):
		self.eliminate_not_direction(right)

	def contains_left(self):
		if self.orientation == None:
			return False
		return self.orientation.contains_direction(left)

	def contains_right(self):
		if self.orientation == None:
			return False
		return self.orientation.contains_direction(right)

class CornerPiece(RectanglePiece):
	def __init__(self):
		self.possible_orientations = []
		self.done = False
		self.orientation = None
		self.possible_orientations.append(Orientation([down, right]))
		self.possible_orientations.append(Orientation([down, left]))
		self.possible_orientations.append(Orientation([up, right]))
		self.possible_orientations.append(Orientation([up, left]))


class LongPiece(RectanglePiece):
	def __init__(self):
		self.possible_orientations = []
		self.done = False
		self.orientation = None
		self.possible_orientations.append(Orientation([up, down]))
		self.possible_orientations.append(Orientation([left, right]))


class EndPiece(RectanglePiece):
	def __init__(self):
		self.possible_orientations = []
		self.done = False
		self.orientation = None
		self.possible_orientations.append(Orientation([up]))
		self.possible_orientations.append(Orientation([down]))
		self.possible_orientations.append(Orientation([left]))
		self.possible_orientations.append(Orientation([right]))


class ProngPiece(RectanglePiece):
	def __init__(self):
		self.possible_orientations = []
		self.done = False
		self.orientation = None
		self.possible_orientations.append(Orientation([left, up, right]))
		self.possible_orientations.append(Orientation([up, right, down]))
		self.possible_orientations.append(Orientation([right, down, left]))
		self.possible_orientations.append(Orientation([down, left, up]))


class HexEndPiece(HexagonPiece):
	def __init__(self):
		self.possible_orientations = []
		self.done = False
		self.orientation = None
		self.possible_orientations.append(Orientation([up]))
		self.possible_orientations.append(Orientation([up_right]))
		self.possible_orientations.append(Orientation([down_right]))
		self.possible_orientations.append(Orientation([down]))
		self.possible_orientations.append(Orientation([down_left]))
		self.possible_orientations.append(Orientation([up_left]))

class VPiece(HexagonPiece):
	def __init__(self):
		self.possible_orientations = []
		self.done = False
		self.orientation = None
		self.possible_orientations.append(Orientation([up_left, up_right]))
		self.possible_orientations.append(Orientation([up, down_right]))
		self.possible_orientations.append(Orientation([up_right, down]))
		self.possible_orientations.append(Orientation([down_right, down_left]))
		self.possible_orientations.append(Orientation([up_left, down]))
		self.possible_orientations.append(Orientation([down_left, up]))

class HexLongPiece(HexagonPiece):
	def __init__(self):
		self.possible_orientations = []
		self.done = False
		self.orientation = None
		self.possible_orientations.append(Orientation([up, down]));
		self.possible_orientations.append(Orientation([up_right, down_left]))
		self.possible_orientations.append(Orientation([up_left, down_right]))

class CPiece(HexagonPiece):
	def __init__(self):
		self.possible_orientations = []
		self.done = False
		self.orientation = None
		self.possible_orientations.append(Orientation([up, up_right]))
		self.possible_orientations.append(Orientation([up_right, down_right]))
		self.possible_orientations.append(Orientation([down_right, down]))
		self.possible_orientations.append(Orientation([down, down_left]))
		self.possible_orientations.append(Orientation([down_left, up_left]))
		self.possible_orientations.append(Orientation([up_left, up]))

class TrianglePiece(HexagonPiece):
	def __init__(self):
		self.possible_orientations = []
		self.done = False
		self.orientation = None
		self.possible_orientations.append(Orientation([up, down_right, down_left]))
		self.possible_orientations.append(Orientation([up_right, down, up_left]))

class YPiece(HexagonPiece):
	def __init__(self):
		self.possible_orientations = []
		self.done = False
		self.orientation = None
		self.possible_orientations.append(Orientation([up, down, up_left]))
		self.possible_orientations.append(Orientation([up, up_right, down_left]))
		self.possible_orientations.append(Orientation([up_left, down_right, up_right]))
		self.possible_orientations.append(Orientation([up, down, down_right]))
		self.possible_orientations.append(Orientation([down_left, down_right, down]))
		self.possible_orientations.append(Orientation([up_left, down_right, down_left]))

class WPiece(HexagonPiece):
	def __init__(self):
		self.possible_orientations = []
		self.done = False
		self.orientation = None
		self.possible_orientations.append(Orientation([up_left, up, up_right]))
		self.possible_orientations.append(Orientation([up, up_right, down_right]))
		self.possible_orientations.append(Orientation([up_right, down_right, down]))
		self.possible_orientations.append(Orientation([down_right, down, down_left]))
		self.possible_orientations.append(Orientation([down, down_left, up_left]))
		self.possible_orientations.append(Orientation([down_left, down_left, up]))

class XPiece(HexagonPiece):
	def __init__(self):
		self.possible_orientations = []
		self.done = False
		self.orientation = None
		self.possible_orientations.append(Orientation([up, down, up_left, down_right]))
		self.possible_orientations.append(Orientation([up, down, up_right, down_left]))
		self.possible_orientations.append(Orientation([up_left, down_right, up_right, down_left]))

class KPiece(HexagonPiece):
	def __init__(self):
		self.possible_orientations = []
		self.done = False
		self.orientation = None
		self.possible_orientations.append(Orientation([up, up_right, down_right, down]))
		self.possible_orientations.append(Orientation([up_right, down_right, down, down_left]))
		self.possible_orientations.append(Orientation([down_right, down, down_left, up_left]))
		self.possible_orientations.append(Orientation([down, down_left, up_left, up]))
		self.possible_orientations.append(Orientation([down_left, up_left, up, up_right]))
		self.possible_orientations.append(Orientation([up_left, up, up_right, down_right]))

class BrushPiece(HexagonPiece):
	def __init__(self):
		self.possible_orientations = []
		self.done = False
		self.orientation = None
		self.possible_orientations.append(Orientation([up, down_right, down, down_left]))
		self.possible_orientations.append(Orientation([up_right, down, down_left, up_left]))
		self.possible_orientations.append(Orientation([down_right, down_left, up_left, up]))
		self.possible_orientations.append(Orientation([down, up_left, up, up_right]))
		self.possible_orientations.append(Orientation([down_left, up, up_right, down_right]))
		self.possible_orientations.append(Orientation([up_left, up_right, down_right, down]))


		


