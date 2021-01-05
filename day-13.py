def buses_with_ids(buses):
    return list(filter(lambda b: b != "x", buses))


def read_buses():
    with open("day-13-puzzle.txt") as f:
        lines = f.readlines()
        timestamp = int(lines[0])
        buses_str = lines[1].rstrip()
        buses = buses_str.split(",")

        def to_int(v):
            if v != "x":
                return int(v)
            return v

        buses = list(map(to_int, buses))
        return buses, timestamp


buses, timestamp = read_buses()
buses = buses_with_ids(buses)
buses.sort()

print("Timestamp: {}, Buses: {}".format(timestamp, buses))

best_bus = None
min_diff = -timestamp

for bus in buses:
    result = timestamp // bus
    result *= bus
    result += bus
    diff = timestamp - result

    if diff > min_diff:
        best_bus = bus
        min_diff = diff

    # print("Bus: {}, diff: {}".format(bus, diff))

print(
    "Best bus: {}, Diff: {}, Mins: {}".format(
        best_bus, abs(min_diff), best_bus * abs(min_diff)
    )
)

# part 2, fails to finish running
buses, _ = read_buses()

# testing and notes
# - each bus number is prime!
# buses = [17, "x", 13, 19]  # 3417
# buses = [67, 7, 59, 61]  # 754018
# buses = [67, "x", 7, 59, 61]  # 779210
# buses = [67, 7, "x", 59, 61]  # 1261476
# buses = [1789, 37, 47, 1889]  # 1202161486

# make a list of buses with ids and their index in the bus list
# bus_list = {}
# for i, bus in enumerate(buses):
#     if bus == "x":
#         continue
#     bus_list[bus] = i

# using the largest bus as the starting timestamp and increment won't finish
# except for the tests above.
# since this algorithm is faulty, we don't need to check for aligned schedules_
# as the new algorithm will account for them
# max_bus = max(buses_with_ids(buses))
# max_bus_index = bus_list[max_bus]
# schedules_aligned = False

# part 2, success!
# many thanks to the great explainer and programmer at https://todd.ginsberg.com/post/advent-of-code/2020/day13/
timestamp = buses[0]
increment = buses[0]

print(f"Buses to find aligned schedules for: {bus_list}")
# print(f"Increment to use: {increment}")

for i, bus in enumerate(buses):
    # print(f"Working on bus {bus} at index {i}")

    if i == 0:
        continue

    if bus == "x":
        continue

    while (timestamp + i) % bus != 0:
        timestamp += increment

    # print(f"  Found a matching timestamp of {timestamp}")
    # print(f"    Increment {increment} * {bus} will be {increment * bus}")
    increment = increment * bus  # new ratio
    # print(f"      New increment of {increment}")

print(timestamp)
