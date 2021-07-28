def range_to_set(r):
    start, end = r[0], r[1]
    return set(i for i in range(start, end + 1))


def parse_field(line):
    # print("line:", line.rstrip())
    field, ranges = line.rstrip().split(":")
    range1, range2 = ranges.strip().split(" or ")
    return {
        "field": field,
        "start": range_to_set(list(map(int, range1.split("-")))),
        "end": range_to_set(list(map(int, range2.split("-")))),
    }


def parse_ticket(line):
    return list(map(int, line.rstrip().split(",")))


def parse_tickets():
    parsers = [parse_field, parse_ticket, parse_ticket]
    parser = 0
    tickets = []
    ticket_dict = {}

    with open("day-16-puzzle.txt") as f:
        for line in f:
            parsed = None

            if line == "\n":
                parser += 1
                continue
            elif line.endswith(":\n"):
                continue
            else:
                parsed = parsers[parser](line)

            if parsed:
                if "field" in parsed:
                    ticket_dict[parsed.get("field")] = parsed.get(
                        "start"
                    ).union(parsed.get("end"))
                else:
                    tickets.append(parsed)
    return tickets, ticket_dict


# parsers for each section of the puzzle file
tickets, ticket_dict = parse_tickets()
my_ticket = tickets.pop(0)

# part 1
valid_tickets = []
error_values = []

for ticket in tickets:
    valid = True
    for value in ticket:
        errors = 0
        for k, v in ticket_dict.items():
            if value not in v:
                errors += 1

        if errors == len(ticket):
            error_values.append(int(value))
            valid = False
            break
    if valid:
        valid_tickets.append(ticket)

print(f"Tickets: {len(tickets)}")
print(f"Tickets with errors: {len(error_values)}")
print(f"Error rate: {sum(error_values)}")

# part 2


def ticket_values(index, tickets):
    values = []
    for ticket in tickets:
        values.append(ticket[index])
    return set(values)


print(f"Tickets without errors: {len(valid_tickets)}")

position_dict = {k: None for k, _ in ticket_dict.items()}
positions = list(range(len(my_ticket)))

while len(positions) > 0:
    for field, v in ticket_dict.items():
        possible_positions = []

        for i in positions:
            if len(ticket_values(i, valid_tickets).difference(v)) == 0:
                possible_positions.append(i)

        if len(possible_positions) == 1:
            positions.remove(possible_positions[0])
            position_dict[field] = possible_positions[0]
            break
final = (
    my_ticket[position_dict["departure location"]]
    * my_ticket[position_dict["departure station"]]
    * my_ticket[position_dict["departure platform"]]
    * my_ticket[position_dict["departure track"]]
    * my_ticket[position_dict["departure date"]]
    * my_ticket[position_dict["departure time"]]
)

print(f"Final: {final}")
