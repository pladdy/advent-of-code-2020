# https://adventofcode.com/2020/day/14

memory = {}
mask = None
index = None


def mem_index(mem_string):
    index = thing.removeprefix("mem[")
    return index.removesuffix("]")


def line_to_value(line):
    line = line.rstrip()
    return line.split(" = ")


# part 1

with open("day-14-puzzle.txt") as f:
    for line in f:
        thing, value = line_to_value(line)

        if thing == "mask":
            mask = value
        else:
            index = mem_index(thing)

            bin_val = format(int(value), "036b")
            new_val = []

            for i, c in enumerate(mask):
                if c.lower() == "x":
                    new_val.append(bin_val[i])
                elif c == "1":
                    new_val.append("1")
                else:
                    new_val.append("0")

            memory[index] = "".join(new_val)

    total = 0
    for m in memory:
        total += int(memory[m], 2)
    print(f"Part 1: {total}")

# part 2

memory = {}
mask = None
index = None

with open("day-14-puzzle.txt") as f:
    for line in f:
        thing, value = line_to_value(line)

        if thing == "mask":
            mask = value
        else:
            index = mem_index(thing)

            bin_val = format(int(index), "036b")
            results = []

            for i, c in enumerate(mask):
                if c.lower() == "x":
                    if not results:
                        results = ["0", "1"]
                    else:
                        new_results = []
                        for j, result in enumerate(results):
                            results[j] = result + "0"
                            new_results.append(result + "1")
                        results = results + new_results
                elif c == "1":
                    if not results:
                        results = ["1"]
                    else:
                        for j, result in enumerate(results):
                            results[j] = result + "1"
                else:
                    if not results:
                        results = [bin_val[i]]
                    else:
                        for j, result in enumerate(results):
                            results[j] = result + bin_val[i]

            for result in results:
                memory[int(result, 2)] = int(value)

    total = 0
    for m in memory:
        total += memory[m]
    print(f"Part 2: {total}")
