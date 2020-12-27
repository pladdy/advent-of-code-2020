def direction_and_value(raw_dir, current_index):
    """Return the value and current_index."""
    dir, value = raw_dir[0], int(raw_dir[1:])

    if dir in ["N", "S", "E", "W"]:
        return value, current_index

    if dir in ["L", "R"]:
        offset = value // 90

        if dir == "L":
            current_index = (current_index - offset) % -4
        if dir == "R":
            current_index = (current_index + offset) % 4

        return 0, current_index

    if dir == "F":
        return value, current_index


def manhattan_distance(direction_values):
    return abs(
        abs(direction_values.get("E", 0)) - abs(direction_values.get("W", 0))
    ) + abs(abs(direction_values.get("N", 0)) - abs(direction_values.get("S", 0)))


# directions list, order matters so "turns" can be done using array offsets.
# current direction is the index of the array (starts at 0)
# turns are executed with value % 90
directions = ["E", "S", "W", "N"]
current_index = 0
direction_values = {"N": 0, "S": 0, "W": 0, "E": 0}

with open("day-12-puzzle.txt") as f:
    for line in f:
        line = line.rstrip()
        value, current_index = direction_and_value(line, current_index)

        if line[0] in directions:
            direction_values[line[0]] += value
        if line[0] == "F":
            direction_values[directions[current_index]] += value

print(direction_values)
print("M. Distance: {}".format(manhattan_distance(direction_values)))

# part 2


# a waypoint is just a location on a graph, an x/y axis and the location is in
# in one of four quadrants.
# N and S are y axis
# E and W are x axis
# W and S are negative values
# N and E are positive values
class Waypoint:
    def __init__(self):
        self.x = 10
        self.y = 1

    def __repr__(self):
        return "x: {}, y: {}".format(self.x, self.y)

    def move(self, direction, value):
        if direction == "N":
            self.y += value
        elif direction == "S":
            self.y -= value
        elif direction == "W":
            self.x -= value
        elif direction == "E":
            self.x += value

    def rotate(self, direction, angle):
        if direction not in ["L", "R"]:
            return

        if direction == "R":
            angle = 360 - angle

        if angle == 90:
            new_y = self.x
            self.x = -1 * self.y
            self.y = +1 * new_y
        elif angle == 180:
            self.x = -1 * self.x
            self.y = -1 * self.y
        elif angle == 270:
            new_y = self.x
            self.x = +1 * self.y
            self.y = -1 * new_y


location_x = 0
location_y = 0
waypoint = Waypoint()

with open("day-12-puzzle.txt") as f:
    for line in f:
        line = line.rstrip()
        dir, value = line[0], int(line[1:])

        if dir in ["N", "S", "W", "E"]:
            waypoint.move(dir, value)

        if dir in ["L", "R"]:
            waypoint.rotate(dir, value)

        if dir == "F":
            location_x += value * waypoint.x
            location_y += value * waypoint.y

        print(
            "Dir: {}, Value: {}, Waypoint: {}, X: {}, Y: {}".format(
                dir, value, waypoint, location_x, location_y
            )
        )

print("Waypoint: {}".format(waypoint))
print(direction_values)
print("M. Distance: {}".format(abs(location_x) + abs(location_y)))
