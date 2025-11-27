"""
Return the day

Complete the function which returns the weekday according to the input number:

1 returns "Sunday"
2 returns "Monday"
3 returns "Tuesday"
4 returns "Wednesday"
5 returns "Thursday"
6 returns "Friday"
7 returns "Saturday"
Otherwise returns "Wrong, please enter a number between 1 and 7"

"""

# Solution 1
def whatday(num):
    week = {1: "Sunday", 2: "Monday", 3: "Tuesday", 4: "Wednesday", 5: "Thursday", 6: "Friday", 7: "Saturday"}

    return week[num] if num in week else "Wrong, please enter a number between 1 and 7"


# Solution 2
def whatday(num):
    days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
    if 1 <= num <= 7:
        return days[num - 1]
    return "Wrong, please enter a number between 1 and 7"
