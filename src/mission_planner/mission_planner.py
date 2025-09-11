from error_collector import rotation_gyro, straight_line_gyro
from imports.import_ev3dev2 import *
from p_controller.paths import circle, lemniscate, reactangle, straight_line
from p_controller import p_controller
from time import sleep
from threading import Thread


def main():
    print("Mission Planner: Starting error collection threads...")

    # Create threads for each error collection script
    thread_array = [
        Thread(target=straight_line_gyro.main),
        Thread(target=rotation_gyro.main),
        Thread(target=p_controller.main, args=(circle.command_circle())),
    ]

    # Start the threads
    for thread in thread_array:
        thread.start()

    # Wait for all threads to complete
    for thread in thread_array:
        thread.join()

    print("Mission Planner: Error collection completed.")


if __name__ == "__main__":
    main()
