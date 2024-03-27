import arcade
import os
import constants as c


class GameView(arcade.View):
    """
    Runs the platformer game application.
    """
    def __init__(self):
        super(GameView, self).__init__()

        # Set the file path to start with this program.
        file_path = os.path.dirname(os.path.abspath(__file__))
        os.chdir(file_path)

        # Set up the map and scene
        self.tile_map = None
        self.scene = None

    def setup(self):
        """
        Loads the scene and map and sets the game state.
        """
        # Create the game map
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

        # Initialize the Scene from the map
        self.scene = arcade.Scene.from_tilemap(self.tile_map)

        # Set the background color based on the map
        if self.tile_map.background_color:
            arcade.set_background_color(self.tile_map.background_color)

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
    