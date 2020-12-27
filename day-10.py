def adapter_diffs(adapters):
    last_outlet = 0
    diffs = {1: 0, 2: 0, 3: 1}
    for adapter in adapters:
        diff = adapter - last_outlet
        diffs[diff] += 1
        last_outlet = adapter
    return diffs


adapters = []

with open("day-10-puzzle.txt") as f:
    for line in f:
        line = line.rstrip()
        adapters.append(int(line))

print(adapters)
adapters.sort()
print(adapters)

diffs = adapter_diffs(adapters)

print(diffs)
print("max: {}, count: {}".format(max(adapters), len(adapters)))
print("1 jolt * 3 jolt: {}".format(diffs[1] * diffs[3]))

sums = {0: 1}

for adapter in adapters:
    sum = 0
    for i in [1, 2, 3]:
        if adapter - i in sums:
            sum += sums[adapter - i]
    sums[adapter] = sum
    print(sums)

print("Total: {}".format(sum))

adapters = [
    28,
    33,
    18,
    42,
    31,
    14,
    46,
    20,
    48,
    47,
    24,
    23,
    49,
    45,
    19,
    38,
    39,
    11,
    1,
    32,
    25,
    35,
    8,
    17,
    7,
    9,
    4,
    2,
    34,
    10,
    3,
]

adapters.sort()
diffs = adapter_diffs(adapters)

print(diffs)
print("max: {}, count: {}".format(max(adapters), len(adapters)))
print("1 jolt * 3 jolt: {}".format(diffs[1] * diffs[3]))

# part 2
# what are all the combinations to get from 0 to 189?
# observations
# every permutation must contain the numbers 3 away
# i looked this up...if you add up the previous possible combos each adapter,
# you'll end up with a grand total
sums = {0: 1}

for adapter in adapters:
    sum = 0
    for i in [1, 2, 3]:
        if adapter - i in sums:
            sum += sums[adapter - i]
    sums[adapter] = sum
    print(sums)

print("Total: {}".format(sum))
