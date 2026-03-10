"""
Sensor monitoring state machine.

Simulates threshold detection and alert escalation.
"""

from dataclasses import dataclass
from enum import Enum, auto
import random
import time


class MonitorState(Enum):
    """Finite state machine states for the sensor monitor."""

    NORMAL = auto()
    WARNING = auto()
    ALERT = auto()


@dataclass
class SensorMonitor:
    """Monitors a simulated sensor and escalates alerts based on thresholds.

    The monitor reads a random sensor value and updates its state according
    to configurable warning and alert thresholds.
    """

    state = MonitorState.NORMAL
    warning_threshold = 60
    alert_threshold = 80

    def read_sensor(self):
        """Read the simulated sensor value.

        Returns:
            int: Random integer between 30 and 100 representing the
                current sensor reading.
        """
        return random.randint(30, 100)

    def update(self):
        """Update the monitor state based on the latest sensor reading.

        The thresholds are applied as follows:
        - value >= alert_threshold -> ALERT
        - value >= warning_threshold -> WARNING
        - otherwise -> NORMAL
        """
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
        """Execute the action associated with the current monitor state."""

        match self.state:
            case MonitorState.NORMAL:
                print("System stable")
            case MonitorState.WARNING:
                print("Warning: threshold exceeded")
            case MonitorState.ALERT:
                print("ALERT: critical value detected")

    def run(self):
        """Run the monitoring loop indefinitely.

        On each iteration, reads the sensor, updates the state, performs
        the corresponding action, and prints a separator line.
        """
        while True:
            self.update()
            self.act()
            print("-----")

            time.sleep(1)


if __name__ == "__main__":
    monitor = SensorMonitor()
    monitor.run()
