import functools

# part 1

uniques_per_group = []

with open("day-6-puzzle.txt") as f:
    letters = set()
    for line in f:
        line = line.rstrip()

        if line == "":
            uniques_per_group.append(len(letters))
            letters.clear()
            continue

        [letters.add(c) for c in list(line)]

    uniques_per_group.append(len(letters))

print(uniques_per_group)
print("Total: {}".format(sum(uniques_per_group)))

# part 2

shared_uniques = []
question_sets = []


def intersections(sets):
    return list(functools.reduce(set.intersection, sets))


with open("day-6-puzzle.txt") as f:
    for line in f:
        letters = set()
        line = line.rstrip()

        if line == "":
            shared_uniques.append(len(intersections(question_sets)))
            print(shared_uniques)
            letters.clear()
            question_sets = []
            continue

        [letters.add(c) for c in list(line)]
        question_sets.append(letters.copy())

    shared_uniques.append(len(intersections(question_sets)))

print(shared_uniques)
print("Total: {}".format(sum(shared_uniques)))
