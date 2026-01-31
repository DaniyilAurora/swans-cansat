import pygame as pg
import utils

class Pane:
    def __init__(self, x, y, width, height, title=""):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.title = title
        self.font = pg.font.SysFont("Arial", 22, bold=True)

    def draw(self, screen, data):
        """Draws a pane with gradient bars."""
        # Draw background with a subtle border
        bg_rect = pg.Rect(self.x, self.y, self.width, self.height)
        pg.draw.rect(screen, utils.GRAPH_BACKGROUND_COLOR, bg_rect)
        pg.draw.rect(screen, utils.BORDERS_COLOR, bg_rect, 1)

        # Draw Title
        title_surf = self.font.render(self.title, True, utils.LABEL_COLOR)
        screen.blit(title_surf, (self.x + 15, self.y + 10))

        if not data:
            return

        # Prepare data slice for drawing (last max_bars)
        max_bars = 50
        data_to_show = data[-max_bars:] if len(data) > max_bars else data
        
        # Calculate bar width based on available space
        bar_width = self.width / max_bars
        
        # Draw Bars
        for i in range(len(data_to_show)):
            self.draw_bar(screen, i, data_to_show, bar_width)

    def draw_bar(self, screen, i, data_to_show, bar_width):
        """Draws a bar with a vertical gradient."""
        bar_height = int((self.height * 0.7 / utils.MAX_DATA) * data_to_show[i]) # Use 70% of height for bars

        x = self.x + (i * bar_width)
        y = self.y + self.height - bar_height - 10 # 10px padding from bottom
        
        # Draw gradient manually by drawing lines
        for step in range(max(1, bar_height)):
            # Calculate color interpolation
            ratio = step / bar_height if bar_height > 0 else 0
            color = pg.Color(
                int(utils.BAR_START_COLOR.r + (utils.BAR_END_COLOR.r - utils.BAR_START_COLOR.r) * ratio),
                int(utils.BAR_START_COLOR.g + (utils.BAR_END_COLOR.g - utils.BAR_START_COLOR.g) * ratio),
                int(utils.BAR_START_COLOR.b + (utils.BAR_END_COLOR.b - utils.BAR_START_COLOR.b) * ratio)
            )
            pg.draw.line(screen, color, (x, self.y + self.height - 10 - step), (x + bar_width - 1, self.y + self.height - 10 - step))