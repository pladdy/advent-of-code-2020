def find_trees(right, down):
    tree = "#"
    tree_count = 0
    index = 0

    with open("day-3-puzzle.txt") as f:
        line_count = 0
        for line in f:
            line_count += 1
            index += right

            if line_count == 1:
                index = 0
                continue

            for _ in range(1, down):
                line = f.readline()
                line_count += 1

            line = line.rstrip()
            char = line[index % len(line)]
            if char == tree:
                tree_count += 1

    return tree_count


# part 1
print("Trees: {}".format(find_trees(3, 1)))

# part 2
print(
    "Result: {}".format(
        find_trees(1, 1)
        * find_trees(3, 1)
        * find_trees(5, 1)
        * find_trees(7, 1)
        * find_trees(1, 2)
    )
)
