from imports.import_ev3dev2 import *
from p_controller import paths
from time import sleep


def main(command_array):
    tank_drive = MoveTank(OUTPUT_A, OUTPUT_D)

    for command in command_array:
        left_speed = command[0]
        right_speed = command[1]
        duration = command[2]

        print(
            f"P Controller: Moving with left speed {left_speed}, right speed {right_speed} for {duration} seconds."
        )
        tank_drive.on_for_seconds(
            SpeedPercent(left_speed), SpeedPercent(right_speed), duration
        )


if __name__ == "__main__":
    main(paths.command_circle())
