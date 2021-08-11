# Notes
# choosing prefix seems like it's not worth it.  the strings are revered to
# convert infix -> prefix and then when computing them reveresed again...
# I'd recommend postfix.

operator_map = {"+": lambda x, y: x + y, "*": lambda x, y: x * y}


def evaluate_ltr(line):
    """This is brittle, can't handle precedence."""
    line = line.replace(" ", "")
    operator = None
    operands = []

    i = 0

    for _ in line:
        c = line[i]

        if c in ["+", "*"]:
            operator = c
        elif c == "(":
            i += 1
            operand, length = evaluate_ltr(line[i:])
            operands.append(operand)
            i += length
        elif c == ")":
            return operands[0], i
        else:
            operands.append(int(c))

        if len(operands) == 2:
            operands = [operator_map[operator](*operands)]

        if i >= len(line) - 1:
            return operands[0], i
        i += 1


def infix_to_prefix(line):
    precedence = {"+": 3, "*": 2, ")": 1}
    operators = []
    output = []

    # pad parens so split will separate operands and parens as separate tokens
    line = line.replace("(", "( ")
    line = line.replace(")", " )")
    tokens = line.split()
    tokens.reverse()

    for token in tokens:
        if token in "1234567890":
            output.insert(0, token)
        elif token == ")":
            operators.append(token)
        elif token == "(":
            top = operators.pop()
            while top != ")":
                output.insert(0, top)
                top = operators.pop()
        else:
            while (
                len(operators) > 0
                and precedence[operators[-1]] >= precedence[token]
            ):
                output.insert(0, operators.pop())
            operators.append(token)

    while len(operators) > 0:
        output.insert(0, operators.pop())
    return " ".join(output)


def operate_ltr(line):
    result, length = evaluate_ltr(line)
    return result


def prefix_compute(prefix):
    # print(prefix)
    operands = []
    operators = []
    tokens = prefix.split()
    tokens.reverse()

    for token in tokens:
        if token in "1234567890":
            operands.append(token)
        else:
            if len(operands) > 1:
                new_operand = operator_map[token](
                    int(operands.pop()), int(operands.pop())
                )
                operands.append(new_operand)
            else:
                operators.append(token)
    return operands[0]


# test
print("Running tests")
tests = [
    ["2 * 3 + (4 * 5)", 26],
    ["5 + (8 * 3 + 9 + 3 * 4 * 3)", 437],
    ["5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))", 12240],
    ["((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2", 13632],
]

for test in tests:
    line, answer = test[0], test[1]
    print(f"Test {line}, Answer {answer}")
    assert operate_ltr(line) == answer

# part 1
with open("day-18-puzzle.txt") as f:
    sum = 0
    for line in f:
        line = line.rstrip()
        sum += operate_ltr(line)
    print(f"Part 1: {sum}")
    print()

# test infix to prefix
assert infix_to_prefix("1 + 2 + 3") == "+ 1 + 2 3"
assert infix_to_prefix("1 * 2 + 3") == "* 1 + 2 3"
assert infix_to_prefix("(1 * 2) + 3") == "+ * 1 2 3"

# tests
print("Running tests")
tests = [
    ["1 + (2 * 3) + (4 * (5 + 6))", 51],
    ["2 * 3 + (4 * 5)", 46],
    ["5 + (8 * 3 + 9 + 3 * 4 * 3)", 1445],
    ["5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))", 669060],
    ["((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2", 23340],
]

for test in tests:
    line, answer = test[0], test[1]
    print(f"Test {line}, Answer {answer}")
    assert prefix_compute(infix_to_prefix(line)) == answer

# part 2
# convert from infix to prefix or postfix
with open("day-18-puzzle.txt") as f:
    sum = 0
    for line in f:
        line = line.rstrip()
        sum += prefix_compute(infix_to_prefix(line))
    print(f"Part 2: {sum}")
