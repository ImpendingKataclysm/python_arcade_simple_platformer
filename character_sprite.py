import arcade
import constants as c
import utils


class CharacterSprite(arcade.Sprite):
    """
    Animated character sprite
    """
    def __init__(self, name_folder, name_file):
        super(CharacterSprite, self).__init__()

        # Sprite scaling
        self.scale = c.CHARACTER_SCALING

        # Sprite texture resource path
        self.main_path = f'{c.CHARACTER_PATH}{name_folder}/{name_file}'

        # Binary flags for setting sprite direction
        self.direction = c.FACING_RIGHT
        self.cur_texture_index = c.INITIAL_TEXTURE_INDEX

        # Idle animation textures
        self.idle_texture_pair = utils.load_texture_pair(f'{self.main_path}_idle.png')

        # Jump animation textures
        self.jump_texture_pair = utils.load_texture_pair(f'{self.main_path}_jump.png')

        # Fall animation textures
        self.fall_texture_pair = utils.load_texture_pair(f'{self.main_path}_fall.png')

        # Walk animation textures
        self.walk_textures = utils.load_walk_textures(self.main_path)

        # Initial texture
        self.texture = self.idle_texture_pair[self.direction]

    def set_face_direction(self):
        """
        Ensure that the sprite is facing its direction of movement.
        """
        if self.change_x < 0 and self.direction != c.FACING_LEFT:
            self.direction = c.FACING_LEFT
        elif self.change_x > 0 and self.direction != c.FACING_RIGHT:
            self.direction = c.FACING_RIGHT

    def set_idle_animation(self):
        """
        If the sprite is not moving, display its idle texture facing the
        appropriate direction.
        :return: True if the sprite is idle, False if it is moving
        """
        if self.change_x == 0 and self.change_y == 0:
            self.texture = self.idle_texture_pair[self.direction]
            return True
        return False
