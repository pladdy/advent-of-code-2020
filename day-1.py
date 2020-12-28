# Find two entries that sum to 2020
# sort numbers, first, then do some ugly for loops bro

nums = []
with open("day-1-puzzle.txt") as f:
    for line in f:
        line = line.rstrip()
        nums.append(int(line))

nums.sort()
found = False

print("Find 2 numbers that sum 2020")

for m in nums:
    for n in nums:
        if n == m:
            continue
        total = n + m
        if total == 2020:
            print("  Matches found.  {} and {}".format(m, n))
            print("  Solution: {}".format(m * n))
            found = True
            break
        if total > 2020:
            continue
    if found:
        break

found = False
print("Find 3 numbers that total 2020")

# this hurts...x^3?
for m in nums:
    for n in nums:
        for o in nums:
            if len(set([m, n, o])) < 3:
                continue
            total = n + m + o
            if total == 2020:
                print("  Matches found.  {} and {} and {}".format(m, n, o))
                print("  Solution: {}".format(m * n * o))
                found = True
                break
            if total > 2020:
                continue
        if found:
            break
    if found:
        break
