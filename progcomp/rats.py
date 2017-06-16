less_than_10000 = list(range(1, 10000))
rats_cycle = []


def rats(item):
    rev_number = int(str(item)[::-1])
    final = int("".join(sorted(str(item + rev_number))))
    return final


def cycle(start):
    current_cycle = [start]
    while True:
        current_number = rats(current_cycle[-1])
        if current_number >= 10e12:
            break
        elif current_number in current_cycle:
            recur_cycle = current_cycle[current_cycle.index(current_number):-2]
            recur_cycle = [str(i) for i in recur_cycle]
            print("Period {}: occurs {} times, cycle {}".format(len(recur_cycle), len(current_cycle), " ".join(recur_cycle)))
            for item in current_cycle:
                if item in less_than_10000:
                    less_than_10000.remove(item)
            break
        else:
            current_cycle.append(current_number)

for number in less_than_10000:
    cycle(number)