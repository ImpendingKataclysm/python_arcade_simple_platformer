import constants as c
from character_sprite import CharacterSprite


class Enemy(CharacterSprite):
    """
    Enemy Sprite
    """
    def __init__(self, name_folder, name_file):
        super(Enemy, self).__init__(name_folder, name_file)


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
