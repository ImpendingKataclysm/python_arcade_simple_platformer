import constants as c
from character_sprite import CharacterSprite


class Enemy(CharacterSprite):
    """
    Enemy Sprite
    """
    def __init__(self, name_folder, name_file):
        super(Enemy, self).__init__(name_folder, name_file)

    def update_animation(self, delta_time: float = 1 / 60):
        """
        Animate the enemy sprite's animations based on the direction it is
        facing.
        :param delta_time:
        :return: None
        """
        self.set_face_direction()

        if self.set_idle_animation():
            return

        self.set_walk_animation()


class RobotEnemy(Enemy):
    """
    Robot enemy sprite
    """
    def __init__(self):
        super(RobotEnemy, self).__init__(
            c.ROBOT_SPRITE_NAME,
            c.ROBOT_SPRITE_NAME
        )

        self.walk_update_interval = 1


class ZombieEnemy(Enemy):
    """
    Zombie enemy sprite
    """
    def __init__(self):
        super(ZombieEnemy, self).__init__(
            c.ZOMBIE_SPRITE_NAME,
            c.ZOMBIE_SPRITE_NAME
        )

        self.walk_update_interval = 3
