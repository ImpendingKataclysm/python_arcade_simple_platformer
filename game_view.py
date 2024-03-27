import arcade
import os
import constants as c
from player_sprite import PlayerSprite


class GameView(arcade.View):
    """
    Runs the platformer game application.
    """
    def __init__(self):
        super(GameView, self).__init__()

        # Set the file path to start with this program
        file_path = os.path.dirname(os.path.abspath(__file__))
        os.chdir(file_path)

        # Set up the map and scene
        self.tile_map = None
        self.scene = None

        # Player sprite
        self.player_sprite = None
        self.player_start_x = None
        self.player_start_y = None

    def create_map(self):
        """
        Creates the game map and initializes the Scene.
        """
        map_name = c.BASIC_MAP
        layer_options = {
            c.COINS_LAYER: {
                'use_spatial_hash': True,
            },
            c.PLATFORMS_LAYER: {
                'use_spatial_hash': True
            },
        }

        self.tile_map = arcade.load_tilemap(
            map_name,
            c.TILE_SCALING,
            layer_options
        )

        self.scene = arcade.Scene.from_tilemap(self.tile_map)

        if self.tile_map.background_color:
            arcade.set_background_color(self.tile_map.background_color)

    def create_player_sprite(self):
        """
        Creates a sprite for the player, calculates its starting coordinates
        and adds it to the scene.
        """
        self.player_sprite = PlayerSprite()
        self.player_start_x = c.PLAYER_START_X * c.TILE_SCALING * self.tile_map.tile_width
        self.player_start_y = c.PLAYER_START_Y * c.TILE_SCALING * self.tile_map.tile_height
        self.player_sprite.center_x = self.player_start_x
        self.player_sprite.center_y = self.player_start_y
        self.scene.add_sprite(c.PLAYER_LAYER, self.player_sprite)

    def setup(self):
        """
        Sets the initial game state.
        """
        # Create the game map and initialize the scene
        self.create_map()

        # Create the player sprite and set its initial coordinates
        self.create_player_sprite()

    def on_show_view(self):
        """
        Display the game in its initial state.
        """
        self.setup()

    def on_draw(self):
        """
        Render the game map and sprites.
        """
        self.clear()
        self.scene.draw()
    