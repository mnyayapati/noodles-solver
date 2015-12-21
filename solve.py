from board import *
import sys

notDone = []

def main():
	print '\n~~~~~~~~~~~~~~~~~ NOODLES GAME SOLVER ~~~~~~~~~~~~~~~~~'
	dimensions = raw_input('Enter board dimensions ([rows] [cols]): ')
	dimensions = dimensions.split()

	board = RectangleBoard(int(dimensions[0]), int(dimensions[1]))
	board.set_up()
	board.run_solver()
	board.print_final_board()

main()