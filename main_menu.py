import arcade
import constants as c
from game_view import GameView


class MainMenu(arcade.View):
    """
    Displays the Main Menu
    """
    def on_show_view(self):
        """
        Called when displaying the main menu view
        :return:
        """
        arcade.set_background_color(arcade.color.MIDNIGHT_BLUE)

    def on_draw(self):
        """
        Draws the main menu
        :return:
        """
        self.clear()
        arcade.draw_text(
            c.MAIN_MENU_TEXT,
            c.SCREEN_WIDTH / 2,
            c.SCREEN_HEIGHT / 2,
            arcade.color.WHITE,
            font_size=c.MENU_FONT_SIZE,
            anchor_x="center"
        )

    def on_mouse_press(self, x: int, y: int, button: int, modifiers: int):
        """
        Advance to the Game View when the user clicks the main menu.
        :param x:
        :param y:
        :param button:
        :param modifiers:
        :return:
        """
        game_view = GameView()
        self.window.show_view(game_view)
