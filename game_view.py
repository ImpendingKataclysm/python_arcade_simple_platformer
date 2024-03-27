import arcade


class GameView(arcade.View):
    """
    Runs the platformer game application.
    """
    def __init__(self):
        super(GameView, self).__init__()

    def on_show_view(self):
        """
        Display the game in its initial state.
        """
        arcade.set_background_color(arcade.color.AIR_SUPERIORITY_BLUE)

    def on_draw(self):
        """
        Render the game map and sprites.
        """
        self.clear()
    