import copy


def any_occupied_seats(state, coordinates):
    for coordinate in coordinates:
        r, c = coordinate
        if state[r][c] == "#":
            return True
    return False


def neighbors(row, col, max_row, max_col):
    """Given an row, col, return a list of tuples for each neighbor.

    Min row/col can be assumed to be 0
    """
    ns = []

    for i in [-1, 0, 1]:
        for j in [-1, 0, 1]:
            if i == 0 and j == 0:
                continue  # skip self
            new_row = row + i
            new_col = col + j
            if (
                new_row >= 0
                and new_row <= max_row
                and new_col >= 0
                and new_col <= max_col
            ):
                ns.append((new_row, new_col))

    return ns


def neighbors2(state, row, col, max_row, max_col):
    ns = []

    for r in [-1, 0, 1]:
        for c in [-1, 0, 1]:
            if r == 0 and c == 0:
                continue

            next_row = row + r
            next_col = col + c

            while (
                next_row >= 0
                and next_row <= max_row
                and next_col >= 0
                and next_col <= max_col
            ):
                if state[next_row][next_col] != ".":
                    ns.append((next_row, next_col))
                    break
                next_row = next_row + r
                next_col = next_col + c
                # print(
                #     "row {} col {} r {} c {} next_row {} next_col {}".format(
                #         row, col, r, c, next_row, next_col
                #     )
                # )
    # print("  neighbors: {}".format(ns))
    return ns


def print_state(state):
    for row in state:
        print(row)
    print("---")


def too_many_neighbors(state, coordinates, max=4):
    count = 0
    for coordinate in coordinates:
        r, c = coordinate
        if state[r][c] == "#":
            count += 1
    return count >= max


puzzle = []

with open("day-11-puzzle.txt") as f:
    for i, line in enumerate(f):
        puzzle.append([])
        line = line.rstrip()
        for char in line:
            puzzle[i].append(char)

# test = """L.LL.LL.LL
# LLLLLLL.LL
# L.L.L..L..
# LLLL.LL.LL
# L.LL.LL.LL
# L.LLLLL.LL
# ..L.L.....
# LLLLLLLLLL
# L.LLLLLL.L
# L.LLLLL.LL"""
#
# puzzle = []
# for i, line in enumerate(test.split("\n")):
#     puzzle.append([])
#     line = line.strip()
#     for char in line:
#         puzzle[i].append(char)

current_state = copy.deepcopy(puzzle)
next_state = copy.deepcopy(puzzle)
max_rows = len(puzzle) - 1
max_cols = len(puzzle[0]) - 1
changed = True

# part 1
print_state(current_state)

while changed:
    changed = False
    occupied = 0

    for r, row in enumerate(current_state):
        for c, char in enumerate(row):
            if char == ".":
                continue

            if char == "#":
                occupied += 1

            ns = neighbors(r, c, max_rows, max_cols)

            if char == "L" and not any_occupied_seats(current_state, ns):
                next_state[r][c] = "#"
                changed = True

            if char == "#" and too_many_neighbors(current_state, ns):
                next_state[r][c] = "L"
                changed = True

    if changed:
        current_state = copy.deepcopy(next_state)

print("Occupied: {}".format(occupied))

# part 2
current_state = copy.deepcopy(puzzle)
next_state = copy.deepcopy(puzzle)
max_rows = len(puzzle) - 1
max_cols = len(puzzle[0]) - 1
changed = True

print_state(current_state)

while changed:
    changed = False
    occupied = 0

    for r, row in enumerate(current_state):
        for c, char in enumerate(row):
            if char == ".":
                continue

            if char == "#":
                occupied += 1

            ns = neighbors2(current_state, r, c, max_rows, max_cols)

            if char == "L" and not any_occupied_seats(current_state, ns):
                next_state[r][c] = "#"
                changed = True

            if char == "#" and too_many_neighbors(current_state, ns, max=5):
                next_state[r][c] = "L"
                changed = True

    if changed:
        # print_state(next_state)
        current_state = copy.deepcopy(next_state)
        # exit()

print("Occupied: {}".format(occupied))
