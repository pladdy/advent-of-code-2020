numbers = []

with open("day-9-puzzle.txt") as f:
    for line in f:
        line = line.rstrip()
        numbers.append(int(line))

preamble = numbers[0:25]

# print(preamble)

missing_number = None
for i in range(len(preamble), len(numbers)):
    next_number = numbers[i]
    # print("next number: {}".format(next_number))

    misses = 0
    for n in preamble:
        # print("checking against {}".format(n))
        if n >= next_number:
            misses += 1
            continue

        diff = abs(next_number - n)
        # print("  need a diff of {}".format(diff))
        if diff != next_number and diff not in preamble:
            misses += 1

    if misses == len(preamble):
        missing_number = next_number
        print("Number {} doesn't have a preamble combo.".format(next_number))
        break

    # print("misses: {}".format(misses))

    preamble.pop(0)
    preamble.append(next_number)
    # print(preamble)

# part 2
sum = 0
sum_list = []
index = last_index = 0

while index <= len(numbers):
    sum += numbers[index]
    sum_list.append(numbers[index])
    index += 1

    if sum == missing_number:
        print("Continguos sum found")
        break

    if sum > missing_number:
        sum = 0
        sum_list = []
        last_index += 1
        index = last_index


print("Encryption weakness: {}".format(min(sum_list) + max(sum_list)))
