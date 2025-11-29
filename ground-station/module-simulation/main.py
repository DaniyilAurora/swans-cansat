import serial
import threading
import pygame as pg
import utils
import time
from pane import Pane
from trajectory import Trajectory

class Simulation:
    def __init__(self):
        pg.init()
        pg.font.init()
        self.screen = pg.display.set_mode((utils.WIDTH, utils.HEIGHT))
        self.clock = pg.time.Clock()
        self.running = True

        pg.display.set_caption("Module Simulation of Swans CanSat")

        self.temp_pane = Pane(0, 0, utils.PANE_WIDTH, utils.PANE_HEIGHT)
        self.hum_pane = Pane(0, 216, utils.PANE_WIDTH, utils.PANE_HEIGHT)
        self.ozone_pane = Pane(0, 216*2, utils.PANE_WIDTH, utils.PANE_HEIGHT)
        self.carbon_pane = Pane(0, 216*3, utils.PANE_WIDTH, utils.PANE_HEIGHT)
        self.oxygen_pane = Pane(0, 216*4, utils.PANE_WIDTH, utils.PANE_HEIGHT)

        self.trajectory = Trajectory(utils.PANE_WIDTH, 0, utils.TRAJECTORY_WIDTH, utils.TRAJECTORY_HEIGHT)

        self.temp_data = []
        self.hum_data = []
        self.ozone_data = []
        self.carbon_data = []
        self.oxygen_data = []

        self.trajectory_data = [(0, 0), (2, 50), (5, 250), (7, 560), (10, 890), (15, 990), (18, 1000), (19, 1000), (20, 990), (25, 750)]

        self.borders = []
        self.borders.append(pg.Rect(0, utils.PANE_HEIGHT-2, utils.PANE_WIDTH, 4))
        self.borders.append(pg.Rect(0, 2 * utils.PANE_HEIGHT-2, utils.PANE_WIDTH, 4))
        self.borders.append(pg.Rect(0, 3 * utils.PANE_HEIGHT-2, utils.PANE_WIDTH, 4))
        self.borders.append(pg.Rect(0, 4 * utils.PANE_HEIGHT-2, utils.PANE_WIDTH, 4))
        self.borders.append(pg.Rect(utils.PANE_WIDTH - 2, 0, 4, utils.HEIGHT))

        self.font = pg.font.SysFont("Arial", 30)
        self.captions = []
        self.captions.append(self.font.render("Temperature", False, pg.Color("white")))
        self.captions.append(self.font.render("Humidity", False, pg.Color("white")))
        self.captions.append(self.font.render("Ozone", False, pg.Color("white")))
        self.captions.append(self.font.render("Carbon", False, pg.Color("white")))
        self.captions.append(self.font.render("Oxygen", False, pg.Color("white")))

        self.data_lock = threading.Lock()
        self.serial_thread = threading.Thread(target=self.read_serial, daemon=True)
        self.serial_thread.start()

    def read_serial(self):
        ser = serial.Serial(utils.PORT, utils.BAUDRATE, timeout=1)
        
        while self.running:
            try:
                if ser.in_waiting > 0:
                    data = ser.readline().decode('utf-8').strip()
                    
                    with self.data_lock:
                        parsed_data = data.split(".")
                        self.temp_data.append(int(parsed_data[0]))
                        self.hum_data.append(int(parsed_data[1]))
                    
                    print(f"Received: {data}")
                    
            except Exception as e:
                print(f"Error: {e}")
            
            time.sleep(0.1)

        ser.close()

    def run(self):
        while self.running:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.running = False
                    utils.save_data(self.temp_data, "temp_data.txt")
                    utils.save_data(self.hum_data, "hum_data.txt")
                    utils.save_data(self.ozone_data, "ozone_data.txt")
                    utils.save_data(self.carbon_data, "carbon_data.txt")
                    utils.save_data(self.oxygen_data, "oxygen_data.txt")
            
            self.screen.fill("darkslategray")

            self.temp_pane.draw(self.screen, self.temp_data)
            self.hum_pane.draw(self.screen, self.hum_data)
            self.ozone_pane.draw(self.screen, self.ozone_data)
            self.carbon_pane.draw(self.screen, self.carbon_data)
            self.oxygen_pane.draw(self.screen, self.oxygen_data)

            self.trajectory.draw(self.screen, self.trajectory_data)

            for border in self.borders:
                pg.draw.rect(self.screen, pg.Color("black"), border)
            
            for i in range(len(self.captions)):
                self.screen.blit(self.captions[i], (utils.PANE_WIDTH + 10, ((i+1) * utils.PANE_HEIGHT) - utils.PANE_HEIGHT / 2 - 30))

            pg.display.flip()
            self.clock.tick(utils.FRAMERATE)

if __name__ == "__main__":
    sim = Simulation()
    sim.run()

    pg.quit()