"""
Write a function, which takes a non-negative integer (seconds) as input and returns the time in a human-readable format (HH:MM:SS)

HH = hours, padded to 2 digits, range: 00 - 99
MM = minutes, padded to 2 digits, range: 00 - 59
SS = seconds, padded to 2 digits, range: 00 - 59
The maximum time never exceeds 359999 (99:59:59)

You can find some examples in the test fixtures.
"""

# Solution for more ambitious people I wounder if you find small mistake in logic that I have put in here
import copy


def make_readable(seconds):
    if seconds < 60:
        return f"00:00:{seconds if len(str(seconds)) > 1 else '0' + f'{seconds}'}"
    hours = 0
    minutes = 0
    time = copy.copy(seconds)

    while time > 0:
        time -= 60
        minutes += 1
        if time - 60 <= 0:
            minutes += 1
            break
        elif minutes == 60:
            hours += 1
            minutes = 0

    hour = f"{hours if len(str(hours)) > 1 else '0' + f'{hours}'}"
    minute = f"{minutes if len(str(minutes)) > 1 else '0' + f'{minutes}'}"
    second = f"{seconds % 60 if seconds % 60 > 9 else '0' + f'{seconds % 60}'}"

    return ':'.join([hour, minute, second])


# Resl solution
def make_readable(seconds):
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    return f"{hours:02}:{minutes:02}:{seconds % 60:02}"

print(make_readable(86399))
