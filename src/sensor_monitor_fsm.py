"""
Sensor monitoring state machine
Simulates threshold detection and alert escalation.
"""
from dataclasses import dataclass
from enum import Enum, auto
import random
import time


class MonitorState(Enum):
    NORMAL = auto()
    WARNING = auto()
    ALERT = auto()

@dataclass
class SensorMonitor:
    state = MonitorState.NORMAL
    warning_threshold = 60
    alert_threshold = 80

    def read_sensor(self):
        return random.randint(30, 100)

    def update(self):
        value = self.read_sensor()

        print(f"Sensor value: {value}")

        match value:
            case value if value >= self.alert_threshold:
                self.state = MonitorState.ALERT
            case value if value >= self.warning_threshold:
                self.state = MonitorState.WARNING
            case _:
                self.state = MonitorState.NORMAL

    def act(self):
        match self.state:
            case MonitorState.NORMAL:
                print("System stable")
            case MonitorState.WARNING:
                print("Warning: threshold exceeded")
            case MonitorState.ALERT:
                print("ALERT: critical value detected")

    def run(self):
        while True:
            self.update()
            self.act()
            print("-----")

            time.sleep(1)


if __name__ == "__main__":
    monitor = SensorMonitor()
    monitor.run()