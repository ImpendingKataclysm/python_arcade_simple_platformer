# Screen display settings
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 650
SCREEN_TITLE = 'Simple Platformer'

# Menu Display
MAIN_MENU_TEXT = 'Main Menu - Click to play'
MENU_FONT_SIZE = 30
GAME_OVER_TEXT = 'Game Over - Click to restart'

# Game Maps
MAP_PATH = ':resources:tiled_maps/'
BASIC_MAP = f'{MAP_PATH}map.json'
LADDER_MAP = f'{MAP_PATH}map_with_ladders.json'

# Map Layers
COINS_LAYER = 'Coins'
PLATFORMS_LAYER = 'Platforms'
PLAYER_LAYER = 'Player'
BACKGROUND_LAYER = 'Background'
LADDERS_LAYER = 'Ladders'
MOVING_PLATFORMS_LAYER = 'Moving Platforms'
ENEMIES_LAYER = 'Enemies'
COINS_POINTS_PROP = 'Points'

# Sprite Scaling
TILE_SCALING = 0.5
CHARACTER_SCALING = TILE_SCALING * 2

# Character Sprites
CHARACTER_PATH = ':resources:images/animated_characters/'
PLAYER_SPRITE_FOLDER = 'female_adventurer'
PLAYER_SPRITE_FILE = 'femaleAdventurer'
PLAYER_START_X = 2
PLAYER_START_Y = 2
ROBOT_SPRITE_NAME = 'robot'
ZOMBIE_SPRITE_NAME = 'zombie'

# Sprite Movement
PLAYER_RUN_SPEED_PX_PER_FRAME = 5
PLAYER_JUMP_SPEED_PX_PER_FRAME = 30
GRAVITY_ACCELERATION = 1.5
OFF_MAP_Y = -100
FACING_RIGHT = 0
FACING_LEFT = 1
INITIAL_TEXTURE_INDEX = 0
WALK_TEXTURES_TOTAL = 8

# Sound Effects
SOUND_EFFECT_PATH = ':resources:sounds/'
JUMP_SOUND_EFFECT = f'{SOUND_EFFECT_PATH}jump1.wav'
COIN_SOUND_EFFECT = f'{SOUND_EFFECT_PATH}coin1.wav'
GAME_OVER_SOUND_EFFECT = f'{SOUND_EFFECT_PATH}gameover1.wav'

# Camera Speed
CAMERA_SPEED = 0.2

# GUI Display
GUI_FONT_SIZE = 18
GUI_TEXT_START_Y = 10
SCORE_TEXT_START_X = 10
COIN_TEXT_START_X = 175
TIMER_TEXT_START_X = 400
SCORE_LABEL = 'Score'
COINS_LABEL = 'Coins'
