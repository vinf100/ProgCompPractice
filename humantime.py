time_input = input("enter robot time:")


def set_hour_suffix(hour):
    if hour == 12:
        return " noon"
    elif hour == 0:
        return " midnight"
    elif hour > 12:
        return "am"
    return "pm"


def set_minute_suffix(minute):
    if minute <= 30:
        return " past"
    elif minute > 30:
        return " to"


def set_minute_interval(minute):
    if minute % 15 == 0:
        if minute == 30:
            return " half"
        return " a quarter"
    elif minute == 1:
        return " a"
    return " {} minutes".format(minute)


def robot_to_human(robot_time):
    hour = int(robot_time[0:2])
    minute = int(robot_time[2:4])

    hour_suffix = set_hour_suffix(hour)
    minute_suffix = set_minute_suffix(minute)
    minute_interval = set_minute_interval(minute)

    return "{} is{}{} {}{}".format(robot_time, minute_interval, minute_suffix, hour, hour_suffix)


print(robot_to_human(time_input))
