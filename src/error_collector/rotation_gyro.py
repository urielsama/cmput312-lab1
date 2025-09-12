# rot in some way

# how to perform rotation? lets say we want to rotate x degrees... what does this mean?

from time import sleep

from imports.import_ev3dev2 import *


def main():
    gy = GyroSensor(INPUT_2)
    gy.reset()  # reset gyro to 0

    tank_drive = MoveTank(OUTPUT_A, OUTPUT_D)

    # drive in straight line
    print("Q2 B: rotate")

    init_gy_angle = gy.angle
    angles_during_trial = []
    errors_during_trial=[]

    seconds = 5
    hz = 60
    for i in range(seconds * hz):
        sleep(1 / hz)
        curr_angle = gy.angle
        angles_during_trial.append(curr_angle)
        errors_during_trial.append(abs(curr_angle-init_gy_angle))

    print("METHOD1, GYRO: errors during trial:", errors_during_trial)

    avg_error = sum(errors_during_trial) / len(errors_during_trial)
    print("METHOD1, GYRO: average error during trial:", avg_error)


if __name__ == "__main__":
    main()
