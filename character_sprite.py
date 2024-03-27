import arcade
import constants as c


class CharacterSprite(arcade.Sprite):
    """
    Animated character sprite
    """
    def __init__(self, name_folder, name_file):
        super(CharacterSprite, self).__init__()

        self.scale = c.CHARACTER_SCALING
        self.main_path = f'{c.CHARACTER_PATH}{name_folder}/{name_file}'

        self.texture = arcade.load_texture(f'{self.main_path}_idle.png')
