from piece import *
import sys

SIZE = 0
notDone = []
board = []

def main():
	print '\n~~~~~~~~~~~~~~~~~ NOODLES GAME SOLVER ~~~~~~~~~~~~~~~~~'
	global SIZE
	SIZE = input('Enter board size: ')
	print 'Board size : ' + str(SIZE) + 'x' + str(SIZE)
	print 'Piece Codes:'
	print '\tE = One-sided end piece'
	print '\tC = Two-sided corner piece'
	print '\tL = Two-sided long piece'
	print '\tP = Three-sided prong piece'

	set_up_board()

	# left edge pieces
	j = 0
	for i in xrange(SIZE):
		run_elimination(i, j)

	# right edge pieces
	j = SIZE-1
	for i in xrange(SIZE):
		run_elimination(i, j)

	# top edge pieces
	i = 0
	for j in xrange(SIZE):
		run_elimination(i, j)

	# bottom edge pieces
	i = SIZE-1
	for j in xrange(SIZE):
		run_elimination(i, j)

	while len(notDone) > 0:
		run_elimination(notDone[0][0], notDone[0][1])

	print 'Final Orientations:'
	for i in xrange(SIZE):
		s = ''
		for j in xrange(SIZE):
			s += ('\t' + board[i][j].orientation.get_name())
		print s

	print ''


def run_elimination(i, j):
	piece = board[i][j]
	if piece.done:
		return

	left = get_left_piece(i, j)
	right = get_right_piece(i ,j)
	up = get_above_piece(i, j)
	down = get_below_piece(i, j)

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

	notDone.remove((i,j))
	if len(piece.possibleOrientations) == 1:
		piece.orientation = piece.possibleOrientations[0]
		piece.done = True
		print '\tSet orientation for piece ' + str(i) + str(j) + ' to ' + piece.orientation.get_name()
	else:
		notDone.append((i,j)) # place piece at end of stack

def get_left_piece(i, j):
	if j == 0:
		return None
	return board[i][j-1]

def get_right_piece(i, j):
	if j == SIZE-1:
		return None
	return board[i][j+1]

def get_above_piece(i, j):
	if i == 0:
		return None
	return board[i-1][j]

def get_below_piece(i, j):
	if i == SIZE-1:
		return None
	return board[i+1][j]

def set_up_board():
	global board
	board = [[None for i in xrange(SIZE)] for j in xrange(SIZE)]

	code = raw_input("Enter pieces for the board: ")
	code = code.replace(' ', '').lower()

	if (len(code) < SIZE**2):
		print 'ERROR: Not enough pieces on the board! Exiting...\n'
		exit()	

	# set up board
	for i in xrange(SIZE):
		for j in xrange(SIZE):
			piece_code = code[SIZE*i+j]
			if piece_code == 'e':
				board[i][j] = EndPiece()
			elif piece_code == 'c':
				board[i][j] = CornerPiece()
			elif piece_code == 'l':
				board[i][j] = LongPiece()
			elif piece_code == 'p':
				board[i][j] = ProngPiece()
			else:
				print 'ERROR: Not a valid board encoding. Exiting...\n'
				exit()
			notDone.append((i,j))


main()