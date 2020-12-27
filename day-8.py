def run(opts):
    ops_run = {}
    index = 0
    accumulator = 0

    while index < len(opts):
        op, value = opts[index]
        # print("index: {}, op: {}, value: {}".format(index, op, value))

        if index in ops_run:
            ops_run[index]["count"] += 1
        else:
            ops_run[index] = {
                "count": 1,
                "index": index,
                "op": op,
                "value": value,
            }

        if ops_run[index]["count"] > 1:
            # print("Infinite Loop.  Accumulatr: {}".format(accumulator))
            break

        # handle ops
        if op == "acc":
            accumulator += int(value)

        # print("  accumulator: {}".format(accumulator))

        if op == "jmp":
            index += int(value)
            continue

        index += 1

    if index not in ops_run:
        return ops_run, 1, accumulator
    return ops_run, ops_run[index]["count"], accumulator


opts = []

with open("day-8-puzzle.txt") as f:
    for line in f:
        line = line.rstrip()
        op, value = line.split(" ")
        opts.append((op, value))

ops_run, exit_code, accumulator = run(opts)

# part 2

ops_to_flip = {}
for k, v in ops_run.items():
    if v["op"] == "jmp" or v["op"] == "nop":
        ops_to_flip[k] = v

print("Ops Run: {}".format(ops_run))
print("Ops to Flip: {}".format(ops_to_flip))

for k, v in ops_to_flip.items():
    old_op = opts[k]

    # swap ops
    if old_op[0] == "jmp":
        opts[k] = ("nop", old_op[1])
    if old_op[0] == "nop":
        opts[k] = ("jmp", old_op[1])

    ops_run, exit_code, accumulator = run(opts)

    if exit_code <= 1:
        print("Accumulator: {}".format(accumulator))
        break

    # flip it back
    opts[k] = old_op
