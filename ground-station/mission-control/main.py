import serial
import serial.tools.list_ports
import threading
import pygame as pg
import utils
import time
from pane import Pane
from trajectory import Trajectory

class Mission_Control:
    def __init__(self):
        pg.init()
        pg.font.init()
        self.screen = pg.display.set_mode((utils.WIDTH, utils.HEIGHT))
        self.clock = pg.time.Clock()
        self.running = True

        pg.display.set_caption("Mission Control of Swans CanSat")

        self.temp_pane = Pane(0, 0, utils.PANE_WIDTH, utils.PANE_HEIGHT)
        self.hum_pane = Pane(0, 216, utils.PANE_WIDTH, utils.PANE_HEIGHT)
        self.ozone_pane = Pane(0, 216*2, utils.PANE_WIDTH, utils.PANE_HEIGHT)
        self.carbon_pane = Pane(0, 216*3, utils.PANE_WIDTH, utils.PANE_HEIGHT)
        self.oxygen_pane = Pane(0, 216*4, utils.PANE_WIDTH, utils.PANE_HEIGHT)

        self.trajectory = Trajectory(utils.PANE_WIDTH, 0, utils.TRAJECTORY_WIDTH, utils.TRAJECTORY_HEIGHT - utils.DATA_RECEIVED_WINDOW_HEIGHT)

        self.data_received = pg.Rect(utils.PANE_WIDTH, utils.TRAJECTORY_HEIGHT - utils.DATA_RECEIVED_WINDOW_HEIGHT, utils.TRAJECTORY_WIDTH, utils.DATA_RECEIVED_WINDOW_HEIGHT)

        self.temp_data = [0]
        self.hum_data = [0]
        self.ozone_data = [0]
        self.carbon_data = [0]
        self.oxygen_data = [0]

        self.trajectory_data = [(0, 0), (2, 50), (5, 250), (6, 350), (6, 450), (7, 560), (10, 890), (12, 950), (15, 990), (18, 1000), (19, 1000), (20, 990), (21, 960), (23, 920), (24, 840), (25, 750)]

        self.borders = []
        self.borders.append(pg.Rect(0, utils.PANE_HEIGHT-2, utils.PANE_WIDTH, 4))
        self.borders.append(pg.Rect(0, 2 * utils.PANE_HEIGHT-2, utils.PANE_WIDTH, 4))
        self.borders.append(pg.Rect(0, 3 * utils.PANE_HEIGHT-2, utils.PANE_WIDTH, 4))
        self.borders.append(pg.Rect(0, 4 * utils.PANE_HEIGHT-2, utils.PANE_WIDTH, 4))
        self.borders.append(pg.Rect(utils.PANE_WIDTH - 2, 0, 4, utils.HEIGHT))

        self.font = pg.font.SysFont("Arial", 30)
        self.captions = []
        self.captions.append(self.font.render("Temperature ", False, utils.TEXT_COLOR))
        self.captions.append(self.font.render("Humidity", False, utils.TEXT_COLOR))
        self.captions.append(self.font.render("Ozone", False, utils.TEXT_COLOR))
        self.captions.append(self.font.render("Carbon", False, utils.TEXT_COLOR))
        self.captions.append(self.font.render("Oxygen", False, utils.TEXT_COLOR))

        self.data_lock = threading.Lock()
        self.serial_thread = threading.Thread(target=self.read_serial, daemon=True)
        self.serial_thread.start()

    def read_serial(self):
        print(serial.tools.list_ports.comports())
        ser = serial.Serial(utils.PORT, utils.BAUDRATE, timeout=1)
        
        while self.running:
            try:
                if ser.in_waiting > 0:
                    data = ser.readline().decode('utf-8').strip()
                    
                    with self.data_lock:
                        parsed_data = utils.validate(data)
                        self.temp_data.append(int(parsed_data[0]))
                        self.hum_data.append(int(parsed_data[1]))
                    
                    print(f"Received: {data}")
                    print(parsed_data)
                    
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

            self.data_received_text = self.font.render("Temp: " + str(utils.parse_data(self.temp_data[len(self.temp_data) - 1])) + "°C Hum: " +
                                            str(utils.parse_data(self.hum_data[len(self.hum_data) - 1])) + "% Ozone: " +
                                            str(utils.parse_data(self.ozone_data[len(self.ozone_data) - 1])) + " Carbon: " +
                                            str(utils.parse_data(self.carbon_data[len(self.carbon_data) - 1])) + " Oxygen: " +
                                            str(utils.parse_data(self.oxygen_data[len(self.oxygen_data) - 1])), False, utils.TEXT_COLOR)

            pg.draw.rect(self.screen, utils.GRAPH_BACKGROUND_COLOR, self.data_received)
            self.screen.blit(self.data_received_text, (utils.PANE_WIDTH + 20, utils.TRAJECTORY_HEIGHT - 50))

            for border in self.borders:
                pg.draw.rect(self.screen, utils.BORDERS_COLOR, border)
            
            for i in range(len(self.captions)):
                self.screen.blit(self.captions[i], (utils.PANE_WIDTH + 10, ((i+1) * utils.PANE_HEIGHT) - utils.PANE_HEIGHT / 2 - 30))

            pg.display.flip()
            self.clock.tick(utils.FRAMERATE)

if __name__ == "__main__":
    sim = Mission_Control()
    sim.run()

    pg.quit()