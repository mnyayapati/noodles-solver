from piece import *

class Board(object):

	def set_up(self, code):
		code = code.replace(' ', '').lower()

		if (len(code) < self.num_rows * self.num_cols):
			print 'ERROR: Not enough pieces on the board! Exiting...\n'
			exit()	

		self.board = [[None for j in xrange(self.num_cols)] for i in xrange(self.num_rows)]

		# set up board
		for i in xrange(self.num_rows):
			for j in xrange(self.num_cols):
				piece_code = code[self.num_cols*i+j]
				self.board[i][j] = self.process_piece_code(piece_code)
				if self.board[i][j] == None:
					print 'ERROR: Not a valid board encoding. Exiting...\n'
					exit()
				self.not_done.append((i,j))

	def run_solver(self):
		# left edge pieces
		j = 0
		for i in xrange(self.num_rows):
			self.run_elimination(i, j)

		# right edge pieces
		j = self.num_cols-1
		for i in xrange(self.num_rows):
			self.run_elimination(i, j)

		# top edge pieces
		i = 0
		for j in xrange(self.num_cols):
			self.run_elimination(i, j)

		# bottom edge pieces
		i = self.num_rows-1
		for j in xrange(self.num_cols):
			self.run_elimination(i, j)

		# keep looping through pieces and eliminating orientations
		while len(self.not_done) > 0:
			self.run_elimination(self.not_done[0][0], self.not_done[0][1])

	def run_elimination(self, i, j):
		piece = self.board[i][j]
		if piece.done:
			return

		self.eliminate_orientations(i, j)

		self.not_done.remove((i,j))
		if len(piece.possible_orientations) == 1:
			piece.orientation = piece.possible_orientations[0]
			piece.done = True
			print '\tSet orientation for piece ' + str(i) + str(j) + ' to ' + piece.orientation.get_name()
		elif len(piece.possible_orientations) == 0:
			print 'ERROR: Seems like this board has no solution. Exiting...'
			exit()
		else:
			self.not_done.append((i,j)) # place piece at end of stack

	def print_final_board(self):
		print 'Final Orientations:'
		for i in xrange(self.num_rows):
			s = ''
			for j in xrange(self.num_cols):
				if self.board[i][j].orientation == None:
					s += '\t0'
				else:
					s += ('\t' + self.board[i][j].orientation.get_name())
			print s
		print ''


class RectangleBoard(Board):
	def __init__(self, rows, cols):
		self.num_rows = rows
		self.num_cols = cols
		self.not_done = []

	def print_piece_codes(self):
		print 'Piece Codes:'
		print '\tE = One-sided end piece'
		print '\tC = Two-sided corner piece'
		print '\tL = Two-sided long piece'
		print '\tP = Three-sided prong piece'
	
	def process_piece_code(self, piece_code):
		if piece_code == 'e':
			return EndPiece()
		elif piece_code == 'c':
			return CornerPiece()
		elif piece_code == 'l':
			return LongPiece()
		elif piece_code == 'p':
			return ProngPiece()


	def eliminate_orientations(self, i, j):
		piece = self.board[i][j]

		# get all neighbors for this piece
		left = self.get_left_piece(i, j)
		right = self.get_right_piece(i ,j)
		up = self.get_above_piece(i, j)
		down = self.get_below_piece(i, j)

		if left == None:
			piece.eliminate_left()
		elif left.done:
			if left.contains_right() : piece.eliminate_not_left()
			else : piece.eliminate_left()
		elif type(piece) == EndPiece and type(left) == EndPiece:
			piece.eliminate_left()

		if right == None:
			piece.eliminate_right()
		elif right.done:
			if right.contains_left() : piece.eliminate_not_right()
			else : piece.eliminate_right()
		elif type(piece) == EndPiece and type(right) == EndPiece:
			piece.eliminate_right()

		if up == None:
			piece.eliminate_up()
		elif up.done:
			if up.contains_down() : piece.eliminate_not_up()
			else : piece.eliminate_up()
		elif type(piece) == EndPiece and type(up) == EndPiece:
			piece.eliminate_up()

		if down == None:
			piece.eliminate_down()
		elif down.done:
			if down.contains_up() : piece.eliminate_not_down()
			else : piece.eliminate_down()
		elif type(piece) == EndPiece and type(down) == EndPiece:
			piece.eliminate_down()

	def get_left_piece(self, i, j):
		if j == 0:
			return None
		return self.board[i][j-1]

	def get_right_piece(self, i, j):
		if j == self.num_cols-1:
			return None
		return self.board[i][j+1]

	def get_above_piece(self, i, j):
		if i == 0:
			return None
		return self.board[i-1][j]

	def get_below_piece(self, i, j):
		if i == self.num_rows-1:
			return None
		return self.board[i+1][j]

class HexagonBoard(Board):
	pass

	# need to implement the following:
	# 	print_piece_codes
	# 	process_piece_code
	# 	elimiate_orientations


