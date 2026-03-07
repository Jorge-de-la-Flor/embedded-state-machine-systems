"""
Traffic Light Finite State Machine
Example of deterministic state-based control for embedded environments
"""

from dataclasses import dataclass
from enum import Enum, auto
import time


class TrafficState(Enum):
    RED = auto()
    GREEN = auto()
    YELLOW = auto()

@dataclass
class TrafficLightController:
    state = TrafficState.RED
    state_durations = {
        TrafficState.RED: 5,
        TrafficState.GREEN: 5,
        TrafficState.YELLOW: 2,
    }

    def next_state(self):
        match self.state:
            case TrafficState.RED:
                self.state = TrafficState.GREEN
            case TrafficState.GREEN:
                self.state = TrafficState.YELLOW
            case TrafficState.YELLOW:
                self.state = TrafficState.RED

    def run(self):
        while True:
            print(f"Current state: {self.state.name}")
            duration = self.state_durations[self.state]
            time.sleep(duration)

            self.next_state()


if __name__ == "__main__":
    controller = TrafficLightController()
    controller.run()
