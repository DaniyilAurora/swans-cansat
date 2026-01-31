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

# New Color Palette (Premium Dark Theme)
BACKGROUND_COLOR = pg.Color(11, 15, 25)
GRAPH_BACKGROUND_COLOR = pg.Color(20, 27, 45)
BORDERS_COLOR = pg.Color(45, 65, 100)
ACCENT_COLOR = pg.Color(0, 180, 255)
TEXT_COLOR = pg.Color(230, 240, 255)
LABEL_COLOR = pg.Color(150, 180, 220)
GRID_COLOR = pg.Color(35, 45, 65)

# Primary bar and trajectory colors
BAR_START_COLOR = pg.Color(0, 120, 255)
BAR_END_COLOR = pg.Color(0, 220, 255)
TRAJECTORY_COLOR = pg.Color(255, 255, 255)
TRAJECTORY_LINE_WIDTH = 3
TRAJECTORY_GLOW_COLOR = pg.Color(0, 150, 255, 60) # Transparent blue for glow

DATA_RECEIVED_WINDOW_HEIGHT = 200

PORT = 'COM3'
BAUDRATE = 115200

def rotate(lst, n):
    """Rotate list by n positions to the right."""
    n = n % len(lst)  # Handle n larger than list length
    return lst[-n:] + lst[:-n]
    
def validate(packet: str):
    """Validates packet using offset detection (101 always sent first, therefore if there is change in data order the data will be shifted)."""
    parsed = packet.split('.')
    shift = len(parsed) - parsed.index("101")

    parsed = rotate(parsed, shift)

    return parsed[1:]

def parse_data(data):
    """Divides the data by 10 in order to get original value with decimal place."""
    return round(data / 10, 1)

def save_data(data, filename):
    """Saves collected data into output/ directory."""
    if not os.path.exists("output"):
        os.mkdir("output")
    
    with open("output/" + filename, "a") as file:
        for d in data:
            file.write(str(d) + "\n")