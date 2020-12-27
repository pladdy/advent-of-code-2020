# How many passwords are valid?
#  parse password: x-y (min-max) letter: password


def _parse_entry(entry):
    counts, letter, password = entry.split(" ")
    min, max = counts.split("-")
    letter = letter.strip(":")
    return int(min), int(max), letter, password


def valid_sled_password(entry):
    min, max, letter, password = _parse_entry(entry)
    letter_count = password.count(letter)
    if letter_count >= min and letter_count <= max:
        return True
    return False


def valid_password(entry):
    x, y, letter, password = _parse_entry(entry)

    letter_count = 0
    if password[x - 1] == letter:
        letter_count += 1
    if password[y - 1] == letter:
        letter_count += 1

    if letter_count == 1:
        return True
    return False


valid_passwords = 0

passwords = []
with open("day-2-puzzle.txt") as f:
    passwords = f.readlines()

for password in passwords:
    if valid_sled_password(password):
        valid_passwords += 1

print("Valid Sled Passwords: {}".format(valid_passwords))

valid_passwords = 0

for password in passwords:
    if valid_password(password):
        valid_passwords += 1

print("Valid Passwords: {}".format(valid_passwords))
