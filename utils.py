import arcade
import constants as c
from enemies import RobotEnemy, ZombieEnemy


def load_texture_pair(filename):
    """
    Loads a given sprite texture resource and its mirror image as a set of
    arcade Textures.
    :param filename: The file path indicating the resource to load
    :return: A List containing the loaded texture and its mirror image.
    """
    return [
        arcade.load_texture(filename),
        arcade.load_texture(filename, flipped_horizontally=True)
    ]


def load_walk_textures(path):
    """
    Loads a given sprite's walk textures.
    :param path: The file path for the sprite
    :return: A list of walk textures for the given sprite
    """
    walk_textures = []
    for i in range(c.WALK_TEXTURES_TOTAL):
        texture = load_texture_pair(f'{path}_walk{i}.png')
        walk_textures.append(texture)

    return walk_textures


def load_climb_textures(path):
    """
    Loads the climb textures for a given sprite resource.
    :param path: The path for the sprite resource
    :return: A list of climbing textures for the sprite
    """
    return [
            arcade.load_texture(f'{path}_climb{c.INITIAL_TEXTURE_INDEX}.png'),
            arcade.load_texture(f'{path}_climb{c.INITIAL_TEXTURE_INDEX + 1}.png')
        ]


def display_gui_text(label, data, start_x):
    """
    Display some information in the GUI at the given start_x coordinate.
    :param label: The label describing the data
    :param data: Data relevant to the player
    :param start_x: The starting x-coordinate for the label
    """
    gui_text = f'{label}: {data}'
    arcade.draw_text(
        gui_text,
        start_x,
        c.GUI_TEXT_START_Y,
        arcade.csscolor.MINT_CREAM,
        c.GUI_FONT_SIZE
    )


def create_enemy(sprite):
    """
    Create a RobotEnemy or a ZombieEnemy with a given Sprite depending on the
    sprite's 'type' property.
    :param sprite: The Sprite with which to create the enemy.
    :return: Either a RobotEnemy or a ZombieEnemy depending on the sprite's
    type.
    """
    enemy_type = sprite.properties['type']
    enemy = None

    if enemy_type == c.ROBOT_SPRITE_NAME:
        enemy = RobotEnemy()
    elif enemy_type == c.ZOMBIE_SPRITE_NAME:
        enemy = ZombieEnemy()
    else:
        message = f'Unknown enemy type {enemy_type}.'
        raise TypeError(message)

    return enemy


def move_inside_boundaries(layer_item, sprite):
    """
    Move a Sprite horizontally between boundaries defined by the tile map layer.
    :param layer_item: The tile map item containing the values that will be
    applied to a Sprite.
    :param sprite: The Sprite object.
    """
    if 'boundary_left' in layer_item.properties:
        sprite.boundary_left = layer_item.properties['boundary_left']

    if 'boundary_right' in layer_item.properties:
        sprite.boundary_right = layer_item.properties['boundary_right']

    if 'change_x' in layer_item.properties:
        sprite.change_x = layer_item.properties['change_x']
