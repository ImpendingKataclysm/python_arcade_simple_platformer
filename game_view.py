import arcade
import os
import math
import utils
import constants as c
from player_sprite import PlayerSprite
from timer import Timer
from enemies import RobotEnemy, ZombieEnemy


class GameView(arcade.View):
    """
    Runs the platformer game application.
    """
    def __init__(self):
        super(GameView, self).__init__()

        # Set the file path to start with this program
        file_path = os.path.dirname(os.path.abspath(__file__))
        os.chdir(file_path)

        # Game map and Scene
        self.tile_map = None
        self.scene = None

        # Player sprite
        self.player_sprite = None
        self.player_start_x = None
        self.player_start_y = None

        # Key press tracking
        self.left_pressed = False
        self.right_pressed = False
        self.up_pressed = False
        self.down_pressed = False
        self.jump_needs_reset = False

        # Physics engine
        self.physics_engine = None

        # Sound effects
        self.jump_sound = arcade.load_sound(c.JUMP_SOUND_EFFECT)
        self.coin_sound = arcade.load_sound(c.COIN_SOUND_EFFECT)
        self.game_over_sound = arcade.load_sound(c.GAME_OVER_SOUND_EFFECT)

        # Cameras
        self.main_camera = None
        self.gui_camera = None

        # Player Score
        self.score = 0

        # Timer
        self.timer = None

    def create_map(self):
        """
        Creates the game map and initializes the Scene.
        """
        map_name = c.LADDER_MAP
        layer_options = {
            c.COINS_LAYER: {
                'use_spatial_hash': True,
            },
            c.PLATFORMS_LAYER: {
                'use_spatial_hash': True
            },
            c.MOVING_PLATFORMS_LAYER: {
                'use_spatial_hash': False
            },
            c.LADDERS_LAYER: {
                'use_spatial_hash': True
            },
        }

        self.tile_map = arcade.load_tilemap(
            map_name,
            c.TILE_SCALING,
            layer_options
        )

        self.scene = arcade.Scene.from_tilemap(self.tile_map)

        if self.tile_map.background_color:
            arcade.set_background_color(self.tile_map.background_color)

    def set_sprite_position(self, start_x, start_y):
        """
        Calculates a sprite's starting position on the map based on the
        TILE_SCALING constant and the tile map's tile_width and tile_height
        properties.
        :param start_x: The sprite's starting x-coordinate before adjusting to
        the tile map.
        :param start_y: The sprite's starting y-coordinate before adjusting to
        the tile map.
        :return: A list containing the sprite's adjusted x- and y-coordinates.
        """
        x = math.floor(start_x * c.TILE_SCALING * self.tile_map.tile_width)
        y = math.floor(start_y * c.TILE_SCALING * self.tile_map.tile_height)

        return [x, y]

    def create_player_sprite(self):
        """
        Creates a sprite for the player, calculates its starting coordinates
        and adds it to the scene.
        """
        self.player_sprite = PlayerSprite()
        self.player_sprite.position = self.set_sprite_position(
            c.PLAYER_START_X,
            c.PLAYER_START_Y
        )

        self.scene.add_sprite(c.PLAYER_LAYER, self.player_sprite)

    def create_enemy_sprites(self):
        """
        Add enemy sprites to the map.
        """
        enemies_layer = self.tile_map.object_lists[c.ENEMIES_LAYER]

        for sprite in enemies_layer:
            cartesian = self.tile_map.get_cartesian(
                sprite.shape[0],
                sprite.shape[1]
            )

            enemy = utils.create_enemy(sprite)
            enemy.position = self.set_sprite_position(
                cartesian[0],
                cartesian[1] + 1
            )

            utils.move_inside_boundaries(sprite, enemy)

            self.scene.add_sprite(c.ENEMIES_LAYER, enemy)

    def setup(self):
        """
        Sets the initial game state.
        """
        self.create_map()

        self.main_camera = arcade.Camera(self.window.width, self.window.height)
        self.gui_camera = arcade.Camera(self.window.width, self.window.height)
        self.timer = Timer()
        self.score = 0

        self.create_player_sprite()
        self.create_enemy_sprites()

        self.physics_engine = arcade.PhysicsEnginePlatformer(
            self.player_sprite,
            platforms=self.scene[c.MOVING_PLATFORMS_LAYER],
            gravity_constant=c.GRAVITY_ACCELERATION,
            ladders=self.scene[c.LADDERS_LAYER],
            walls=self.scene[c.PLATFORMS_LAYER]
        )

    def update_player_movement(self):
        """
        Moves the player sprite in response to keyboard inputs.
        """
        self.player_sprite.change_x = 0
        self.player_sprite.change_y = 0

        if self.up_pressed and not self.down_pressed:
            if self.physics_engine.is_on_ladder():
                self.player_sprite.change_y = c.PLAYER_RUN_SPEED_PX_PER_FRAME
            elif self.physics_engine.can_jump() and not self.jump_needs_reset:
                self.player_sprite.change_y = c.PLAYER_JUMP_SPEED_PX_PER_FRAME
                self.jump_needs_reset = True
                arcade.play_sound(self.jump_sound)
        elif self.down_pressed and not self.up_pressed:
            if self.physics_engine.is_on_ladder():
                self.player_sprite.change_y = -c.PLAYER_RUN_SPEED_PX_PER_FRAME

        if self.physics_engine.is_on_ladder():
            if (
                (not self.up_pressed and not self.down_pressed)
                or (self.up_pressed and self.down_pressed)
            ):
                self.player_sprite.change_y = 0

        if self.left_pressed and not self.right_pressed:
            self.player_sprite.change_x = -c.PLAYER_RUN_SPEED_PX_PER_FRAME
        elif self.right_pressed and not self.left_pressed:
            self.player_sprite.change_x = c.PLAYER_RUN_SPEED_PX_PER_FRAME
        else:
            self.player_sprite.change_x = 0

    def center_camera_to_player(self):
        """
        Focus the game camera on the player sprite to scroll the viewport as the
        player moves across the map.
        """
        screen_center_x = self.player_sprite.center_x - (
            self.main_camera.viewport_width / 2
        )

        screen_center_y = self.player_sprite.center_y - (
            self.main_camera.viewport_height / 2
        )

        if screen_center_x < 0:
            screen_center_x = 0

        if screen_center_y < 0:
            screen_center_y = 0

        player_center = screen_center_x, screen_center_y

        self.main_camera.move_to(player_center, c.CAMERA_SPEED)

    def game_over(self):
        """
        Play the game over sound effect and display the game over window.
        """
        arcade.play_sound(self.game_over_sound)
        game_over = self.GameOverView()
        self.window.show_view(game_over)

    def update_player_animations(self):
        """
        Set the values of the player sprite's can_jump and is_on_ladder flags
        based on the physics engine status.
        """
        if self.physics_engine.can_jump():
            self.player_sprite.can_jump = False
        else:
            self.player_sprite.can_jump = True

        if (
                self.physics_engine.is_on_ladder()
                and not self.physics_engine.can_jump()
        ):
            self.player_sprite.is_on_ladder = True
            self.update_player_movement()
        else:
            self.player_sprite.is_on_ladder = False

    def check_enemy_boundaries(self):
        for enemy in self.scene[c.ENEMIES_LAYER]:
            if (
                enemy.boundary_right and
                enemy.right > enemy.boundary_right and
                enemy.change_x > 0
            ) or (
                enemy.boundary_left and
                enemy.left < enemy.boundary_left and
                enemy.change_x < 0
            ):
                enemy.change_x *= -1

    def update_animations(self, delta_time):
        """
        Updates the animations for the player sprite and scene objects.
        :param delta_time: Time interval to use when updating animations
        """
        self.update_player_animations()
        self.scene.update_animation(
            delta_time,
            [c.COINS_LAYER, c.BACKGROUND_LAYER, c.PLAYER_LAYER, c.ENEMIES_LAYER]
        )

        self.scene.update([c.MOVING_PLATFORMS_LAYER, c.ENEMIES_LAYER])
        self.check_enemy_boundaries()

    def check_collisions(self):
        """
        Checks whether the player has collided with any coin sprites and collects
        them if so.
        """
        player_collision_list = arcade.check_for_collision_with_lists(
            self.player_sprite,
            [self.scene[c.COINS_LAYER]]
        )

        for sprite in player_collision_list:
            if self.scene[c.COINS_LAYER] in sprite.sprite_lists:
                points = int(sprite.properties[c.COINS_POINTS_PROP])
                self.score += points
                arcade.play_sound(self.coin_sound)
                sprite.remove_from_sprite_lists()

    def on_show_view(self):
        """
        Display the game in its initial state.
        """
        self.setup()

    def on_draw(self):
        """
        Render the game map and sprites.
        """
        self.clear()
        self.main_camera.use()
        self.scene.draw()
        self.gui_camera.use()
        utils.display_gui_text(c.SCORE_LABEL, self.score, c.SCORE_TEXT_START_X)
        coins_left = len(self.scene[c.COINS_LAYER])
        utils.display_gui_text(c.COINS_LABEL, coins_left, c.COIN_TEXT_START_X)
        self.timer.timer_text.draw()

    def on_key_press(self, symbol: int, modifiers: int):
        """
        Handle keyboard inputs for player sprite movement
        :param symbol: The key entered by the user
        :param modifiers:
        """
        if symbol == arcade.key.UP or symbol == arcade.key.W:
            self.up_pressed = True
        elif symbol == arcade.key.DOWN or symbol == arcade.key.S:
            self.down_pressed = True
        elif symbol == arcade.key.LEFT or symbol == arcade.key.A:
            self.left_pressed = True
        elif symbol == arcade.key.RIGHT or symbol == arcade.key.D:
            self.right_pressed = True

        self.update_player_movement()

    def on_key_release(self, _symbol: int, _modifiers: int):
        """
        Handle released keyboard inputs by halting movement and ensuring jumping
        is enabled.
        :param _symbol: The key released by the user
        :param _modifiers:
        """
        if _symbol == arcade.key.UP or _symbol == arcade.key.W:
            self.up_pressed = False
            self.jump_needs_reset = False
        elif _symbol == arcade.key.DOWN or _symbol == arcade.key.S:
            self.down_pressed = False
        elif _symbol == arcade.key.LEFT or _symbol == arcade.key.A:
            self.left_pressed = False
        elif _symbol == arcade.key.RIGHT or _symbol == arcade.key.D:
            self.right_pressed = False

        self.update_player_movement()

    def on_update(self, delta_time: float):
        """
        Update the physics engine and sprite animations.
        :param delta_time: The time interval at which to update the animations
        :return: None
        """
        self.physics_engine.update()
        self.update_animations(delta_time)
        self.check_collisions()

        if self.player_sprite.center_y < c.OFF_MAP_Y:
            self.game_over()
            return

        self.center_camera_to_player()
        self.timer.update(delta_time)

    class GameOverView(arcade.View):
        """
        Displays game over window
        """
        def on_show_view(self):
            """
            Display a black screen
            """
            arcade.set_background_color(arcade.color.BLACK)

        def on_draw(self):
            """
            Display the game over screen with text
            """
            self.clear()
            arcade.draw_text(
                c.GAME_OVER_TEXT,
                c.SCREEN_WIDTH / 2,
                c.SCREEN_HEIGHT / 2,
                arcade.color.WHITE,
                c.GUI_FONT_SIZE,
                anchor_x='center'
            )

        def on_mouse_press(self, x: int, y: int, button: int, modifiers: int):
            """
            Restart the game when the user clicks the game over screen
            :param x:
            :param y:
            :param button:
            :param modifiers:
            """
            game_view = GameView()
            self.window.show_view(game_view)
    