import re


def count_matches(messages, pattern):
    matches = 0
    for message in messages:
        if re.match(pattern, message):
            matches += 1
    return matches


def parse_puzzle(lines):
    """Parse lines of a puzzle text into rules and messages."""
    rules = {}
    messages = []

    parsing_rules = True
    parsing_messages = False

    for line in lines:
        line = line.strip()
        if line == "":
            if len(rules) > 0:
                parsing_rules = False
                parsing_messages = True
            continue

        if parsing_rules:
            index, value = line.split(":")
            rules[index] = value.strip().replace('"', "")
        if parsing_messages:
            messages.append(line)

    return rules, messages


def part2_rules(rules):
    rules["8"] = "42+"
    rules[
        "11"
    ] = "42 31 | (42 42 31 31) | (42 42 42 31 31 31) | (42 42 42 42 31 31 31 31)"  # noqa
    return rules


def rule_to_pattern(rule, rules):
    """Return a rule from a rule list into a pattern."""
    pattern = rule

    subrules = rule.split()
    while re.search(r"\d", pattern):
        for subrule in set(subrules):
            # scrub subrule so we can find the right rule key
            for token in ["(", ")", "+", "*"]:
                subrule = subrule.replace(token, "")

            if subrule in "ab|+*":
                continue

            defn = rules.get(subrule)

            if "|" in defn:
                pattern = re.sub(rf"\b{subrule}\b", "(" + defn + ")", pattern)
            else:
                pattern = re.sub(rf"\b{subrule}\b", defn, pattern)

        subrules = pattern.split()

    return f"^{pattern.replace(' ', '')}$"


test = """
0: 4 1 5
1: 2 3 | 3 2
2: 4 4 | 5 5
3: 4 5 | 5 4
4: "a"
5: "b"

ababbb
bababa
abbbab
aaabbb
aaaabbb
"""

# Notes on test case
"""
0: 4 1 5
1: 2 3 | 3 2
2: 4 4 | 5 5
3: 4 5 | 5 4
4: "a"
5: "b"

ababbb
bababa  # no match: starts with b
abbbab
aaabbb  # no match: if tokens 2 and 3 are aa, tokens 3 and 4 must be a/b or b/a
aaaabbb # no match: too long

0: 4 1 5
0: a (2 3 | 3 2) b
0: a ((4 4 | 5 5) (4 5 | 5 4) | (4 5 | 5 4) | (4 4 | 5 5)) b
0: a ((a a | b b) (a b | b a) | (a b | b a) | (a a | b b)) b

observations:
- based on rule parsing, length has to be 6
- has to start and end in b
- after checking first and last tokens, only need to check middle 4 tokens
"""

# Implementation notes
# - what if i convert the subrules into a big regex?
"""
0: 4 1 5
0: a (2 3 | 3 2) b
0: a ((4 4 | 5 5) (4 5 | 5 4) | (4 5 | 5 4) (4 4 | 5 5)) b
- convert to letters and no rule reference
0: a ((a a | b b) (a b | b a) | (a b | b a) (a a | b b)) b
- remove spaces and add boundaries
0: ^a((aa|bb)(ab|ba)|(ab|ba)(aa|bb))b$

Seems to work: https://regex101.com/r/YSeKkw/1
"""
rules, messages = parse_puzzle(test.split("\n"))
pattern = rule_to_pattern(rules["0"], rules)
matches = count_matches(messages, pattern)

print(f"Part 1 test matches {matches}")
assert matches == 2
print("Part 1 test case passes.")

# part 1
with open("day-19-puzzle.txt") as f:
    rules, messages = parse_puzzle(f.readlines())
pattern = rule_to_pattern(rules["0"], rules)
matches = count_matches(messages, pattern)
print(f"Part 1: {matches}")

# part 2
#
# Replace rules 8: 42 and 11: 42 31 with the following:
# 8: 42 | 42 8
#    42 | 42 42 | 42 8
#    Below is wrong.  According to two sources I checked:
#   - https://github.com/mariothedog/Advent-of-Code-2020/blob/main/Day%2019/day_19.py#L53 # noqa
#   - https://dev.to/rpalo/advent-of-code-2020-solution-megathread-day-19-monster-messages-58ep # noqa
#   Rule 8 transltes to X | XX | XXX | XXXX which is 42+ in regex...how?
#   42 | 42 42 | 42 42 | 42 42 | 42 8, etc.
# 11: 42 31 | 42 11 31
#     42 31 | 42 42 31 | 42 11 31 31
#     Same issue as above, I somehow cannot see how this recursion works.  What
#     should happen is you get 42 31 | 42 42 31 31 | 42 42 42 31 31 31, etc.
#     How?  Why am I dummmmmbbbbbb?
#     42 31 | 42 42 31 | 42 42 31 | 42 42 31 | 42 11 31 31 31 31
#
# Rule 0 is still 8 11
#
# 42: 131 52 | 61 72
# 31: 52 14 | 72 12
# note: 72 is b, 52 is a

test = """
42: 9 14 | 10 1
9: 14 27 | 1 26
10: 23 14 | 28 1
1: "a"
11: 42 31
5: 1 14 | 15 1
19: 14 1 | 14 14
12: 24 14 | 19 1
16: 15 1 | 14 14
31: 14 17 | 1 13
6: 14 14 | 1 14
2: 1 24 | 14 4
0: 8 11
13: 14 3 | 1 12
15: 1 | 14
17: 14 2 | 1 7
23: 25 1 | 22 14
28: 16 1
4: 1 1
20: 14 14 | 1 15
3: 5 14 | 16 1
27: 1 6 | 14 18
14: "b"
21: 14 1 | 1 14
25: 1 1 | 1 14
22: 14 14
8: 42
26: 14 22 | 1 20
18: 15 15
7: 14 5 | 1 21
24: 14 1

abbbbbabbbaaaababbaabbbbabababbbabbbbbbabaaaa
bbabbbbaabaabba
babbbbaabbbbbabbbbbbaabaaabaaa
aaabbbbbbaaaabaababaabababbabaaabbababababaaa
bbbbbbbaaaabbbbaaabbabaaa
bbbababbbbaaaaaaaabbababaaababaabab
ababaaaaaabaaab
ababaaaaabbbaba
baabbaaaabbaaaababbaababb
abbbbabbbbaaaababbbbbbaaaababb
aaaaabbaabaaaaababaa
aaaabbaaaabbaaa
aaaabbaabbaaaaaaabbbabbbaaabbaabaaa
babaaabbbaaabaababbaabababaaab
aabbbbbaabbbaaaaaabbbbbababaaaaabbaaabba
"""

rules, messages = parse_puzzle(test.split("\n"))
rules = part2_rules(rules)
pattern = rule_to_pattern(rules["0"], rules)
matches = count_matches(messages, pattern)

print(f"Part 2 test: {matches}")
assert matches == 12
print("Part 2 test case passes.")

with open("day-19-puzzle.txt") as f:
    rules, messages = parse_puzzle(f.readlines())
rules = part2_rules(rules)
pattern = rule_to_pattern(rules["0"], rules)
matches = count_matches(messages, pattern)
print(f"Part 2: {matches}")
