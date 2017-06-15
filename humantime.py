time_input = input("enter robot time:")


def robot_to_human(robot_time):
    hour = int(robot_time[0:2])
    minute = int(robot_time[2:4])

    minute_suffix = ""
    minute_interval = ""

    if hour >= 12:
        hour_suffix = "pm"
        hour -= 12
    else:
        minute_suffix = "am"

    if hour % 12 == 0:
        if hour == 12:
            hour_suffix = " noon"
        else:
            hour_suffix = " midnight"
            hour += 12

    if minute > 0:
        # set past
        if minute <= 30:
            minute_suffix = " past"
        elif minute > 30:
            minute_suffix = " to"
            minute -= 30

        # set minute interval
        if minute == 30:
            minute_interval = " half"
        elif minute == 15:
            minute_interval = " a quarter"
        elif minute == 1:
            minute_interval = " a"
        else:
            minute_interval = " {} minutes".format(minute)

    return "{} is{}{} {}{}".format(robot_time, minute_interval, minute_suffix, hour, hour_suffix)


print(robot_to_human(time_input))
