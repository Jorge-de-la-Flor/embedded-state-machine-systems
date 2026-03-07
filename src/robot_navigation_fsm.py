"""
Reactive robot navigation using a finite state machine.
Simulated obstacle detection with simple transitions.
"""
from dataclasses import dataclass
from enum import Enum, auto
import random
import time


class RobotState(Enum):
    IDLE = auto()
    MOVE_FORWARD = auto()
    AVOID_OBSTACLE = auto()
    STOP = auto()

@dataclass
class RobotNavigator:
    state = RobotState.IDLE
    obstacle_threshold = 0.7

    def read_sensor(self):
        return random.random()

    def update(self):
        sensor_value = self.read_sensor()

        match self.state:
            case RobotState.IDLE:
                self.state = RobotState.MOVE_FORWARD
            case RobotState.MOVE_FORWARD if sensor_value > self.obstacle_threshold:
                self.state = RobotState.AVOID_OBSTACLE
            case RobotState.AVOID_OBSTACLE:
                self.state = RobotState.MOVE_FORWARD

    def step(self):
        print(f"State: {self.state.name}")

        if self.state == RobotState.MOVE_FORWARD:
            print("Moving forward")
        elif self.state == RobotState.AVOID_OBSTACLE:
            print("Avoiding obstacle")

        time.sleep(1)

    def run(self):
        while True:
            self.update()
            self.step()


if __name__ == "__main__":
    robot = RobotNavigator()
    robot.run()