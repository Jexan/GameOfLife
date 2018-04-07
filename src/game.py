import pyglet

# Window Dimensions
window_height = 300
info_width = 100
window_width = window_height + info_width
grid_count = 20
tile_size = window_height//grid_count
cells_multipliers = 3

#Relevant game variables
random_cells = grid_count*(tile_size//10)*cells_multipliers
generation = 0
pause = False
board = []
limit = 0

# Sprites handling
pyglet.resource.path = ['../imgs']
pyglet.resource.reindex()
restart_image = pyglet.resource.image("restart.png")
pause_image = pyglet.resource.image("pause.png")
off = pyglet.resource.image("blue-tile.png")
on = pyglet.resource.image("lime-tile.png")
info_batch = pyglet.graphics.Batch()

# Resize of on/off tiles
on.width = tile_size
off.width = tile_size
on.height = tile_size
off.height = tile_size

#Cenetering the anchor of images
pause_image.anchor_x = pause_image.width/2
pause_image.anchor_y = pause_image.height/2
restart_image.anchor_x = restart_image.width/2
restart_image.anchor_y = restart_image.height/2

#Sprites creation
pause_button = pyglet.sprite.Sprite(img=pause_image,x=window_width - info_width/2
	,y=20,batch=info_batch)
restart_button = pyglet.sprite.Sprite(img=restart_image,x=window_width - info_width/2
	,y=60,batch=info_batch)

# Used for button click
pause_x_start = pause_button.x - pause_button.width/2
pause_x_end = pause_button.x + pause_button.width/2
pause_y_start = pause_button.y - pause_button.height/2
pause_y_end = pause_button.y + pause_button.height/2
restart_x_start = restart_button.x - restart_button.width/2
restart_x_end = restart_button.x + restart_button.width/2
restart_y_start = restart_button.y - restart_button.height/2
restart_y_end = restart_button.y + restart_button.height/2

# Generation text
generation_label = pyglet.text.Label(str(generation),
                font_name='Roboto', font_size=11, x=window_width - info_width/2 - 5, 
                y=window_height - 50, batch= info_batch)
generation_text_label = pyglet.text.Label("Generation:",
                font_name='Roboto Slab', font_size=12, x=window_width - info_width + 5, 
                y=window_height - 20, batch= info_batch, bold = True)
# Main window
game_window = pyglet.window.Window(window_width,window_height)