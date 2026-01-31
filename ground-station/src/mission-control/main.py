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

        # Initialize Panes with Titles
        self.temp_pane = Pane(0, 0, utils.PANE_WIDTH, utils.PANE_HEIGHT, "Temperature (°C)")
        self.hum_pane = Pane(0, utils.PANE_HEIGHT, utils.PANE_WIDTH, utils.PANE_HEIGHT, "Humidity (%)")
        self.ozone_pane = Pane(0, utils.PANE_HEIGHT*2, utils.PANE_WIDTH, utils.PANE_HEIGHT, "Ozone (ppm)")
        self.carbon_pane = Pane(0, utils.PANE_HEIGHT*3, utils.PANE_WIDTH, utils.PANE_HEIGHT, "Carbon Monoxide (ppm)")
        self.oxygen_pane = Pane(0, utils.PANE_HEIGHT*4, utils.PANE_WIDTH, utils.PANE_HEIGHT, "Oxygen (%)")

        self.trajectory = Trajectory(utils.PANE_WIDTH, 60, utils.TRAJECTORY_WIDTH, utils.TRAJECTORY_HEIGHT - utils.DATA_RECEIVED_WINDOW_HEIGHT - 60)

        self.data_received_rect = pg.Rect(utils.PANE_WIDTH, utils.HEIGHT - utils.DATA_RECEIVED_WINDOW_HEIGHT, utils.TRAJECTORY_WIDTH, utils.DATA_RECEIVED_WINDOW_HEIGHT)

        self.temp_data = [0]
        self.hum_data = [0]
        self.ozone_data = [0]
        self.carbon_data = [0]
        self.oxygen_data = [0]

        # Sample trajectory data
        self.trajectory_data = [(0, 0), (2, 50), (5, 250), (6, 350), (6, 450), (7, 560), (10, 890), (12, 950), (15, 990), (18, 1000), (19, 1000), (20, 990), (21, 960), (23, 920), (24, 840), (25, 750)]

        self.main_font = pg.font.SysFont("Arial", 28)
        self.title_font = pg.font.SysFont("Arial", 36, bold=True)
        self.data_font = pg.font.SysFont("Consolas", 24)

        self.data_lock = threading.Lock()
        self.serial_thread = threading.Thread(target=self.read_serial, daemon=True)
        self.serial_thread.start()

    def read_serial(self):
        """Reads serial data from port."""
        try:
            ser = serial.Serial(utils.PORT, utils.BAUDRATE, timeout=1)
            while self.running:
                if ser.in_waiting > 0:
                    data = ser.readline().decode('utf-8').strip()
                    with self.data_lock:
                        parsed_data = utils.validate(data)
                        if len(parsed_data) >= 2:
                            self.temp_data.append(int(parsed_data[0]))
                            self.hum_data.append(int(parsed_data[1]))
                            # Handle other sensors if data is available
        except Exception as e:
            print(f"Serial Error: {e}")

    def draw_title_bar(self):
        # Draw top title bar
        title_bar_rect = pg.Rect(utils.PANE_WIDTH, 0, utils.TRAJECTORY_WIDTH, 60)
        pg.draw.rect(self.screen, utils.GRAPH_BACKGROUND_COLOR, title_bar_rect)
        pg.draw.line(self.screen, utils.BORDERS_COLOR, (utils.PANE_WIDTH, 60), (utils.WIDTH, 60), 2)
        
        title_text = self.title_font.render("SWANS CANSAT - GROUND MISSION CONTROL", True, utils.ACCENT_COLOR)
        self.screen.blit(title_text, (utils.PANE_WIDTH + 20, 10))
        
        # System clock
        time_str = time.strftime("%H:%M:%S")
        time_text = self.main_font.render(time_str, True, utils.TEXT_COLOR)
        self.screen.blit(time_text, (utils.WIDTH - 150, 15))

    def draw_status_panel(self):
        # Background for the status/data panel
        pg.draw.rect(self.screen, utils.GRAPH_BACKGROUND_COLOR, self.data_received_rect)
        pg.draw.rect(self.screen, utils.BORDERS_COLOR, self.data_received_rect, 2)
        
        # Headers
        header_text = self.main_font.render("REAL-TIME TELEMETRY", True, utils.LABEL_COLOR)
        self.screen.blit(header_text, (self.data_received_rect.x + 20, self.data_received_rect.y + 15))

        # Data rows
        def get_last_val(data):
            return utils.parse_data(data[-1]) if data else 0.0

        sensors = [
            ("TEMP", get_last_val(self.temp_data), "°C"),
            ("HUMI", get_last_val(self.hum_data), "%"),
            ("OZONE", get_last_val(self.ozone_data), "ppm"),
            ("CARB", get_last_val(self.carbon_data), "ppm"),
            ("OXYG", get_last_val(self.oxygen_data), "%")
        ]

        x_offset = 20
        y_offset = 60
        for i, (name, val, unit) in enumerate(sensors):
            label = self.data_font.render(f"{name}:", True, utils.LABEL_COLOR)
            value = self.data_font.render(f"{val:>5} {unit}", True, utils.TEXT_COLOR)
            
            row_x = self.data_received_rect.x + x_offset + (i % 3) * 350
            row_y = self.data_received_rect.y + y_offset + (i // 3) * 50
            
            self.screen.blit(label, (row_x, row_y))
            self.screen.blit(value, (row_x + 80, row_y))

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
            
            self.screen.fill(utils.BACKGROUND_COLOR)

            # Draw Sensor Panes
            self.temp_pane.draw(self.screen, self.temp_data)
            self.hum_pane.draw(self.screen, self.hum_data)
            self.ozone_pane.draw(self.screen, self.ozone_data)
            self.carbon_pane.draw(self.screen, self.carbon_data)
            self.oxygen_pane.draw(self.screen, self.oxygen_data)

            # Draw Trajectory
            self.trajectory.draw(self.screen, self.trajectory_data)

            # Draw UI Elements
            self.draw_title_bar()
            self.draw_status_panel()

            pg.display.flip()
            self.clock.tick(utils.FRAMERATE)

if __name__ == "__main__":
    sim = Mission_Control()
    sim.run()
    pg.quit()