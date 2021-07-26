def append(k, memory, v):
    if k in memory:
        memory[k].append(v)
    else:
        memory[k] = [v]
    return memory


def create_memory(puzzle):
    memory = {}
    turn = 1
    for n in puzzle:
        memory = append(n, memory, turn)
        turn += 1
    return memory


def run_puzzle(puzzle, turns):
    puzzle_size = len(puzzle)
    say = puzzle[0]
    memory = create_memory(puzzle)
    turn = puzzle_size

    while turn < turns:
        turn += 1
        last_said = say

        if len(memory.get(last_said, [])) == 1:
            say = 0
        else:
            say = memory[last_said][-1] - memory[last_said][-2]
        memory = append(say, memory, turn)
        # print(f"turn: {turn}, say: {say}, last_said: {last_said}")

    return say


def run_tests(tests):
    for test in tests:
        puzzle, answer = test.get("puzzle"), test.get("answer")
        result = run_puzzle(puzzle, turns)
        print(f"  {result}")
        assert result == answer


# Part 1
tests = [
    {"puzzle": [0, 3, 6], "answer": 436},
    {"puzzle": [1, 3, 2], "answer": 1},
    {"puzzle": [2, 1, 3], "answer": 10},
    {"puzzle": [1, 2, 3], "answer": 27},
    {"puzzle": [2, 3, 1], "answer": 78},
    {"puzzle": [3, 2, 1], "answer": 438},
    {"puzzle": [3, 1, 2], "answer": 1836},
]

turns = 2020

print("Part 1:")
run_tests(tests)
print(f"  {run_puzzle([1, 17, 0, 10, 18, 11, 6], turns)}")

# Part 2
tests = [
    {"puzzle": [0, 3, 6], "answer": 175594},
    {"puzzle": [1, 3, 2], "answer": 2578},
    {"puzzle": [2, 1, 3], "answer": 3544142},
    {"puzzle": [1, 2, 3], "answer": 261214},
    {"puzzle": [2, 3, 1], "answer": 6895259},
    {"puzzle": [3, 2, 1], "answer": 18},
    {"puzzle": [3, 1, 2], "answer": 362},
]

turns = 30000000

print("Part 2:")
run_tests(tests)
print(f"  {run_puzzle([1, 17, 0, 10, 18, 11, 6], turns)}")
