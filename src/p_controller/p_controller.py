from imports.import_ev3dev2 import *
from p_controller import paths
from time import sleep


def main(command_array):
    tank_drive = MoveTank(OUTPUT_A, OUTPUT_D)
    left_motor = LargeMotor(OUTPUT_A)
    right_motor = LargeMotor(OUTPUT_D)
    left_motor.reset()
    right_motor.reset()

    gy = GyroSensor(INPUT_2)
    gy.reset()  # reset gyro to 0

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
    
    # Print final encoder positions
    print(f"Left motor encoder position: {left_motor.position}")
    print(f"Right motor encoder position: {right_motor.position}")

    # Print the orientation of the robot using the gyro sensor
    print(f"Final gyro angle: {gy.angle}")

if __name__ == "__main__":
    main(paths.command_circle())
