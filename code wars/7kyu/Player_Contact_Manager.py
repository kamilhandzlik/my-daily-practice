"""
Player Contact Manager

You are the Dungeon Master for a public DnD game at your local comic shop and recently you've had some trouble keeping your players' info neat and organized so you've decided to write a bit of code to help keep them sorted!

The goal of this code is to create an array of objects that stores a player's name and contact number from a given string.

The method should return an empty array if the argument passed is an empty string or nil/None/null.

Examples
player_manager("John Doe, 8167238327, Jane Doe, 8163723827") returns [{"player": "John Doe", "contact": 8167238327}, {"player": "Jane Doe", "contact": 8163723827}]
player_manager(None) returns []
player_manager("")   returns []
playerManager("John Doe, 8167238327, Jane Doe, 8163723827") returns [{player: "John Doe", contact: 8167238327}, {player: "Jane Doe", contact: 8163723827}]
playerManager(null) returns []
playerManager("")   returns []
Have at thee!

made by IanEarley
https://www.codewars.com/kata/5b203de891c7469b520000b4/train/python
"""


# Solution 1
def player_manager(players):
    if not players:
        return []

    result = []
    sp = players.split(', ')

    for i, j in enumerate(sp):
        if j.replace(" ", "").isalpha():
            result.append({"player": j, "contact": int(sp[i + 1])})

    return result


# Solution 2
def player_manager(players):
    if not players:
        return []

    sp = players.split(', ')
    return [{"player": j, "contact": int(sp[i + 1])} for i, j in enumerate(sp) if j.replace(" ", "").isalpha()]


print(player_manager("John Doe, 8167238327, Jane Doe, 8163723827"))
