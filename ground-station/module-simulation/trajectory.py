import pygame as pg
import utils

class Trajectory:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def draw(self, screen, data):
        pg.draw.rect(screen, pg.Color("darkslategray"), pg.Rect(self.x, self.y, self.width, self.height))

        if len(data) > 1:
            for i in range(1, len(data)):
                start_x = self.x + utils.START_X + (data[i-1][0] / utils.MAX_X) * self.width
                end_x = self.x + utils.START_X + (data[i][0] / utils.MAX_X) * self.width
                
                start_y = self.y + self.height - (data[i-1][1] / utils.MAX_Y) * self.height
                end_y = self.y + self.height - (data[i][1] / utils.MAX_Y) * self.height

                start_pos = (start_x, start_y)
                end_pos = (end_x, end_y)
                pg.draw.line(screen, pg.Color("white"), start_pos, end_pos, 3)
            
            module_x = self.x + utils.START_X + (data[len(data) - 1][0] / utils.MAX_X) * self.width
            module_y = self.y + self.height - (data[len(data) - 1][1] / utils.MAX_Y) * self.height
            pg.draw.circle(screen, pg.Color("grey43"), (module_x, module_y), 6)