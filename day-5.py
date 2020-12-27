# plane rows: 0 - 127
# first 7 chars is location via binary search (7 halves)
# 0..63, 64..127
# 0..31, 32..63 ; 64..95, 96..127
# etc.
#
# 8 plane columns
# last 3 chars is location via binary search (3 halves)
#
# seat id is row * 8 + colums


def boarding_pass_col(boarding_pass):
    min, max = (0, 7)
    bins = boarding_pass[7:10]
    return enumerate_bins(bins, min, max)


def boarding_pass_id(boarding_pass):
    row = boarding_pass_row(boarding_pass)
    col = boarding_pass_col(boarding_pass)
    return row * 8 + col


def boarding_pass_row(boarding_pass):
    min, max = (0, 127)
    bins = boarding_pass[0:7]
    return enumerate_bins(bins, min, max)


def enumerate_bins(bins, min, max):
    rows = max
    for i, b in enumerate(bins):
        rows = rows // 2
        if b == "F" or b == "L":
            if i == len(bins) - 1:
                return min
            min, max = (min, max - rows - 1)
        if b == "B" or b == "R":
            if i == len(bins) - 1:
                return max
            min, max = (min + rows + 1, max)
    raise


boarding_passes = []

with open("day-5-puzzle.txt") as f:
    boarding_passes = [line.rstrip() for line in f]

max_id = 0
ids = []
for boarding_pass in boarding_passes:
    id = boarding_pass_id(boarding_pass)
    ids.append(id)
    if id > max_id:
        max_id = id

print("Max ID: {}".format(max_id))

# part 2

ids.sort()
print("Total IDs: {}".format(len(ids)))
# print(ids)

last_id = ids[0]
ids_with_gap = []

# if there's a diff of more than 1 between ids, the id i want is in between
for i, id in enumerate(ids):
    if i == len(ids) - 1:
        break
    if id - last_id > 1:
        ids_with_gap.append(last_id)
        ids_with_gap.append(id)
    last_id = id

print("Potential IDs: {}".format(len(ids_with_gap)))
print(ids_with_gap)
print("ID: {}".format(ids_with_gap[0] + 1))
