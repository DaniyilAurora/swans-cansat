import pygame as pg
import utils

class Trajectory:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.font = pg.font.SysFont("Arial", 18)

    def draw_grid(self, screen):
        """Draws a coordinate grid for the trajectory."""
        # Vertical lines (Time/X)
        for x_val in range(0, utils.MAX_X + 1, 10):
            screen_x = self.x + utils.START_X + (x_val / utils.MAX_X) * self.width
            if self.x <= screen_x <= self.x + self.width:
                pg.draw.line(screen, utils.GRID_COLOR, (screen_x, self.y), (screen_x, self.y + self.height), 1)
                label = self.font.render(f"{x_val}s", True, utils.LABEL_COLOR)
                screen.blit(label, (screen_x + 2, self.y + self.height - 20))

        # Horizontal lines (Altitude/Y)
        for y_val in range(0, utils.MAX_Y + 1, 100):
            screen_y = self.y + self.height - (y_val / utils.MAX_Y) * self.height
            if self.y <= screen_y <= self.y + self.height:
                pg.draw.line(screen, utils.GRID_COLOR, (self.x, screen_y), (self.x + self.width, screen_y), 1)
                label = self.font.render(f"{y_val}m", True, utils.LABEL_COLOR)
                screen.blit(label, (self.x + 5, screen_y - 18))

    def draw(self, screen, data):
        """Draws a trajectory with a grid and glow."""
        # Background
        bg_rect = pg.Rect(self.x, self.y, self.width, self.height)
        pg.draw.rect(screen, utils.GRAPH_BACKGROUND_COLOR, bg_rect)
        
        # Grid
        self.draw_grid(screen)

        if len(data) > 1:
            # Draw glow first
            for i in range(1, len(data)):
                # Simplified glow: draw thicker semi-transparent lines
                start_x = self.x + utils.START_X + (data[i-1][0] / utils.MAX_X) * self.width
                end_x = self.x + utils.START_X + (data[i][0] / utils.MAX_X) * self.width
                start_y = self.y + self.height - (data[i-1][1] / utils.MAX_Y) * self.height
                end_y = self.y + self.height - (data[i][1] / utils.MAX_Y) * self.height

                # Draw multiple lines for glow effect
                for w in range(utils.TRAJECTORY_LINE_WIDTH + 4, utils.TRAJECTORY_LINE_WIDTH, -2):
                    pg.draw.line(screen, (0, 100, 200, 50), (start_x, start_y), (end_x, end_y), w)

            # Draw main trajectory line
            points = []
            for d in data:
                px = self.x + utils.START_X + (d[0] / utils.MAX_X) * self.width
                py = self.y + self.height - (d[1] / utils.MAX_Y) * self.height
                points.append((px, py))
            
            if len(points) > 1:
                pg.draw.lines(screen, utils.ACCENT_COLOR, False, points, utils.TRAJECTORY_LINE_WIDTH)
            
            # Module indicator
            module_x = points[-1][0]
            module_y = points[-1][1]
            pg.draw.circle(screen, utils.ACCENT_COLOR, (int(module_x), int(module_y)), 8)
            pg.draw.circle(screen, (255, 255, 255), (int(module_x), int(module_y)), 4)
            
        # Border
        pg.draw.rect(screen, utils.BORDERS_COLOR, bg_rect, 2)