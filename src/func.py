import game
import copy
import random

# Updates the location of cells and the generation
def update(dt):
	if game.pause:
		return
	eliminate_adjacent()
	game.generation += 1
	game.generation_label.text = str(game.generation)

# Creates random cells at the star of the game
def randomize_board():
	for i in range(game.random_cells):
		game.board[random.randint(0,game.grid_count - 1)][random.randint(0,game.grid_count - 1)] = 1

# Blits the cells
def draw_board():
	for index_y,y in enumerate(game.board):
		for index_x,x in enumerate(y):
			if x:
				game.on.blit(index_x*game.tile_size, index_y*game.tile_size)
			else:
				game.off.blit(index_x*game.tile_size, index_y*game.tile_size)

# Checks if a cell lives or dies; N = North... 
def eliminate_adjacent():
	board_copy = copy.deepcopy(game.board)
	for index_y,y in enumerate(game.board):
		for index_x,x in enumerate(y):
			neighboors = 0

			if index_y != 0:
				neighboors += game.board[index_y - 1][index_x]         # N
				if index_x < game.limit:
					neighboors += game.board[index_y - 1][index_x + 1] # NE
					neighboors += game.board[index_y][index_x + 1]     # E
				if index_x != 0:
					neighboors += game.board[index_y - 1][index_x - 1] # NW
					neighboors += game.board[index_y][index_x - 1]     # W

			if index_y < game.limit:
				neighboors += game.board[index_y + 1][index_x]         # S
				if index_x < game.limit:
					neighboors += game.board[index_y + 1][index_x + 1] # SE
				if index_x != 0:
					neighboors += game.board[index_y + 1][index_x - 1] # SW
					
			if x == 0:			
				if neighboors == 3 or neighboors == 2:
					board_copy[index_y][index_x] = 1
			elif x == 1:
				if neighboors != 2:
					board_copy[index_y][index_x] = 0
			
	game.board = board_copy

# Used for the restart too; 1 means a live cell, 0, a dead one
def start():
	game.board = [[0 for y in range(game.grid_count)] for i in range(game.grid_count)]
	game.limit = len(game.board) - 1
	randomize_board()
	game.generation = 0
	game.generation_label.text = "0"