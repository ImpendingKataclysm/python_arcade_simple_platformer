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


def get_walk_textures(path):
    walk_textures = []
    for i in range(c.WALK_TEXTURES_TOTAL):
        texture = load_texture_pair(f'{path}_walk{i}.png')
        walk_textures.append(texture)

    return walk_textures
