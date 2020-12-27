import re


def append_to_passports(passport, all, valid):
    if valid_passport(current_passport):
        valid.append(current_passport)
    all.append(current_passport)


def valid_passport(passport):
    valid = True
    if "byr" not in passport:
        valid = False
    if "iyr" not in passport:
        valid = False
    if "eyr" not in passport:
        valid = False
    if "hgt" not in passport:
        valid = False
    if "hcl" not in passport:
        valid = False
    if "ecl" not in passport:
        valid = False
    if "pid" not in passport:
        valid = False
    return valid


# part 1

passports = []
valid_passports = []
raw_text = ""
current_passport = {}

with open("day-4-puzzle.txt") as f:
    for line in f:
        line = line.rstrip()

        if line == "":
            append_to_passports(current_passport, passports, valid_passports)
            raw_text = line
            current_passport = {}
            continue

        for chunk in line.split(" "):
            k, v = chunk.split(":")
            current_passport[k] = v

append_to_passports(current_passport, passports, valid_passports)
print("Valid Passports: {}".format(len(valid_passports)))

# part 2

passports = []
valid_passports = []
raw_text = ""
current_passport = {}


def append_strict_passports(passport, all, valid):
    if strict_passport(current_passport):
        valid.append(current_passport)
    all.append(current_passport)


def strict_passport(passport):
    return (
        valid_passport(passport)
        and valid_byr(passport)
        and valid_ecl(passport)
        and valid_eyr(passport)
        and valid_hcl(passport)
        and valid_hgt(passport)
        and valid_iyr(passport)
        and valid_pid(passport)
    )


def valid_byr(passport):
    v = passport.get("byr", 0)
    return int(v) >= 1920 and int(v) <= 2002


def valid_ecl(passport):
    v = passport.get("ecl")
    return v in ("amb", "blu", "brn", "gry", "grn", "hzl", "oth")


def valid_eyr(passport):
    v = passport.get("eyr", 0)
    return int(v) >= 2020 and int(v) <= 2030


def valid_hcl(passport):
    v = passport.get("hcl", "")
    p = re.compile("^#[0-9a-f]{6}$")

    if p.match(v):
        return True
    return False


def valid_hgt(passport):
    v = passport.get("hgt", "")

    if v.endswith("cm"):
        v = v.rstrip("cm")
        return int(v) >= 150 and int(v) <= 193

    if v.endswith("in"):
        v = v.rstrip("in")
        return int(v) >= 59 and int(v) <= 76

    return False


def valid_iyr(passport):
    v = passport.get("iyr", 0)
    return int(v) >= 2010 and int(v) <= 2020


def valid_pid(passport):
    v = passport.get("pid", "")
    p = re.compile("^[0-9]{9}$")

    if p.match(v):
        return True
    return False


with open("day-4-puzzle.txt") as f:
    for line in f:
        line = line.rstrip()

        if line == "":
            append_strict_passports(current_passport, passports, valid_passports)
            raw_text = line
            current_passport = {}
            continue

        for chunk in line.split(" "):
            k, v = chunk.split(":")
            current_passport[k] = v

append_strict_passports(current_passport, passports, valid_passports)
print("Strict Passports: {}".format(len(valid_passports)))
