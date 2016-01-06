from board import *
import sys

notDone = []

def main():
	print '\n~~~~~~~~~~~~~~~~~ NOODLES GAME SOLVER ~~~~~~~~~~~~~~~~~'

	# Prompr user for board type
	board_type = raw_input('Enter board type (r for rectangle, h for hexagon): ')

	# Prompt user for board dimensions
	dimensions = raw_input('Enter board dimensions ([rows] [cols]): ')
	dimensions = dimensions.split()

	if board_type.lower() == 'r':
		board = RectangleBoard(int(dimensions[0]), int(dimensions[1]))
	elif board_type.lower() == 'h':
		board = HexagonBoard(int(dimensions[0]), int(dimensions[1]))
	else:
		print 'Not a valid board type! Exiting...'
		exit()
	
	board.print_piece_codes()
	
	# Prompt user for pieces
	board_code = raw_input("Enter pieces for the board: ")

	board.set_up(board_code)
	board.run_solver()
	board.print_final_board()

main()