import pyglet
import game
import func

func.start()

# Event handlers
@game.game_window.event
def on_draw():
	game.game_window.clear()
	func.draw_board()
	game.info_batch.draw()

@game.game_window.event
def on_mouse_press(x, y, button, modifiers):
	# Restart button
	if game.restart_x_start < x < game.restart_x_end:
		 if game.restart_y_start < y < game.restart_y_end:
		 	func.start()

	# Pause button
	if game.pause_x_start < x < game.pause_x_end:
		 if game.pause_y_start < y < game.pause_y_end:
		 	game.pause = True if game.pause == False else False

pyglet.clock.schedule_interval(func.update, 1)
pyglet.app.run()