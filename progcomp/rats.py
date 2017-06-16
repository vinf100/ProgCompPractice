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

        if current_number in current_cycle:
            rats_cycle.append({
                "cycle": current_cycle
            })

            for item in current_cycle:
                less_than_10000.remove(item)
            break
        else:
            current_cycle.insert(current_number, len(current_cycle))
for number in less_than_10000:
    cycle(number)

print(rats_cycle)