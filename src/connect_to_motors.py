#!/usr/bin/env python3

from time import sleep

from ev3dev2.motor import LargeMotor, OUTPUT_A, OUTPUT_D, SpeedPercent, MoveTank
from ev3dev2.sensor import INPUT_1, INPUT_2
from ev3dev2.sensor.lego import TouchSensor, GyroSensor
from ev3dev2.led import Leds

gy = GyroSensor(INPUT_2)

tank_drive = MoveTank(OUTPUT_A, OUTPUT_D)

while True:
    print(gy.angle)
    sleep(0.1)
angle1 = gy.angle

# drive in a turn for 5 rotations of the outer motor
# the first two parameters can be unit classes or percentages.
# tank_drive.on_for_rotations(SpeedPercent(50), SpeedPercent(75), 10)

# drive in a different turn for 3 seconds
tank_drive.on_for_seconds(SpeedPercent(4), SpeedPercent(3), 3)

angle2 = gy.angle

print(angle1)
print(angle2)
