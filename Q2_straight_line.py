from time import sleep

from ev3dev2.motor import LargeMotor, OUTPUT_A, OUTPUT_D, SpeedPercent, MoveTank
from ev3dev2.sensor import INPUT_1, INPUT_2
from ev3dev2.sensor.lego import TouchSensor, GyroSensor
from ev3dev2.led import Leds

gy = GyroSensor(INPUT_2)
gy.reset() # reset gyro to 0

tank_drive = MoveTank(OUTPUT_A, OUTPUT_D)

# drive in straight line
print("Q2 A: drive in straight line")

init_gy_angle = gy.angle
angles_during_trial =[]

iters=30
straight_line_speed=30
for i in range(iters):
    tank_drive.on(SpeedPercent(straight_line_speed), SpeedPercent(straight_line_speed))
    curr_angle = gy.angle
    angles_during_trial.append(curr_angle)

errors_during_trial=[]
for angle in angles_during_trial:
    errors_during_trial.append(abs(angle-init_gy_angle)) #we could do abs OR we could do **2 

print("METHOD1, GYRO: errors during trial:", errors_during_trial)

avg_error = sum(errors_during_trial) / len(errors_during_trial)
print("METHOD1, GYRO: average error during trial:", avg_error)

