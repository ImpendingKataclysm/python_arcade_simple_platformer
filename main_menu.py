import arcade
import constants as c


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
