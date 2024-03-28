import arcade
import constants as c


class Timer:
    """
    Displays how much time the player has spent in minutes and seconds.
    """
    def __init__(self):
        self.total_time = 0.0
        self.initial_text = "00:00"
        self.anchor_x = "center"
        self.timer_text = arcade.Text(
            text=self.initial_text,
            start_x=c.TIMER_TEXT_START_X,
            start_y=c.GUI_TEXT_START_Y,
            color=arcade.color.MINT_CREAM,
            font_size=c.GUI_FONT_SIZE,
            anchor_x=self.anchor_x
        )

    def update(self, delta_time: float):
        """
        Increment the timer's total_time by the delta_time and display the
        updated time in minutes and seconds.
        :param delta_time: The amount by which to increment the total_time
        """
        self.total_time += delta_time
        minutes = int(self.total_time) // 60
        seconds = int(self.total_time) % 60
        self.timer_text.text = f'{minutes:02d}:{seconds:02d}'
