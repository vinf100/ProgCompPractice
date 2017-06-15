input = raw_input("enter robot time:")

def hour_suffix(hour):
    if hour == 12:
        return "noon"
    elif hour == 0:
        return "midnight"
    elif hour > 12:
        return "am"
    return "pm"

def minute_suffix(minute):
    if minute <= 30:
        return "past"
    elif minute > 30:
        return "to"

def minute_interval(minute):
    if minute % 15 == 0:
        if minute == 30:
            return "half"
        return "a quarter"
    elif minute == 1:
        return " a"
    return minute + "minutes"


def robot_to_human(robot_time):
    hour = int(robot_time[0:2])
    minute = int(robot_time[2:4])

    hour_suffix = hour_suffix(hour)
    minute_suffix = minute_suffix(minute)
    minute_interval = minute_interval(minute)

    return "%s is %s %s %s%s" %(robot, str(minute_interval), str(minute_suffix), robot_hour, am_pm)

print(robot_to_human(input))
