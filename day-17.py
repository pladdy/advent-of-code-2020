import functools
import itertools

from copy import copy

INACTIVE = "."
ACTIVE = "#"
POCKET_DIMENSION_FILE = "day-17-puzzle.txt"


def list_neighbors(point):
    """Given a point `[x, ...]` return its neighbors."""
    neighbor_offsets = [-1, 0, 1]
    neighbors = []

    # iterate through each combination of offsets to create neighbors
    for p in itertools.product(neighbor_offsets, repeat=len(point)):
        # add pairs together to form new point
        new_point = list(
            itertools.starmap(lambda x, y: x + y, itertools.zip_longest(p, point))
        )
        if new_point != point:
            neighbors.append(new_point)
    return neighbors


def nested_get(d, keys):
    # call get on each dict returned; return final value
    return functools.reduce(lambda d, x: d.get(x, {}), keys, d)


def nested_set(d, keys, value):
    for key in keys[:-1]:
        d = d.setdefault(key, {})
    d[keys[-1]] = value


class PocketDimension:
    def __init__(self, dimensions):
        self.cubes = {}
        self.cube_points = []

        with open(POCKET_DIMENSION_FILE) as f:
            point = [0 for _ in range(dimensions)]
            self.cubes[point[0]] = {}

            for line in f:
                for status in list(line.rstrip()):
                    p = copy(point)
                    cube = Cube(p, status)
                    nested_set(self.cubes, p, cube)
                    self.cube_points.append(p)
                    point[1] += 1
                point[0] += 1
                point[1] = 0
                self.cubes[point[0]] = {}

            # add neighboring cubes
            points = copy(self.cube_points)
            for point in points:
                neighbors = list_neighbors(point)
                for neighbor in neighbors:
                    self.get(neighbor)

    def __repr__(self):
        size = 0
        for point in self.cube_points:
            if self.get(point).is_active():
                size += 1
        return f"Active Cube: {size}"

    def get(self, point):
        cube = nested_get(self.cubes, point)
        if cube:
            return cube
        else:
            cube = Cube(point, INACTIVE)
            nested_set(self.cubes, point, cube)
            self.cube_points.append(point)
            return cube

    def run_cycles(self, cycles):
        for cycle in range(cycles):
            points = copy(self.cube_points)

            for point in points:
                cube = self.get(point)
                active_neighbors = 0
                inactive_neighbors = 0

                for neighbor in cube.neighbors:
                    if self.get(neighbor).is_active():
                        active_neighbors += 1
                    else:
                        inactive_neighbors += 1

                if cube.is_active():
                    if active_neighbors == 2 or active_neighbors == 3:
                        cube.status = ACTIVE
                    else:
                        cube.status = INACTIVE
                elif not cube.is_active() and active_neighbors == 3:
                    cube.status = ACTIVE

            # swap statuses; TODO: put in class?
            for point in self.cube_points:
                cube = self.get(point)
                cube.last_status = cube.status

            print(f"Cycle {cycle+1}: {pocket_dimension}")


class Cube:
    def __init__(self, point, status):
        self.point = point
        self.last_status = self.status = status
        self._neighbors = None

    def __repr__(self):
        reps = [
            f"<Cube: point: {self.point}"
            f" Status: '{self.status}'>"
            f" Last Status: '{self.last_status}'>"
        ]
        return "".join(reps)

    @property
    def neighbors(self):
        if self._neighbors:
            return self._neighbors
        else:
            self._neighbors = list_neighbors(self.point)
            return self._neighbors

    def is_active(self):
        return self.last_status == ACTIVE


cycles = 6

# part 1
print("Part 1")
pocket_dimension = PocketDimension(3)
print(f"Before cycles: {pocket_dimension}")
pocket_dimension.run_cycles(cycles)


# part 2

print("Part 2")
pocket_dimension = PocketDimension(4)
print(f"Before cycles: {pocket_dimension}")
pocket_dimension.run_cycles(cycles)
