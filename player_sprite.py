import arcade
import constants as c
from character_sprite import CharacterSprite


class PlayerSprite(CharacterSprite):
    """
    Player character sprite
    """
    def __init__(self):
        super().__init__(c.PLAYER_SPRITE_FOLDER, c.PLAYER_SPRITE_FILE)

        self.is_on_ladder = False
        self.jumping = False
        self.climbing = False

    def update_animation(self, delta_time: float = 1 / 60):
        """
        Update the player sprite's animation depending on the direction it's
        facing and whether it is walking, jumping, climbing or falling.
        :param delta_time:
        :return: None
        """
        # Determine the sprite's direction
        self.set_face_direction()

        # Jumping animation
        if self.change_y > 0 and not self.is_on_ladder:
            self.texture = self.jump_texture_pair[self.direction]
            return
        # Falling animation
        elif self.change_y < 0 and not self.is_on_ladder:
            self.texture = self.fall_texture_pair[self.direction]
            return

        # Idle animation
        if self.set_idle_animation():
            return

        # Walking animation
        self.cur_texture_index += 1
        if self.cur_texture_index >= c.WALK_TEXTURES_TOTAL:
            self.cur_texture_index = 0

        self.texture = self.walk_textures[self.cur_texture_index][self.direction]
