import constants as c
from character_sprite import CharacterSprite


class Enemy(CharacterSprite):
    """
    Enemy Sprite
    """
    def __init__(self, name_folder, name_file):
        super(Enemy, self).__init__(name_folder, name_file)

        self.should_update_walk = 0

    def update_animation(self, delta_time: float = 1 / 60):
        """
        Animate the enemy sprite's walking animation based on the direction it
        is facing.
        :param delta_time:
        :return: None
        """
        walk_limit = 3

        self.set_face_direction()

        if self.set_idle_animation():
            return

        if self.should_update_walk == walk_limit:
            self.cur_texture_index += 1

            if self.cur_texture_index >= c.WALK_TEXTURES_TOTAL:
                self.cur_texture_index = 0

            self.texture = self.walk_textures[self.cur_texture_index][self.direction]
            self.should_update_walk = 0

            return

        self.should_update_walk += 1


class RobotEnemy(Enemy):
    """
    Robot enemy sprite
    """
    def __init__(self):
        super(RobotEnemy, self).__init__(
            c.ROBOT_SPRITE_NAME,
            c.ROBOT_SPRITE_NAME
        )
        
        
class ZombieEnemy(Enemy):
    """
    Zombie enemy sprite
    """
    def __init__(self):
        super(ZombieEnemy, self).__init__(
            c.ZOMBIE_SPRITE_NAME,
            c.ZOMBIE_SPRITE_NAME
        )
