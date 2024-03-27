import arcade
import constants as c
from character_sprite import CharacterSprite


class PlayerSprite(CharacterSprite):
    """
    Player character sprite
    """
    def __init__(self):
        super().__init__(c.PLAYER_SPRITE_FOLDER, c.PLAYER_SPRITE_FILE)
