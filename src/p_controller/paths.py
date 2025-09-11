def command_circle():
    return [
        (20, 100, 4),  # (left_speed, right_speed,
    ]


def command_lemniscate():
    return [
        (50, 100, 2),  # (left_speed, right_speed, duration)
        (100, 50, 2),  # (left_speed, right_speed, duration)
    ]


def command_rectangle():
    return [
        (50, 50, 2),  # Move forward
        (50, -50, 1),  # Turn right
        (50, 50, 2),  # Move forward
        (50, -50, 1),  # Turn right
        (50, 50, 2),  # Move forward
        (50, -50, 1),  # Turn right
        (50, 50, 2),  # Move forward
        (50, -50, 1),  # Turn right to original orientation
    ]


def command_straight_line():
    return [
        (50, 50, 5),  # Move forward for 5 seconds
    ]
