"""
Reactive robot navigation using a finite state machine.

Simulated obstacle detection with simple state transitions.
"""

from dataclasses import dataclass
from enum import Enum, auto
import random
import time


class RobotState(Enum):
    """Finite state machine states for the reactive robot navigator."""

    IDLE = auto()
    MOVE_FORWARD = auto()
    AVOID_OBSTACLE = auto()
    STOP = auto()


@dataclass
class RobotNavigator:
    """Reactive navigator controlled by a finite state machine.

    The navigator reads a simulated obstacle sensor and changes state when
    it detects a value over a configurable probability threshold.
    """

    state = RobotState.IDLE
    obstacle_threshold = 0.7

    def read_sensor(self):
        """Read the simulated obstacle sensor value.

        Returns:
            float: Random value between 0.0 and 1.0 representing the
                probability of detecting an obstacle.
        """
        return random.random()

    def update(self):
        """Update the robot state based on the sensor reading.

        The transitions are:
        - IDLE -> MOVE_FORWARD on the next cycle.
        - MOVE_FORWARD -> AVOID_OBSTACLE when the reading exceeds the threshold.
        - AVOID_OBSTACLE -> MOVE_FORWARD after one avoidance cycle.
        """
        sensor_value = self.read_sensor()

        match self.state:
            case RobotState.IDLE:
                self.state = RobotState.MOVE_FORWARD
            case RobotState.MOVE_FORWARD if sensor_value > self.obstacle_threshold:
                self.state = RobotState.AVOID_OBSTACLE
            case RobotState.AVOID_OBSTACLE:
                self.state = RobotState.MOVE_FORWARD

    def step(self):
        """Execute one behavior step of the robot.

        Prints the current state and its associated action, then sleeps for
        one second to simulate the passage of time.
        """
        print(f"State: {self.state.name}")

        if self.state == RobotState.MOVE_FORWARD:
            print("Moving forward")
        elif self.state == RobotState.AVOID_OBSTACLE:
            print("Avoiding obstacle")

        time.sleep(1)

    def run(self):
        """Run the main loop of the robot indefinitely.

        On each iteration, the robot updates its state and executes the
        corresponding behavior.
        """
        while True:
            self.update()
            self.step()


if __name__ == "__main__":
    robot = RobotNavigator()
    robot.run()
