from time import sleep
from imports.import_ev3dev2 import *


def main():
    left_motor = LargeMotor(OUTPUT_A)
    right_motor = LargeMotor(OUTPUT_D)
    left_motor.reset()
    right_motor.reset()
    left_encoder = left_motor.position
    right_encoder = right_motor.position

    encoder_readings = []
    seconds = 5
    hz = 60
    for i in range(seconds * hz):
        sleep(1 / hz)
        left_encoder = left_motor.position
        right_encoder = right_motor.position
        encoder_readings.append((left_encoder, right_encoder))

    print("Encoder readings:", encoder_readings)
    file = open("straight_line_encoder_data.txt", "w")
    file.write(str(encoder_readings))
    file.close()


if __name__ == "__main__":
    main()
