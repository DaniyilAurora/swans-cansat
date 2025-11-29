import os

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

PORT = 'COM3'
BAUDRATE = 115200

def save_data(data, filename):
    if not os.path.exists("output"):
        os.mkdir("output")
    
    with open("output/" + filename, "a") as file:
        for d in data:
            file.write(str(d) + "\n")