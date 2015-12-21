from board import *
import sys

notDone = []

def main():
	print '\n~~~~~~~~~~~~~~~~~ NOODLES GAME SOLVER ~~~~~~~~~~~~~~~~~'

	# Prompt user for board dimensions
	dimensions = raw_input('Enter board dimensions ([rows] [cols]): ')
	dimensions = dimensions.split()

	board = RectangleBoard(int(dimensions[0]), int(dimensions[1]))
	
	board.print_piece_codes()
	
	# Prompt user for pieces
	board_code = raw_input("Enter pieces for the board: ")

	board.set_up(board_code)
	board.run_solver()
	board.print_final_board()

main()