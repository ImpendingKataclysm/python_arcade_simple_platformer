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

    def set_jump_animation(self):
        """
        Use the player sprite's jump textures if it is currently moving upwards
        and not on a ladder.
        :return: True if the player is jumping, False if not
        """
        if self.change_y > 0 and not self.is_on_ladder:
            self.texture = self.jump_texture_pair[self.direction]
            return True
        return False

    def set_fall_animation(self):
        """
        Use the player sprite's fall textures if it is currently moving downwards
        and not on a ladder.
        :return: True if the player is falling, False if not
        """
        if self.change_y < 0 and not self.is_on_ladder:
            self.texture = self.fall_texture_pair[self.direction]
            return True
        return False

    def set_climb_animation(self):
        """
        Use the player sprite's climb textures if it is currently on a ladder
        and moving vertically.
        :return: True if the player is currently climbing, False if not
        """
        if self.is_on_ladder:
            self.climbing = True

        if not self.is_on_ladder and self.climbing:
            self.climbing = False

        if self.climbing and abs(self.change_y) > 1:
            self.cur_texture_index += 1

            if self.cur_texture_index >= c.WALK_TEXTURES_TOTAL:
                self.cur_texture_index = 0

        if self.climbing:
            self.texture = self.climb_texture_pair[
                self.cur_texture_index // int(c.WALK_TEXTURES_TOTAL / 2)
            ]

        return self.climbing

    def set_walk_animation(self):
        """
        Update the player sprite's walk texture to cycle through the list of
        walk textures.
        """
        self.cur_texture_index += 1
        if self.cur_texture_index >= c.WALK_TEXTURES_TOTAL:
            self.cur_texture_index = 0

        self.texture = self.walk_textures[self.cur_texture_index][self.direction]

    def update_animation(self, delta_time: float = 1 / 60):
        """
        Update the player sprite's animation depending on the direction it's
        facing and whether it is walking, jumping, climbing or falling.
        :param delta_time:
        :return: None
        """
        self.set_face_direction()

        if (
            self.set_jump_animation()
            or self.set_fall_animation()
            or self.set_climb_animation()
            or self.set_idle_animation()
        ):
            return

        self.set_walk_animation()
