#########################################################################################################
##################################            1             #############################################
#########################################################################################################

"""Once upon a time, on a way through the old wild mountainous west,…
… a man was given directions to go from one point to another. The directions were "NORTH", "SOUTH", "WEST", "EAST". Clearly "NORTH" and "SOUTH" are opposite, "WEST" and "EAST" too.

Going to one direction and coming back the opposite direction right away is a needless effort. Since this is the wild west, with dreadful weather and not much water, it's important to save yourself some energy, otherwise you might die of thirst!

How I crossed a mountainous desert the smart way.
The directions given to the man are, for example, the following (depending on the language):

["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"].
or
{ "NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST" };
or
[North, South, South, East, West, North, West]
You can immediately see that going "NORTH" and immediately "SOUTH" is not reasonable, better stay to the same place! So the task is to give to the man a simplified version of the plan. A better plan in this case is simply:

["WEST"]
or
{ "WEST" }
or
[West]
Other examples:
In ["NORTH", "SOUTH", "EAST", "WEST"], the direction "NORTH" + "SOUTH" is going north and coming back right away.

The path becomes ["EAST", "WEST"], now "EAST" and "WEST" annihilate each other, therefore, the final result is [] (nil in Clojure).

In ["NORTH", "EAST", "WEST", "SOUTH", "WEST", "WEST"], "NORTH" and "SOUTH" are not directly opposite but they become directly opposite after the reduction of "EAST" and "WEST" so the whole path is reducible to ["WEST", "WEST"].

Task
Write a function dirReduc which will take an array of strings and returns an array of strings with the needless directions removed (W<->E or S<->N side by side).

The Haskell version takes a list of directions with data Direction = North | East | West | South.
The Clojure version returns nil when the path is reduced to nothing.
The Rust version takes a slice of enum Direction {North, East, West, South}.
See more examples in "Sample Tests:"
Notes
Not all paths can be made simpler. The path ["NORTH", "WEST", "SOUTH", "EAST"] is not reducible. "NORTH" and "WEST", "WEST" and "SOUTH", "SOUTH" and "EAST" are not directly opposite of each other and can't become such. Hence the result path is itself : ["NORTH", "WEST", "SOUTH", "EAST"].
if you want to translate, please ask before translating."""


def dir_reduc(arr):
    opposites = {'NORTH': 'SOUTH', 'SOUTH': 'NORTH', 'WEST': 'EAST', 'EAST': 'WEST'}
    stack = []

    for direction in arr:
        if stack and opposites[direction] == stack[-1]:
            stack.pop()
        else:
            stack.append(direction)

    return stack


#########################################################################################################
##################################            2             #############################################
#########################################################################################################

"""You have an award-winning garden and every day the plants need exactly 40mm of water. You created a great
piece of JavaScript to calculate the amount of water your plants will need when you have taken into consideration the
amount of rain water that is forecast for the day. Your jealous neighbour hacked your computer and filled your code with bugs.
Your task is to debug the code before your plants die!"""

# original code for debugging
def rain_amount(mm):
    if rain_amount == 40:
         return "You need to give your plant " + {rain_amount - 40} + " mm of water"
    else:
         return "Your plant has had more than enough water for today!"

#solution
def rain_amount(mm):
    if mm < 40:
         return f"You need to give your plant {40 - mm}mm of water"
    else:
         return "Your plant has had more than enough water for today!"


#########################################################################################################
##################################            3             #############################################
#########################################################################################################

"""Description:
Replace all vowel to exclamation mark in the sentence. aeiouAEIOU is vowel.

Examples
replace("Hi!") === "H!!"
replace("!Hi! Hi!") === "!H!! H!!"
replace("aeiou") === "!!!!!"
replace("ABCDE") === "!BCD!"""

def replace_exclamation(st):
    vowels = 'aeiouAEIOU'
    result = ''
    for char in st:
        if char in vowels:
            result += '!'
        else:
            result += char
    return result



#########################################################################################################
##################################            4             #############################################
#########################################################################################################

"""Given three integers a, b, and c, return the largest number obtained after inserting the operators +, *, and parentheses (). In other words, try every combination of a, b, and c with the operators, without reordering the operands, and return the maximum value.

Example
With the numbers 1, 2, and 3, here are some possible expressions:

1 * (2 + 3) = 5
1 * 2 * 3 = 6
1 + 2 * 3 = 7
(1 + 2) * 3 = 9
The maximum value that can be obtained is 9.

Notes
The numbers are always positive, in the range 1 ≤ a, b, c ≤ 10.
You can use the same operation more than once.
It is not necessary to use all the operators or parentheses.
You cannot swap the operands. For example, with the given numbers, you cannot get the expression (1 + 3) * 2 = 8.
Input and Output Examples
expressionsMatter(1, 2, 3) ==> 9, because (1 + 2) * 3 = 9.
expressionsMatter(1, 1, 1) ==> 3, because 1 + 1 + 1 = 3.
expressionsMatter(9, 1, 1) ==> 18, because 9 * (1 + 1) = 18."""

def expressions_matter(a, b, c):
    return max(
        a + b + c,
        a * b * c,
        a + b * c,
        (a + b) * c,
        a * (b + c),
        (a * b) + c
    )


#########################################################################################################
##################################            5             #############################################
#########################################################################################################


"""The goal of this exercise is to convert a string to a new string where each character in the new string is "(" if that character appears only once in the original string, or ")" if that character appears more than once in the original string. Ignore capitalization when determining if a character is a duplicate.

Examples
"din"      =>  "((("
"recede"   =>  "()()()"
"Success"  =>  ")())())"
"(( @"     =>  "))((" 
Notes
Assertion messages may be unclear about what they display in some languages. If you read "...It Should encode XXX", the "XXX" is the expected result, not the input!

"""

def duplicate_encode(word):
    word = word.lower()
    result = ""
    for char in word:
        if word.count(char) > 1:
            result += ')'
        else:
            result += '('
    return result



#########################################################################################################
##################################            6             #############################################
#########################################################################################################

"""What if we need the length of the words separated by a space to be added at the end of that same word and have it returned as an array?

Example(Input --> Output)

"apple ban" --> ["apple 5", "ban 3"]
"you will win" -->["you 3", "will 4", "win 3"]
Your task is to write a function that takes a String and returns an Array/list with the length of each word added to each element .

Note: String will have at least one element; words will always be separated by a space.
"""


def add_length(str_):
    sentence = str_.split(' ')
    result = []

    for word in sentence:
        length = len(word)
        with_length = f'{word} {length}'
        result.append(with_length)

    return result


#########################################################################################################
##################################            7             #############################################
#########################################################################################################

"""Issue
Looks like some hoodlum plumber and his brother has been running around and damaging your stages again.

The pipes connecting your level's stages together need to be fixed before you receive any more complaints.

The pipes are correct when each pipe after the first is 1 more than the previous one.

Task
Given a list of unique numbers sorted in ascending order, return a new list so that the values increment by 1 for each index from the minimum value up to the maximum value (both included).

Example
Input:  1,3,5,6,7,8 Output: 1,2,3,4,5,6,7,8

"""

def pipe_fix(nums):
    return list(range(nums[0], nums[-1] + 1))




