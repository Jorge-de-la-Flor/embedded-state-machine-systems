"""
Traffic Light Finite State Machine.

Example of deterministic state-based control for embedded environments.
"""

from dataclasses import dataclass
from enum import Enum, auto
import time


class TrafficState(Enum):
    """Finite state machine states for a traffic light controller."""

    RED = auto()
    GREEN = auto()
    YELLOW = auto()


@dataclass
class TrafficLightController:
    """Controls a traffic light using a finite state machine.

    The controller cycles deterministically through RED, GREEN, and YELLOW
    states, holding each state for a configurable duration.
    """

    state = TrafficState.RED
    state_durations = {
        TrafficState.RED: 5,
        TrafficState.GREEN: 5,
        TrafficState.YELLOW: 2,
    }

    def next_state(self):
        """Advance the traffic light to the next state in the cycle.

        The transitions are:
        - RED -> GREEN
        - GREEN -> YELLOW
        - YELLOW -> RED
        """
        match self.state:
            case TrafficState.RED:
                self.state = TrafficState.GREEN
            case TrafficState.GREEN:
                self.state = TrafficState.YELLOW
            case TrafficState.YELLOW:
                self.state = TrafficState.RED

    def run(self):
        """Run the traffic light controller loop indefinitely.

        On each iteration, prints the current state, waits for the
        configured duration, then advances to the next state.
        """
        while True:
            print(f"Current state: {self.state.name}")
            duration = self.state_durations[self.state]
            time.sleep(duration)

            self.next_state()


if __name__ == "__main__":
    controller = TrafficLightController()
    controller.run()
