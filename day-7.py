bags = {}


def count_bags(bag, bags_dict, last_count=1):
    print("count_bags called with bag {} and last_count {}".format(bag, last_count))
    child_bags = bags_dict.get(bag.get("bag"))
    total = last_count

    for b in child_bags:
        count = child_bags.get(b)
        total += count_bags({"bag": b, "count": count}, bags_dict, count * last_count)

    return total


def find_bag(bag, search, bags_dict):
    # print("searching for bag '{}' in '{}'".format(search, bag))

    child_bags = bags_dict.get(bag)
    # print("  bags inside '{}' are {}".format(bag, child_bags))

    if search in child_bags:
        return bag

    for b in child_bags:
        if find_bag(b, search, bags_dict):
            return b
    return None


with open("day-7-puzzle.txt") as f:
    for line in f:
        line = line.rstrip()
        line = line.rstrip(".")

        container, contains = map(str.strip, line.split("contain"))
        container = container.replace("bags", "bag")
        bags[container] = {}

        if contains == "no other bags":
            continue

        contains = list(map(str.strip, contains.split(",")))
        for bag in contains:
            count, bag = bag.split(" ", maxsplit=1)
            bag = bag.replace("bags", "bag")
            bags[container][bag] = int(count)

# how many bag colors, can eventually contain a shiny gold bag?
eligible_bags = set()
for bag in bags:
    if find_bag(bag, "shiny gold bag", bags):
        eligible_bags.add(bag)

print("Eligible Bags: {}".format(eligible_bags))
print("Eligible Bag Count: {}".format(len(eligible_bags)))

# part 2
child_bags = bags.get("shiny gold bag")
print("Shiny gold bag has {} child bags".format(child_bags))

total = 0
for bag in child_bags:
    count = child_bags.get(bag)
    print("child bag: {}, count: {}".format(bag, count))
    total += count * count_bags({"bag": bag, "count": count}, bags)

print("Total bags: {}".format(total))

# shiny gold bags contain 2 dark red bags.
# dark red bags contain 2 dark orange bags.
# dark orange bags contain 2 dark yellow bags.
# dark yellow bags contain 2 dark green bags.
# dark green bags contain 2 dark blue bags.
# dark blue bags contain 2 dark violet bags.
# dark violet bags contain no other bags.
# 2 dark reds
# 4 dark orange
# 8 dark yellow
# 16 dark green
# 32 dark blue
# 64 dark violet
# 126
