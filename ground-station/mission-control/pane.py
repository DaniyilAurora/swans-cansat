import pygame as pg
import utils

class Pane:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def draw(self, screen, data):
        """Draws a pane with bars."""
        pg.draw.rect(screen, utils.GRAPH_BACKGROUND_COLOR, pg.Rect(self.x, self.y, self.width, self.height))

        for i in range(len(data)):
            self.draw_bar(screen, i, data)

    def draw_bar(self, screen, i, data):
        """Draws a bar."""
        x_start = int(self.width * i / len(data))
        x_end = int(self.width * (i + 1) / len(data))
        bar_width = x_end - x_start
        
        bar_height = int((self.height / utils.MAX_DATA) * data[i])

        x = self.x + x_start
        y = self.y + self.height - bar_height
        
        bar = pg.Rect(x, y, bar_width, bar_height)
        pg.draw.rect(screen, utils.BAR_COLOR, bar)