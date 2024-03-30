import arcade
import constants as c


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
    return [
            arcade.load_texture(f'{path}_climb{c.INITIAL_TEXTURE_INDEX}.png'),
            arcade.load_texture(f'{path}_climb{c.INITIAL_TEXTURE_INDEX + 1}.png')
        ]
