import os
import pygame as pg

WIDTH = 1920
HEIGHT = 1080
FRAMERATE = 60

PANE_WIDTH = 700
PANE_HEIGHT = 216

TRAJECTORY_WIDTH = WIDTH - PANE_WIDTH
TRAJECTORY_HEIGHT = HEIGHT

START_X = TRAJECTORY_WIDTH / 2

MAX_X = 100
MAX_Y = 1090
MAX_DATA = 999

TEXT_COLOR = pg.Color("white")
BAR_COLOR = pg.Color(25, 146, 242)
TRAJECTORY_BACKGROUND_COLOR = pg.Color(63, 75, 101)
TRAJECTORY_COLOR = pg.Color("white")
GRAPH_BACKGROUND_COLOR = pg.Color(28, 37, 54)
BORDERS_COLOR = pg.Color(40, 57, 85)

TRAJECTORY_LINE_WIDTH = 4

DATA_RECEIVED_WINDOW_HEIGHT = 200

PORT = 'COM3'
BAUDRATE = 115200

def save_data(data, filename):
    if not os.path.exists("output"):
        os.mkdir("output")
    
    with open("output/" + filename, "a") as file:
        for d in data:
            file.write(str(d) + "\n")