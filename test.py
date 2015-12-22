from board import *

# Board Types:
# 0 for Rectangle Board


def run_test(board_type, rows, cols, board_code, orientations):
	if board_type == 0:
		board = RectangleBoard(rows, cols)

	board.set_up(board_code)
	board.run_solver()

	for i in xrange(rows):
		for j in xrange(cols):
			if not board.board[i][j].orientation.equals(orientations[i*cols+j]):
				print 'Test FAILED!'
				print '\tPiece ' + str(i) + str(j) + ' orientation should be ' +\
					   orientations[i*cols+j].get_name() + ' but was ' +\
					   board.board[i][j].orientation.get_name()
				return

	print 'Test PASSED!'

def main():
	# TEST 1: 2x3 rectangle
	orientations = [[down, right], [left, down, right], [left], [up], [up, right], 
					[left]]
	orientations = [Orientation(x) for x in orientations]
	run_test(0, 2, 3, 'CPEECE', orientations)

	# TEST 2: 3x3 rectangle
	orientations = [[right], [left, down, right], [left, down], [right, down],
					[left, up, down], [up, down], [up], [up], [up]]
	orientations = [Orientation(x) for x in orientations]
	run_test(0, 3, 3, 'EPCCPLEEE', orientations)

	# TEST 3: 4x4 rectangle
	orientations = [[down, right], [left], [down, right], [left], [up, down],
					[down, right], [up, left], [down], [up, down], 
					[up, right, down], [left], [up, down], [right, up],
					[left, up, right], [right, left], [left, up]]
	orientations = [Orientation(x) for x in orientations]
	run_test(0, 4, 4, 'CECELCCELPELCPLC', orientations)

	# TEST 4: 5x4 rectangle
	orientations = [[right], [left, down], [down], [down], [down], [up, right],
					[left, up, right], [down, left, up], [up, down], [right],
					[left, down, right], [up, left, down], [up, right],
					[left, right], [up, left, down], [up, down], [right], 
					[right, left], [left, up], [up]]
	orientations = [Orientation(x) for x in orientations]
	run_test(0, 5, 4, 'ECEEECPPLEPPCLPLELCE', orientations)

	# TEST 5: 5x5 rectangle
	orientations = [[right], [right, left], [right, left, down], [left], [down],
					[right], [left, down], [up, right, down], [left, right],
					[left, up], [down], [up, right, down], [left, up, right],
					[left, right], [left], [up, down], [up, right, down], [left],
					[right, down], [left], [up, right], [left, up, right],
					[left, right], [left, up, right], [left]]
	orientations = [Orientation(x) for x in orientations]
	run_test(0, 5, 5, 'ELPEEECPLCEPPLELPECECPLPE', orientations)

	# TEST 6: 3x3 hexagon

	# TEST 7: 4x3 hexagon

	# TEST 8: 4x5 hexagon

	# TEST 9: 4x5 hexagon

	# TEST 10: 6x5 rectangle
	orientations = [[right, down], [left, down, right], [left, down], [right],
					[left, down], [up, down], [up], [up, right], [left, right],
					[left, up, down], [up, down], [right], [left, down, right],
					[left, right], [left, up, down], [up, right, down],
					[left, down], [up], [right], [left, up, down], [up, down],
					[up, down], [right, down], [left, right, down], [up, down, left],
					[up], [up], [up], [up], [up]]
	orientations = [Orientation(x) for x in orientations]
	run_test(0, 6, 5, 'CPCECLECLPLEPLPPCEEPLLCPPEEEEE', orientations)

	# TEST 11 - 5x5 hexagon

	# TEST 12 - 6x6 rectangle
	orientations = [[down, right], [left], [down], [right], [left, right],
					[left, down], [up, right, down], [left], [up, right, down],
					[left], [down], [up, down], [up, right, down], [right, left],
					[left, up, right], [left, down, right], [left, up], [up, down],
					[up, down], [down], [right], [left, up, down], [right],
					[left, up, down], [up, down], [up, right, down], [left, down],
					[up, right], [left, down, right], [up, left, down], [up],
					[up], [up, right], [left, right], [left, up], [up]]
	orientations = [Orientation(x) for x in orientations]
	run_test(0, 6, 6, 'CEEELCPEPEELPLPPCLLEEPEPLPCCPPEECLCE', orientations)


	# TEST 13 - 6x5 hexagon

	# TEST 14 - 7x7 rectangle - FIX THIS!!!
	orientations = [[right], [left, right], [left, right], [left, right],
					[left, right], [left, down], [down], [right], [left, right],
					[left, right], [left, right, down], [left, right, down],
					[left, right, up], [up, down, left], [down, right],
					[left, right, down], [left, right], [left, up, down],
					[up, down, right], [left, down], [up], [up], [up, down],
					[right], [left, up, down], [up, down], [up, down, right],
					[left, down], [down, right], [left, up, down], [right],
					[left, up, down], [up, down], [up], [up, down], [up, down],
					[up, down, right], [left], [up], [up, down, right], [left],
					[up, down], [up], [up], [right], [left, right], [left, up],
					[right], [left, up]]
	orientations = [Orientation(x) for x in orientations]
	# run_test(0, 7, 7, 'ELLLLCEELLPPPPCPLPPCEELEPLPCCPEPLELLPEEPELEEELCEC', orientations)

	# TEST 15 - 5x7 hexagon


main()