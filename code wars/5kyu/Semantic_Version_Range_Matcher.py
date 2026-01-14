"""
Semantic Version Range Matcher

Every package manager uses semantic versioning, but have you ever implemented the range matching yourself?

Given a version string and a range constraint, determine if the version satisfies the constraint.

Version format: MAJOR.MINOR.PATCH (e.g., 1.2.3)

Supported range syntax:

Syntax	Meaning	Example
Exact	Matches exactly	1.2.3
> >= < <=	Comparisons	>=1.2.0
^ (caret)	Compatible - allows changes that don't modify the left-most non-zero digit	^1.2.3 means >=1.2.3 <2.0.0
~ (tilde)	Allows patch-level changes	~1.2.3 means >=1.2.3 <1.3.0
Space	AND (both must match)	>=1.0.0 <2.0.0
||	OR (either can match)	^1.0.0 || ^2.0.0
Caret ^ edge cases:

^0.2.3 → >=0.2.3 <0.3.0 (minor is left-most non-zero)
^0.0.3 → >=0.0.3 <0.0.4 (patch is left-most non-zero)
satisfies("1.2.3", "1.2.3")        # True - exact match
satisfies("1.2.4", ">=1.2.0")      # True
satisfies("2.0.0", "^1.2.3")       # False - caret locks major
satisfies("1.9.9", "^1.2.3")       # True
satisfies("1.2.5", "~1.2.3")       # True - patch can change
satisfies("1.3.0", "~1.2.3")       # False - minor can't change
satisfies("1.5.0", ">=1.0.0 <2.0.0")  # True - AND
satisfies("3.0.0", "^1.0.0 || ^3.0.0") # True - OR
satisfies("1.5.0", ">=1.0.0 <2.0.0 || ^3.0.0")  # True - matches first group
satisfies("3.5.0", ">=1.0.0 <2.0.0 || ^3.0.0")  # True - matches second group
satisfies("2.5.0", ">=1.0.0 <2.0.0 || ^3.0.0")  # False - matches neither
Precedence: AND (space) binds tighter than OR (||).

>=1.0.0 <2.0.0 || ^3.0.0 means (>=1.0.0 AND <2.0.0) OR (^3.0.0)
Notes:

All versions are valid semver with exactly 3 numeric parts
No pre-release tags or build metadata
Ranges are always valid syntax
Whitespace around || and comparators is flexible


prodigysml
https://www.codewars.com/kata/695735855167b52333139d89/train/python
"""


def parse_version(v):
    return tuple(map(int, v.split(".")))


def cmp(v1, v2):
    return (v1 > v2) - (v1 < v2)


def satisfies_simple(version, expr):
    v = parse_version(version)

    if expr.startswith(">="):
        return v >= parse_version(expr[2:])
    if expr.startswith("<="):
        return v <= parse_version(expr[2:])
    if expr.startswith(">"):
        return v > parse_version(expr[1:])
    if expr.startswith("<"):
        return v < parse_version(expr[1:])
    if expr.startswith("^"):
        base = parse_version(expr[1:])
        major, minor, patch = base

        if major != 0:
            upper = (major + 1, 0, 0)
        elif minor != 0:
            upper = (0, minor + 1, 0)
        else:
            upper = (0, 0, patch + 1)

        return base <= v < upper

    if expr.startswith("~"):
        major, minor, patch = parse_version(expr[1:])
        lower = (major, minor, patch)
        upper = (major, minor + 1, 0)
        return lower <= v < upper

    return v == parse_version(expr)


def satisfies(version, range_str):
    or_groups = [g.strip() for g in range_str.split("||")]

    for group in or_groups:
        parts = group.split()
        if all(satisfies_simple(version, part) for part in parts):
            return True

    return False
