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
import math


def dir_reduc(arr):
    opposites = {"NORTH": "SOUTH", "SOUTH": "NORTH", "WEST": "EAST", "EAST": "WEST"}
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


# solution
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
    vowels = "aeiouAEIOU"
    result = ""
    for char in st:
        if char in vowels:
            result += "!"
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
    return max(a + b + c, a * b * c, a + b * c, (a + b) * c, a * (b + c), (a * b) + c)


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
            result += ")"
        else:
            result += "("
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
    sentence = str_.split(" ")
    result = []

    for word in sentence:
        length = len(word)
        with_length = f"{word} {length}"
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


#########################################################################################################
##################################            8             #############################################
#########################################################################################################

"""Challenge:

Given a two-dimensional array of integers, return the flattened version of the array with all the integers in the sorted (ascending) order.

Example:

Given [[3, 2, 1], [4, 6, 5], [], [9, 7, 8]], your function should return [1, 2, 3, 4, 5, 6, 7, 8, 9]."""


def flatten_and_sort(array):
    flattened = [item for sublist in array for item in sublist]

    sorted_list = sorted(flattened)

    return sorted_list


#########################################################################################################
##################################            9             #############################################
#########################################################################################################

"""This kata is about multiplying a given number by eight if it is an even number and by nine otherwise."""


# Rozwiązanie 1
def simple_multiplication(number):
    if number % 2 != 0:
        return number * 9
    else:
        return number * 8


# Rozwiązanie 2


def simple_multiplication(number):
    return number * 9 if number % 2 != 0 else number * 8


#########################################################################################################
##################################            10            #############################################
#########################################################################################################

"""Now you have to write a function that takes an argument and returns the square of it."""
"""I have found this magnificent picture and I have to post it here
    
    ⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿⠛⠛⠛⠋⠉⠈⠉⠉⠉⠉⠛⠻⢿⣿⣿⣿⣿⣿⣿⣿
    ⣿⣿⣿⣿⣿⡿⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠛⢿⣿⣿⣿⣿
    ⣿⣿⣿⣿⡏⣀⠀⠀⠀⠀⠀⠀⠀⣀⣤⣤⣤⣄⡀⠀⠀⠀⠀⠀⠀⠀⠙⢿⣿⣿
    ⣿⣿⣿⢏⣴⣿⣷⠀⠀⠀⠀⠀⢾⣿⣿⣿⣿⣿⣿⡆⠀⠀⠀⠀⠀⠀⠀⠈⣿⣿
    ⣿⣿⣟⣾⣿⡟⠁⠀⠀⠀⠀⠀⢀⣾⣿⣿⣿⣿⣿⣷⢢⠀⠀⠀⠀⠀⠀⠀⢸⣿
    ⣿⣿⣿⣿⣟⠀⡴⠄⠀⠀⠀⠀⠀⠀⠙⠻⣿⣿⣿⣿⣷⣄⠀⠀⠀⠀⠀⠀⠀⣿
    ⣿⣿⣿⠟⠻⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠶⢴⣿⣿⣿⣿⣿⣧⠀⠀⠀⠀⠀⠀⣿
    ⣿⣁⡀⠀⠀⢰⢠⣦⠀⠀⠀⠀⠀⠀⠀⠀⢀⣼⣿⣿⣿⣿⣿⡄⠀⣴⣶⣿⡄⣿
    ⣿⡋⠀⠀⠀⠎⢸⣿⡆⠀⠀⠀⠀⠀⠀⣴⣿⣿⣿⣿⣿⣿⣿⠗⢘⣿⣟⠛⠿⣼
    ⣿⣿⠋⢀⡌⢰⣿⡿⢿⡀⠀⠀⠀⠀⠀⠙⠿⣿⣿⣿⣿⣿⡇⠀⢸⣿⣿⣧⢀⣼
    ⣿⣿⣷⢻⠄⠘⠛⠋⠛⠃⠀⠀⠀⠀⠀⢿⣧⠈⠉⠙⠛⠋⠀⠀⠀⣿⣿⣿⣿⣿
    ⣿⣿⣧⠀⠈⢸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠟⠀⠀⠀⠀⢀⢃⠀⠀⢸⣿⣿⣿⣿
    ⣿⣿⡿⠀⠴⢗⣠⣤⣴⡶⠶⠖⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⡸⠀⣿⣿⣿⣿
    ⣿⣿⣿⡀⢠⣾⣿⠏⠀⠠⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠛⠉⠀⣿⣿⣿⣿
    ⣿⣿⣿⣧⠈⢹⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⣿⣿⣿⣿
    ⣿⣿⣿⣿⡄⠈⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣴⣾⣿⣿⣿⣿⣿
    ⣿⣿⣿⣿⣧⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿
    ⣿⣿⣿⣿⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
    ⣿⣿⣿⣿⣿⣦⣄⣀⣀⣀⣀⠀⠀⠀⠀⠘⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
    ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡄⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
    ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⠀⠀⠀⠙⣿⣿⡟⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿
    ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠇⠀⠁⠀⠀⠹⣿⠃⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿
    ⣿⣿⣿⣿⣿⣿⣿⣿⡿⠛⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⢐⣿⣿⣿⣿⣿⣿⣿⣿⣿
    ⣿⣿⣿⣿⠿⠛⠉⠉⠁⠀⢻⣿⡇⠀⠀⠀⠀⠀⠀⢀⠈⣿⣿⡿⠉⠛⠛⠛⠉⠉
    ⣿⡿⠋⠁⠀⠀⢀⣀⣠⡴⣸⣿⣇⡄⠀⠀⠀⠀⢀⡿⠄⠙⠛⠀⣀⣠⣤⣤⠄
    
    """


def square(n):
    return n ** 2


#########################################################################################################
##################################            11            #############################################
#########################################################################################################


"""A bookseller has lots of books classified in 26 categories labeled A, B, ... Z. Each book has a code c of 3, 4, 5 or more characters. The 1st character of a code is a capital letter which defines the book category.

In the bookseller's stocklist each code c is followed by a space and by a positive integer n (int n >= 0) which indicates the quantity of books of this code in stock.

For example an extract of a stocklist could be:

L = {"ABART 20", "CDXEF 50", "BKWRK 25", "BTSQZ 89", "DRTYM 60"}.
or
L = ["ABART 20", "CDXEF 50", "BKWRK 25", "BTSQZ 89", "DRTYM 60"] or ....
You will be given a stocklist (e.g. : L) and a list of categories in capital letters e.g :

M = {"A", "B", "C", "W"} 
or
M = ["A", "B", "C", "W"] or ...
and your task is to find all the books of L with codes belonging to each category of M and to sum their quantity according to each category.

For the lists L and M of example you have to return the string (in Haskell/Clojure/Racket/Prolog a list of pairs):

(A : 20) - (B : 114) - (C : 50) - (W : 0)
where A, B, C, W are the categories, 20 is the sum of the unique book of category A, 114 the sum corresponding to "BKWRK" and "BTSQZ", 50 corresponding to "CDXEF" and 0 to category 'W' since there are no code beginning with W.

If L or M are empty return string is "" (Clojure/Racket/Prolog should return an empty array/list instead).

Notes:
In the result codes and their values are in the same order as in M.
See "Samples Tests" for the return."""


def stock_list(list_of_art, list_of_cat):
    if not list_of_art or not list_of_cat:
        return ""

    category_sums = {cat: 0 for cat in list_of_cat}

    for book in list_of_art:
        code, quantity = book.split()
        category = code[0]
        quantity = int(quantity)

        if category in category_sums:
            category_sums[category] += quantity

    result = " - ".join(f"({cat} : {category_sums[cat]}" for cat in list_of_cat)
    return result


#########################################################################################################
##################################            12            #############################################
#########################################################################################################

"""Create a function that accepts a string and a single character, and returns an integer of the count of occurrences the 2nd argument is found in the first one.

If no occurrences can be found, a count of 0 should be returned.

("Hello", 'o')  =>  1
("Hello", 'l')  =>  2
("", 'z')       =>  0
Notes
The first argument can be an empty string
In languages with no distinct character data type, the second argument will be a string of length 1"""


def str_count(strng, letter):
    return strng.count(letter)


#########################################################################################################
##################################            13            #############################################
#########################################################################################################

"""The Story:
Bob is working as a bus driver. However, he has become extremely popular amongst the city's residents. With so many passengers wanting to get aboard his bus, he sometimes has to face the problem of not enough space left on the bus! He wants you to write a simple program telling him if he will be able to fit all the passengers.

Task Overview:
You have to write a function that accepts three parameters:

cap is the amount of people the bus can hold excluding the driver.
on is the number of people on the bus excluding the driver.
wait is the number of people waiting to get on to the bus excluding the driver.
If there is enough space, return 0, and if there isn't, return the number of passengers he can't take.

Usage Examples:
cap = 10, on = 5, wait = 5 --> 0 # He can fit all 5 passengers
cap = 100, on = 60, wait = 50 --> 10 # He can't fit 10 of the 50 waiting"""


# solution 1
def enough(cap, on, wait):
    if (wait + on) > cap:
        return (on + wait) - cap
    else:
        return 0


# Solution 2


def enough(cap, on, wait):
    return (on + wait) - cap if (wait + on) > cap else 0


# solution 3
def enough(cap, on, wait):
    return max(0, wait - (cap - on))


#########################################################################################################
##################################            14            #############################################
#########################################################################################################

"""Create a function finalGrade, which calculates the final grade of a student depending on two parameters: a grade for the exam and a number of completed projects.

This function should take two arguments: exam - grade for exam (from 0 to 100); projects - number of completed projects (from 0 and above);

This function should return a number (final grade). There are four types of final grades:

100, if a grade for the exam is more than 90 or if a number of completed projects more than 10.
90, if a grade for the exam is more than 75 and if a number of completed projects is minimum 5.
75, if a grade for the exam is more than 50 and if a number of completed projects is minimum 2.
0, in other cases
Examples(Inputs-->Output):

100, 12 --> 100
99, 0 --> 100
10, 15 --> 100

85, 5 --> 90

55, 3 --> 75

55, 0 --> 0
20, 2 --> 0
*Use Comparison and Logical Operators."""


def final_grade(exam, projects):
    if exam > 90 or projects > 10:
        return 100
    elif exam > 75 and projects >= 5:
        return 90
    elif exam > 50 and projects >= 2:
        return 75
    else:
        return 0


#########################################################################################################
##################################            15            #############################################
#########################################################################################################

"""This function should test if the factor is a factor of base.

Return true if it is a factor or false if it is not.

About factors
Factors are numbers you can multiply together to get another number.

2 and 3 are factors of 6 because: 2 * 3 = 6

You can find a factor by dividing numbers. If the remainder is 0 then the number is a factor.
You can use the mod operator (%) in most languages to check for a remainder
For example 2 is not a factor of 7 because: 7 % 2 = 1

Note: base is a non-negative number, factor is a positive number."""


def check_for_factor(base, factor):
    if factor <= 0:
        raise ValueError("Factor should be a positive number.")
    return base % factor == 0


#########################################################################################################
##################################            16            #############################################
#########################################################################################################
"""Find Mean
Find the mean (average) of a list of numbers in an array.

Information
To find the mean (average) of a set of numbers add all of the numbers together and divide by the number of values in the list.

For an example list of 1, 3, 5, 7

1. Add all of the numbers

1+3+5+7 = 16
2. Divide by the number of values in the list. In this example there are 4 numbers in the list.

16/4 = 4
3. The mean (or average) of this list is 4"""


def find_average(nums):
    if not nums:
        return 0
    return sum(nums) / len(nums)


#########################################################################################################
##################################            17            #############################################
#########################################################################################################

"""The number 
89
89 is the first integer with more than one digit that fulfills the property partially introduced in the title of this kata. What's the use of saying "Eureka"? Because this sum gives the same number: 
89
=
8
1
+
9
2
89=8 
1
 +9 
2
 

The next number in having this property is 
135
135:

See this property again: 
135
=
1
1
+
3
2
+
5
3
135=1 
1
 +3 
2
 +5 
3
 

Task
We need a function to collect these numbers, that may receive two integers 
a
a, 
b
b that defines the range 
[
a
,
b
]
[a,b] (inclusive) and outputs a list of the sorted numbers in the range that fulfills the property described above.

Examples
Let's see some cases (input -> output):

1, 10  --> [1, 2, 3, 4, 5, 6, 7, 8, 9]
1, 100 --> [1, 2, 3, 4, 5, 6, 7, 8, 9, 89]
If there are no numbers of this kind in the range 
[
a
,
b
]
[a,b] the function should output an empty list.

90, 100 --> []
Enjoy it!!"""


def sum_dig_pow(a, b):
    def is_eureka_number(n):
        digits = [int(d) for d in str(n)]
        return n == sum(digit ** (i + 1) for i, digit in enumerate(digits))

    return [n for n in range(a, b + 1) if is_eureka_number(n)]


#########################################################################################################
##################################            18            #############################################
#########################################################################################################


"""Take an array and remove every second element from the array. Always keep the first element and start removing with the next element.

Example:
["Keep", "Remove", "Keep", "Remove", "Keep", ...] --> ["Keep", "Keep", "Keep", ...]

None of the arrays will be empty, so you don't have to worry about that!"""


# solution 1
def remove_every_other(my_list):
    return my_list[::2]


# solution for fun
def remove_every_other(my_list):
    r = []
    for i in range(len(my_list)):
        if i % 2 == 0:
            r.append(my_list[i])
    return r


#########################################################################################################
##################################            19            #############################################
#########################################################################################################

"""The wide-mouth frog is particularly interested in the eating habits of other creatures.

He just can't stop asking the creatures he encounters what they like to eat. But, then he meets the alligator who just 
LOVES to eat wide-mouthed frogs!

When he meets the alligator, it then makes a tiny mouth.

Your goal in this kata is to create complete the mouth_size method this method takes one argument animal which corresponds 
to the animal encountered by the frog.
If this one is an alligator (case-insensitive) return small otherwise return wide."""


# solution 1


def mouth_size(animal):
    if animal.lower() == "alligator":
        return "small"
    else:
        return "wide"


# solution 2
def mouth_size(animal):
    return "small" if animal.lower() == "alligator" else "wide"


#########################################################################################################
##################################            20            #############################################
#########################################################################################################

"""You are given two arrays a1 and a2 of strings. Each string is composed with letters from a to z. Let x be any string in the first array and y be any string in the second array.

Find max(abs(length(x) − length(y)))

If a1 and/or a2 are empty return -1 in each language except in Haskell (F#) where you will return Nothing (None).

Example:
a1 = ["hoqq", "bbllkw", "oox", "ejjuyyy", "plmiis", "xxxzgpsssa", "xxwwkktt", "znnnnfqknaz", "qqquuhii", "dvvvwz"]
a2 = ["cccooommaaqqoxii", "gggqaffhhh", "tttoowwwmmww"]
mxdiflg(a1, a2) --> 13
Bash note:
input : 2 strings with substrings separated by ,
output: number as a string"""


def mxdiflg(a1, a2):
    if not a1 or not a2:  # If either array is empty
        return -1

    max_len_a1 = max(len(x) for x in a1)  # Maximum length in a1
    min_len_a1 = min(len(x) for x in a1)  # Minimum length in a1
    max_len_a2 = max(len(x) for x in a2)  # Maximum length in a2
    min_len_a2 = min(len(x) for x in a2)  # Minimum length in a2

    # Calculate the maximum of the absolute differences
    return max(abs(max_len_a1 - min_len_a2), abs(max_len_a2 - min_len_a1))


#########################################################################################################
##################################            21            #############################################
#########################################################################################################


"""Exclusive "or" (xor) Logical Operator
Overview
In some scripting languages like PHP, there exists a logical operator (e.g. &&, ||, and, or, etc.) called the "Exclusive Or" (hence the name of this Kata). The exclusive or evaluates two booleans. It then returns true if exactly one of the two expressions are true, false otherwise. For example:

false xor false == false // since both are false
true xor false == true // exactly one of the two expressions are true
false xor true == true // exactly one of the two expressions are true
true xor true == false // Both are true.  "xor" only returns true if EXACTLY one of the two expressions evaluate to true.
Task
Since we cannot define keywords in Javascript (well, at least I don't know how to do it), your task is to define a function xor(a, b) where a and b are the two expressions to be evaluated. Your xor function should have the behaviour described above, returning true if exactly one of the two expressions evaluate to true, false otherwise."""


def xor(a, b):
    return (a and not b) or (not a and b)


#########################################################################################################
##################################            22            #############################################
#########################################################################################################

"""Create a function that returns the name of the winner in a fight between two fighters.

Each fighter takes turns attacking the other and whoever kills the other first is victorious. Death is defined as having health <= 0.

Each fighter will be a Fighter object/instance. See the Fighter class below in your chosen language.

Both health and damagePerAttack (damage_per_attack for python) will be integers larger than 0. You can mutate the Fighter objects.

Your function also receives a third argument, a string, with the name of the fighter that attacks first.

Example:
  declare_winner(Fighter("Lew", 10, 2), Fighter("Harry", 5, 4), "Lew") => "Lew"
  
  Lew attacks Harry; Harry now has 3 health.
  Harry attacks Lew; Lew now has 6 health.
  Lew attacks Harry; Harry now has 1 health.
  Harry attacks Lew; Lew now has 2 health.
  Lew attacks Harry: Harry now has -1 health and is dead. Lew wins.
class Fighter(object):
    def __init__(self, name, health, damage_per_attack):
        self.name = name
        self.health = health
        self.damage_per_attack = damage_per_attack
        
    def __str__(self): return "Fighter({}, {}, {})".format(self.name, self.health, self.damage_per_attack)
    __repr__=__str__"""


class Fighter(object):
    def __init__(self, name, health, damage_per_attack):
        self.name = name
        self.health = health
        self.damage_per_attack = damage_per_attack

    def __str__(self):
        return "Fighter({}, {}, {})".format(
            self.name, self.health, self.damage_per_attack
        )

    __repr__ = __str__


# solution1
def declare_winner(fighter1, fighter2, first_attacker):
    attacker = fighter1 if fighter1.name == first_attacker else fighter2
    defender = fighter2 if attacker == fighter1 else fighter1

    while fighter1.health > 0 and fighter2.health > 0:
        defender.health -= attacker.damage_per_attack

        if defender.health <= 0:
            return attacker.name

        attacker, defender = defender, attacker

    return attacker.name


#########################################################################################################
##################################            23            #############################################
#########################################################################################################


"""Your boss decided to save money by purchasing some cut-rate optical character recognition software for scanning
 in the text of old novels to your database. At first it seems to capture words okay, but you quickly notice that it throws
  in a lot of numbers at random places in the text.

Examples (input -> output)
'! !'                 -> '! !'
'123456789'           -> ''
'This looks5 grea8t!' -> 'This looks great!'
Your harried co-workers are looking to you for a solution to take this garbled text and remove all of the numbers.
 Your program will take in a string and clean out all numeric characters, and return a string with spacing and special characters
  ~#$%^&!@*():;"'.,? all intact."""


# solution 1
def string_clean(s):
    cleared_string = ""

    for char in s:
        if char not in "0123456789":
            cleared_string += char

    return cleared_string


# solution 2
def string_clean(s):
    return "".join(x for x in s if not x.isdigit())


#########################################################################################################
##################################            24            #############################################
#########################################################################################################

"""Scenario
Several people are standing in a row divided into two teams.
The first person goes into team 1, the second goes into team 2, the third goes into team 1, and so on.

Task
Given an array of positive integers (the weights of the people), return a new array/tuple of two integers, where the first one is the total weight of team 1, and the second one is the total weight of team 2.

Notes
Array size is at least 1.
All numbers will be positive"""


def row_weights(array):
    team1 = 0
    team2 = 0

    for i, weight in enumerate(array):
        if i % 2 == 0:
            team1 += weight
        else:
            team2 += weight

    return (team1, team2)


#########################################################################################################
##################################            25            #############################################
#########################################################################################################

"""Your task, is to create N×N multiplication table, of size provided in parameter.

For example, when given size is 3:

1 2 3
2 4 6
3 6 9
For the given example, the return value should be:

[[1,2,3],[2,4,6],[3,6,9]]"""


def multiplication_table(size):
    result = []

    for i in range(1, size + 1):
        row = []
        for j in range(1, size + 1):
            row.append(i * j)
        result.append(row)

    return result


#########################################################################################################
##################################            25            #############################################
#########################################################################################################

"""Americans are odd people: in their buildings, the first floor is actually the ground floor and there is no 13th floor (due to superstition).

Write a function that given a floor in the american system returns the floor in the european system.

With the 1st floor being replaced by the ground floor and the 13th floor being removed, the numbers move down to take their place. In case of above 13, they move down by two because there are two omitted numbers below them.

Basements (negatives) stay the same as the universal level.

More information here

Examples
1  =>  0 
0  =>  0
5  =>  4
15  =>  13
-3  =>  -3"""


# first version i know crude but works
def get_real_floor(n):
    result = 0

    if n <= 0:
        result = n
    elif n <= 13:
        result = n - 1
    elif n > 13:
        result = n - 2

    return result


# second version
def get_real_floor(n):
    if n <= 0:
        return n
    elif n <= 13:
        return n - 1
    else:
        return n - 2


#########################################################################################################
##################################            26            #############################################
#########################################################################################################


"""Character recognition software is widely used to digitise printed texts. Thus the texts can be edited, searched and stored on a computer.

When documents (especially pretty old ones written with a typewriter), are digitised character recognition softwares often make mistakes.

Your task is correct the errors in the digitised text. You only have to handle the following mistakes:

S is misinterpreted as 5
O is misinterpreted as 0
I is misinterpreted as 1
The test cases contain numbers only by mistake.

"""


# solution 1
def correct(s):
    mistakes = {"5": "S", "0": "O", "1": "I"}

    for mistake, proper in mistakes.items():
        s = s.replace(mistake, proper)

    return s


# solution 2
def correct(string):
    return string.translate(str.maketrans("501", "SOI"))


#########################################################################################################
##################################            27            #############################################
#########################################################################################################


"""Write a function that accepts two integers and returns the remainder of dividing the larger value by the smaller value.

Division by zero should return an empty value.

Examples:
n = 17
m = 5
result = 2 (remainder of `17 / 5`)

n = 13
m = 72
result = 7 (remainder of `72 / 13`)

n = 0
m = -1
result = 0 (remainder of `0 / -1`)

n = 0
m = 1
result - division by zero (refer to the specifications on how to handle this in your language)
"""


# solution 1
def remainder(a, b):
    if min(a, b) == 0:
        return None
    elif a > b:
        return a % b
    else:
        return b % a

    # solution 2


def remainder(a, b):
    min_val = min(a, b)

    if min_val == 0:
        return None

    return max(a, b) % min(a, b)


#########################################################################################################
##################################            28            #############################################
#########################################################################################################

"""The Fibonacci numbers are the numbers in the following integer sequence (Fn):

0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, ...

such as

F(n) = F(n-1) + F(n-2) with F(0) = 0 and F(1) = 1.

Given a number, say prod (for product), we search two Fibonacci numbers F(n) and F(n+1) verifying

F(n) * F(n+1) = prod.

Your function productFib takes an integer (prod) and returns an array:

[F(n), F(n+1), true] or {F(n), F(n+1), 1} or (F(n), F(n+1), True)
depending on the language if F(n) * F(n+1) = prod.

If you don't find two consecutive F(n) verifying F(n) * F(n+1) = prodyou will return

[F(n), F(n+1), false] or {F(n), F(n+1), 0} or (F(n), F(n+1), False)
F(n) being the smallest one such as F(n) * F(n+1) > prod.

Some Examples of Return:
(depend on the language)

productFib(714) # should return (21, 34, true), 
                # since F(8) = 21, F(9) = 34 and 714 = 21 * 34

productFib(800) # should return (34, 55, false), 
                # since F(8) = 21, F(9) = 34, F(10) = 55 and 21 * 34 < 800 < 34 * 55
-----
productFib(714) # should return [21, 34, true], 
productFib(800) # should return [34, 55, false], 
-----
productFib(714) # should return {21, 34, 1}, 
productFib(800) # should return {34, 55, 0},        
-----
productFib(714) # should return {21, 34, true}, 
productFib(800) # should return {34, 55, false}, 
Note:
You can see examples for your language in "Sample Tests"."""


def product_fib(_prod):
    a, b = 0, 1

    while a * b < _prod:
        a, b = b, a + b

    return [a, b, a * b == _prod]


#########################################################################################################
##################################            29            #############################################
#########################################################################################################

"""Your task is to find the first element of an array that is not consecutive.

By not consecutive we mean not exactly 1 larger than the previous element of the array.

E.g. If we have an array [1,2,3,4,6,7,8] then 1 then 2 then 3 then 4 are all consecutive but 6 is not, so that's the first non-consecutive number.

If the whole array is consecutive then return null2.

The array will always have at least 2 elements1 and all elements will be numbers. The numbers will also all be unique and in ascending order. The numbers could be positive or negative and the first non-consecutive could be either too!

If you like this Kata, maybe try this one next: https://www.codewars.com/kata/represent-array-of-numbers-as-ranges

1 Can you write a solution that will return null2 for both [] and [ x ] though? (This is an empty array and one with a single number and is not tested for, but you can write your own example test. )

2
Swift, Ruby and Crystal: nil
Haskell: Nothing
Python, Rust, Scala: None
Julia: nothing
Nim: none(int) (See options)

"""


def first_non_consecutive(arr):
    if len(arr) < 2:
        return None

    for i in range(1, len(arr)):
        if arr[i] != arr[i - 1] + 1:
            return arr[i]

    return None


#########################################################################################################
##################################            30            #############################################
#########################################################################################################


"""Return a new array consisting of elements which are multiple of their own index in input array (length > 1).

Some cases:
[22, -6, 32, 82, 9, 25] =>  [-6, 32, 25]

[68, -1, 1, -7, 10, 10] => [-1, 10]

[-56,-85,72,-26,-14,76,-27,72,35,-21,-67,87,0,21,59,27,-92,68] => [-85, 72, 0, 68]"""


def multiple_of_index(arr):
    return [arr[i] for i in range(1, len(arr)) if arr[i] % i == 0]


#########################################################################################################
##################################            31            #############################################
#########################################################################################################

"""Implement the function unique_in_order which takes as argument a sequence and returns a list of items without any elements with the same value next to each other and preserving the original order of elements.

For example:

unique_in_order('AAAABBBCCDAABBB') == ['A', 'B', 'C', 'D', 'A', 'B']
unique_in_order('ABBCcAD')         == ['A', 'B', 'C', 'c', 'A', 'D']
unique_in_order([1, 2, 2, 3, 3])   == [1, 2, 3]
unique_in_order((1, 2, 2, 3, 3))   == [1, 2, 3]"""


def unique_in_order(sequence):
    result = []

    for i, item in enumerate(sequence):
        if i == 0 or item != sequence[i - 1]:
            result.append(item)

    return result


#########################################################################################################
##################################            32            #############################################
#########################################################################################################

"""Write a function that checks if a given string (case insensitive) is a palindrome.

A palindrome is a word, number, phrase, or other sequence of symbols that reads the same backwards as forwards,
 such as madam or racecar."""


# first solution
def is_palindrome(s):
    s = s.lower()
    middle_index = len(s) // 2

    if len(s) % 2 == 0:
        first_half = s[:middle_index]
        second_half_reversed = s[middle_index:][::-1]
    else:
        first_half = s[:middle_index]
        second_half_reversed = s[middle_index + 1:][::-1]

    return first_half == second_half_reversed


# XDD
# second solution
def is_palindrome(s):
    s = s.lower()
    middle_index = len(s) // 2
    return (
        s[:middle_index] == s[middle_index:][::-1]
        if len(s) % 2 == 0
        else s[:middle_index] == s[middle_index + 1:][::-1]
    )


# XD
# third solution
def is_palindrome(s):
    s = s.lower()
    return s == s[::-1]


#########################################################################################################
##################################            33            #############################################
#########################################################################################################

"""Define a method hello that returns "Hello, Name!" to a given name, or says Hello, World! if name is not given (or passed as an empty String).

Assuming that name is a String and it checks for user typos to return a name with a first capital letter (Xxxx).

Examples:

* With `name` = "john"  => return "Hello, John!"
* With `name` = "aliCE" => return "Hello, Alice!"
* With `name` not given 
  or `name` = ""        => return "Hello, World!"""


# first solution
def hello(name="World"):
    return (
        f"Hello, World!"
        if name == "" or name == None
        else f"Hello, {name.lower().capitalize()}!"
    )


# second solution
def hello(name=""):
    return f"Hello, {name.title() or 'World'}!"


#########################################################################################################
##################################            34            #############################################
#########################################################################################################

"""In this Kata, you will be given a string that may have mixed uppercase and lowercase letters and your task is to convert that string to either lowercase only or uppercase only based on:

make as few changes as possible.
if the string contains equal number of uppercase and lowercase letters, convert the string to lowercase.
For example:

solve("coDe") = "code". Lowercase characters > uppercase. Change only the "D" to lowercase.
solve("CODe") = "CODE". Uppercase characters > lowecase. Change only the "e" to uppercase.
solve("coDE") = "code". Upper == lower"""


def solve(s):
    lowercase_count = sum(1 for char in s if char.islower())
    uppercase_count = sum(1 for char in s if char.isupper())

    if lowercase_count >= uppercase_count:
        return s.lower()
    else:
        return s.upper()


#########################################################################################################
##################################            35            #############################################
#########################################################################################################

"""Sum of Pairs
Given a list of integers and a single sum value, return the first two values (parse from the left please) in order of appearance that add up to form the sum.

If there are two or more pairs with the required sum, the pair whose second element has the smallest index is the solution.

sum_pairs([11, 3, 7, 5],         10)
#              ^--^      3 + 7 = 10
== [3, 7]

sum_pairs([4, 3, 2, 3, 4],         6)
#          ^-----^         4 + 2 = 6, indices: 0, 2 *
#             ^-----^      3 + 3 = 6, indices: 1, 3
#                ^-----^   2 + 4 = 6, indices: 2, 4
#  * the correct answer is the pair whose second value has the smallest index
== [4, 2]

sum_pairs([0, 0, -2, 3], 2)
#  there are no pairs of values that can be added to produce 2.
== None/nil/undefined (Based on the language)

sum_pairs([10, 5, 2, 3, 7, 5],         10)
#              ^-----------^   5 + 5 = 10, indices: 1, 5
#                    ^--^      3 + 7 = 10, indices: 3, 4 *
#  * the correct answer is the pair whose second value has the smallest index
== [3, 7]
Negative numbers and duplicate numbers can and will appear."""


def sum_pairs(ints, s):
    seen = set()
    for num in ints:
        target = s - num
        if target in seen:
            return [target, num]
        seen.add(num)
    return None


#########################################################################################################
##################################            36            #############################################
#########################################################################################################

"""An anagram is the result of rearranging the letters of a word to produce a new word (see wikipedia).

Note: anagrams are case insensitive

Complete the function to return true if the two arguments given are anagrams of each other; return false otherwise.

Examples
"foefet" is an anagram of "toffee"

"Buckethead" is an anagram of "DeathCubeK"

"""


def is_anagram(test, original):
    return sorted(test.lower()) == sorted(original.lower())


#########################################################################################################
##################################            37            #############################################
#########################################################################################################
"""Create a class Ball. Ball objects should accept one argument for "ball type" when instantiated.

If no arguments are given, ball objects should instantiate with a "ball type" of "regular."

ball1 = Ball()
ball2 = Ball("super")
ball1.ball_type  #=> "regular"
ball2.ball_type  #=> "super"""


class Ball:
    def __init__(self, ball_type="regular"):
        self.ball_type = ball_type


#########################################################################################################
##################################            38            #############################################
#########################################################################################################

"""Implement a pseudo-encryption algorithm which given a string S and an integer N concatenates all the odd-indexed characters of S with all the even-indexed characters of S, this process should be repeated N times.

Examples:

encrypt("012345", 1)  =>  "135024"
encrypt("012345", 2)  =>  "135024"  ->  "304152"
encrypt("012345", 3)  =>  "135024"  ->  "304152"  ->  "012345"

encrypt("01234", 1)  =>  "13024"
encrypt("01234", 2)  =>  "13024"  ->  "32104"
encrypt("01234", 3)  =>  "13024"  ->  "32104"  ->  "20314"
Together with the encryption function, you should also implement a decryption function which reverses the process.

If the string S is an empty value or the integer N is not positive, return the first argument without changes.

"""


def encrypt(text, n):
    if not text or n <= 0:
        return text

    for _ in range(n):
        odd_chars = text[1::2]
        even_chars = text[0::2]
        text = odd_chars + even_chars
    return text


def decrypt(encrypted_text, n):
    if not encrypted_text or n <= 0:
        return encrypted_text

    lenght = len(encrypted_text)

    for _ in range(n):
        mid = lenght // 2
        odd_chars = encrypted_text[:mid]
        even_chars = encrypted_text[mid:]

        decrypted_text = []
        odd_index = 0
        even_index = 0

        for i in range(lenght):
            if i % 2 == 0:
                decrypted_text.append(even_chars[even_index])
                even_index += 1
            else:
                decrypted_text.append(odd_chars[odd_index])
                odd_index += 1

        encrypted_text = "".join(decrypted_text)

    return encrypted_text

    return


#########################################################################################################
##################################            38            #############################################
#########################################################################################################


"""Clock shows h hours, m minutes and s seconds after midnight.

Your task is to write a function which returns the time since midnight in milliseconds.

Example:
h = 0
m = 1
s = 1

result = 61000
Input constraints:

0 <= h <= 23
0 <= m <= 59
0 <= s <= 59"""


def past(h, m, s):
    return h * 3600000 + m * 60000 + s * 1000


#########################################################################################################
##################################            39            #############################################
#########################################################################################################

"""The input is a string str of digits. Cut the string into chunks (a chunk here is a substring of the initial string) of size sz (ignore the last chunk if its size is less than sz).

If the sum of a chunk's digits is divisible by 2, reverse that chunk; otherwise rotate it to the left by one position. Put together these modified chunks and return the result as a string.

If

sz is <= 0 or if str == "" return ""
sz is greater (>) than the length of str it is impossible to take a chunk of size sz hence return "".
Examples:
("123456987654", 6) --> "234561876549"
("123456987653", 6) --> "234561356789"
("66443875", 4) --> "44668753"
("66443875", 8) --> "64438756"
("664438769", 8) --> "67834466"
("123456779", 8) --> "23456771"
("", 8) --> ""
("123456779", 0) --> "" 
("563000655734469485", 4) --> "0365065073456944"
Example of a string rotated to the left by one position:
s = "123456" gives "234561"."""


def rev_rot(strng, sz):
    if sz <= 0 or strng == "" or sz > len(strng):
        return ""

    chunks = []

    for i in range(0, len(strng), sz):
        chunk = strng[i: i + sz]

        if len(chunk) == sz:
            chunk_sum = sum(int(digit) for digit in chunk)

            if chunk_sum % 2 == 0:
                chunks.append(chunk[::-1])
            else:
                chunks.append(chunk[1:] + chunk[0])

    return "".join(chunks)


#########################################################################################################
##################################            40            #############################################
#########################################################################################################

"""Your Job
Find the sum of all multiples of n below m

Keep in Mind
n and m are natural numbers (positive integers)
m is excluded from the multiples
Examples
sumMul(2, 9)   ==> 2 + 4 + 6 + 8 = 20
sumMul(3, 13)  ==> 3 + 6 + 9 + 12 = 30
sumMul(4, 123) ==> 4 + 8 + 12 + ... = 1860
sumMul(4, -7)  ==> "INVALID"""


def sum_mul(n, m):
    if n >= m or n == m:
        return 0

    if m <= n or m <= 0:
        return "INVALID"

    result = 0
    multiple_of_n = n

    while multiple_of_n <= m:
        result += multiple_of_n
        multiple_of_n += n

    return result


#########################################################################################################
##################################            41            #############################################
#########################################################################################################

"""Finish the solution so that it sorts the passed in array of numbers. If the function passes in an empty array or null/nil value then it should return an empty array.

For example:

solution([1,2,3,10,5]) # should return [1,2,3,5,10]
solution(None) # should return []"""


# Solution 1
def solution(nums):
    return [] if nums == None or nums == [] else sorted(nums)


# Solution 2
def solution(nums):
    return sorted(nums or [])


#########################################################################################################
##################################            42            #############################################
#########################################################################################################

"""Make multiple functions that will return the sum, difference, modulus, product, quotient, and the exponent respectively.

Please use the following function names:

addition = add

multiply = multiply

division = divide (both integer and float divisions are accepted)

modulus = mod

exponential = exponent

subtraction = subt

Note: All math operations will be: a (operation) b"""


def add(a, b):
    return a + b


def multiply(a, b):
    return a * b


def divide(a, b):
    return a / b


def mod(a, b):
    return a % b


def exponent(a, b):
    return a ** b


def subt(a, b):
    return a - b


#########################################################################################################
##################################            43            #############################################
#########################################################################################################

"""There's a "3 for 2" (or "2+1" if you like) offer on mangoes. For a given quantity and price (per mango), calculate the total cost of the mangoes.

Examples
mango(2, 3) ==> 6    # 2 mangoes for $3 per unit = $6; no mango for free
mango(3, 3) ==> 6    # 2 mangoes for $3 per unit = $6; +1 mango for free
mango(5, 3) ==> 12   # 4 mangoes for $3 per unit = $12; +1 mango for free
mango(9, 5) ==> 30   # 6 mangoes for $5 per unit = $30; +3 mangoes for free"""


# Solution 2
def mango(quantity, price):
    free_fruit = quantity // 3
    paid_fruit = quantity - free_fruit
    return paid_fruit * price


# Solution 2
def mango(quantity, price):
    return (quantity - quantity // 3) * price


#########################################################################################################
##################################            44            #############################################
#########################################################################################################

"""*** No Loops Allowed ***

You will be given an array a and a value x. All you need to do is check whether the provided array contains the value, without using a loop.

Array can contain numbers or strings. x can be either. Return true if the array contains the value, false if not. With strings you will need to account for case.

Looking for more, loop-restrained fun? Check out the other kata in the series:"""


def check(a, x):
    return x in a


#########################################################################################################
##################################            45            #############################################
#########################################################################################################

"""Given two numbers and an arithmetic operator (the name of it, as a string), return the result of the two numbers having that operator used on them.

a and b will both be positive integers, and a will always be the first number in the operation, and b always the second.

The four operators are "add", "subtract", "divide", "multiply".

A few examples:(Input1, Input2, Input3 --> Output)

5, 2, "add"      --> 7
5, 2, "subtract" --> 3
5, 2, "multiply" --> 10
5, 2, "divide"   --> 2.5"""


# Solutin 1
def arithmetic(a, b, operator):
    if operator == "add":
        return a + b
    elif operator == "subtract":
        return a - b
    elif operator == "multiply":
        return a * b
    elif operator == "divide":
        return a / b


# Solutin 2 without if statements
def arithmetic(a, b, operator):
    operations = {"add": a + b, "subtract": a - b, "multiply": a * b, "divide": a / b}
    return operations[operator]


#########################################################################################################
##################################            46            #############################################
#########################################################################################################

"""Take an integer n (n >= 0) and a digit d (0 <= d <= 9) as an integer.

Square all numbers k (0 <= k <= n) between 0 and n.

Count the numbers of digits d used in the writing of all the k**2.

Implement the function taking n and d as parameters and returning this count.

Examples:
n = 10, d = 1 
the k*k are 0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100
We are using the digit 1 in: 1, 16, 81, 100. The total count is then 4.

The function, when given n = 25 and d = 1 as argument, should return 11 since
the k*k that contain the digit 1 are:
1, 16, 81, 100, 121, 144, 169, 196, 361, 441.
So there are 11 digits 1 for the squares of numbers between 0 and 25.
Note that 121 has twice the digit 1."""


def nb_dig(n, d):
    count = 0
    d = str(d)

    for k in range(n + 1):
        squared = str(k ** 2)
        count += squared.count(d)

    return count


#########################################################################################################
##################################            47            #############################################
#########################################################################################################

"""Grasshopper - Function syntax debugging
A student was working on a function and made some syntax mistakes while coding. Help them find their mistakes and fix them."""

"""
def main [verb, noun]
return verb + noun
"""


def main(verb, noun):
    # This function has three problems: square brackets instead of parenthesis,
    # a colon after the parenthesis and the return command inside the
    # function is not indented.
    return verb + noun


#########################################################################################################
##################################            48            #############################################
#########################################################################################################

"""Write Number in Expanded Form
You will be given a number and you will need to return it as a string in Expanded Form. For example:

expandedForm(12)    --> should return "10 + 2"
expandedForm(42)    --> should return "40 + 2"
expandedForm(70304) --> should return "70000 + 300 + 4"
NOTE: All numbers will be whole numbers greater than 0.

If you liked this kata, check out part 2!!"""


# Solution 1
def expanded_form(num):
    numbers = []
    num = str(num)

    for i, j in enumerate(num[::-1]):
        if j != "0":
            numbers.append(str(int(j) * (10 ** i)))

    numbers = numbers[::-1]
    return (" + ").join(numbers)


# Solution 2 this one was made by user rafiathallah3 all credits go to him. Yes I took it but it's to impressive to be left alone and for me to have chance about forgeting about this masterpice.
def expanded_form(num):
    """
    ⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿⠛⠛⠛⠋⠉⠈⠉⠉⠉⠉⠛⠻⢿⣿⣿⣿⣿⣿⣿⣿
    ⣿⣿⣿⣿⣿⡿⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠛⢿⣿⣿⣿⣿
    ⣿⣿⣿⣿⡏⣀⠀⠀⠀⠀⠀⠀⠀⣀⣤⣤⣤⣄⡀⠀⠀⠀⠀⠀⠀⠀⠙⢿⣿⣿
    ⣿⣿⣿⢏⣴⣿⣷⠀⠀⠀⠀⠀⢾⣿⣿⣿⣿⣿⣿⡆⠀⠀⠀⠀⠀⠀⠀⠈⣿⣿
    ⣿⣿⣟⣾⣿⡟⠁⠀⠀⠀⠀⠀⢀⣾⣿⣿⣿⣿⣿⣷⢢⠀⠀⠀⠀⠀⠀⠀⢸⣿
    ⣿⣿⣿⣿⣟⠀⡴⠄⠀⠀⠀⠀⠀⠀⠙⠻⣿⣿⣿⣿⣷⣄⠀⠀⠀⠀⠀⠀⠀⣿
    ⣿⣿⣿⠟⠻⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠶⢴⣿⣿⣿⣿⣿⣧⠀⠀⠀⠀⠀⠀⣿
    ⣿⣁⡀⠀⠀⢰⢠⣦⠀⠀⠀⠀⠀⠀⠀⠀⢀⣼⣿⣿⣿⣿⣿⡄⠀⣴⣶⣿⡄⣿
    ⣿⡋⠀⠀⠀⠎⢸⣿⡆⠀⠀⠀⠀⠀⠀⣴⣿⣿⣿⣿⣿⣿⣿⠗⢘⣿⣟⠛⠿⣼
    ⣿⣿⠋⢀⡌⢰⣿⡿⢿⡀⠀⠀⠀⠀⠀⠙⠿⣿⣿⣿⣿⣿⡇⠀⢸⣿⣿⣧⢀⣼
    ⣿⣿⣷⢻⠄⠘⠛⠋⠛⠃⠀⠀⠀⠀⠀⢿⣧⠈⠉⠙⠛⠋⠀⠀⠀⣿⣿⣿⣿⣿
    ⣿⣿⣧⠀⠈⢸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠟⠀⠀⠀⠀⢀⢃⠀⠀⢸⣿⣿⣿⣿
    ⣿⣿⡿⠀⠴⢗⣠⣤⣴⡶⠶⠖⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⡸⠀⣿⣿⣿⣿
    ⣿⣿⣿⡀⢠⣾⣿⠏⠀⠠⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠛⠉⠀⣿⣿⣿⣿
    ⣿⣿⣿⣧⠈⢹⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⣿⣿⣿⣿
    ⣿⣿⣿⣿⡄⠈⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣴⣾⣿⣿⣿⣿⣿
    ⣿⣿⣿⣿⣧⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿
    ⣿⣿⣿⣿⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
    ⣿⣿⣿⣿⣿⣦⣄⣀⣀⣀⣀⠀⠀⠀⠀⠘⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
    ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡄⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
    ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⠀⠀⠀⠙⣿⣿⡟⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿
    ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠇⠀⠁⠀⠀⠹⣿⠃⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿
    ⣿⣿⣿⣿⣿⣿⣿⣿⡿⠛⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⢐⣿⣿⣿⣿⣿⣿⣿⣿⣿
    ⣿⣿⣿⣿⠿⠛⠉⠉⠁⠀⢻⣿⡇⠀⠀⠀⠀⠀⠀⢀⠈⣿⣿⡿⠉⠛⠛⠛⠉⠉
    ⣿⡿⠋⠁⠀⠀⢀⣀⣠⡴⣸⣿⣇⡄⠀⠀⠀⠀⢀⡿⠄⠙⠛⠀⣀⣠⣤⣤⠄

    Why yes i love programming, How do you know?
    """

    return " + ".join(
        [
            str(int(v) * int("1" + "0" * (len(str(num)) - (i + 1))))
            for i, v in enumerate(str(num))
            if v != "0"
        ]
    )


#########################################################################################################
##################################            49            #############################################
#########################################################################################################


"""Given a number of points on a plane, your task is to find two points with the smallest distance between them in linearithmic O(n log n) time.

Example
  1  2  3  4  5  6  7  8  9
1  
2    . A
3                . D
4                   . F       
5             . C
6              
7                . E
8    . B
9                   . G
For the plane above, the input will be:

(
  (2,2), # A
  (2,8), # B
  (5,5), # C
  (6,3), # D
  (6,7), # E
  (7,4), # F
  (7,9)  # G
)
=> closest pair is: ((6,3),(7,4)) or ((7,4),(6,3))
(both answers are valid. You can return a list of tuples too)
The two points that are closest to each other are D and F.
Expected answer should be an array with both points in any order.

Goal
The goal is to come up with a function that can find two closest points for any arbitrary array of points, in a linearithmic time.

Note: Don't use math.hypot, it's too slow...

More information on wikipedia."""

from math import sqrt


# This function calculate distance between points
def distance(p1, p2):
    return sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)


# This function search closest  pair of points in strip
def closest_strip(strip, d):
    min_dist = d
    closest_pair = None
    strip.sort(key=lambda p: p[1])

    # Search for pair of points in the strip
    for i in range(len(strip)):
        for j in range(i + 1, len(strip)):
            if (strip[j][1] - strip[i][1]) < min_dist:
                dist = distance(strip[i], strip[j])
                if dist < min_dist:
                    min_dist = dist
                    closest_pair = ((strip[i]), strip[j])
            else:
                break
    return closest_pair, min_dist


# Recurecting function divide and win
def closest_recursive(points_x, points_y):
    # if we have less than four points we bruteforce the problem
    if len(points_x) <= 3:
        min_dist = float("inf")
        closest_pair = None
        for i in range(len(points_x)):
            for j in range(i + 1, len(points_x)):
                dist = distance(points_x[i], points_x[j])

                if dist < min_dist:
                    min_dist = dist
                    closest_pair = (points_x[i], points_x[j])
        return closest_pair, min_dist

    # Finding center of the plain
    mid = len(points_x) // 2
    midpoint = points_x[mid]

    # Divide points in two halves
    left_x = points_x[:mid]
    right_x = points_x[mid:]

    # Save points sorted by coordinates y
    left_y = list(filter(lambda p: p[0] <= midpoint[0], points_y))
    right_y = list(filter(lambda p: p[0] > midpoint[0], points_y))

    # Find closest pair in both halves
    closest_left, dist_left = closest_recursive(left_x, left_y)
    closest_right, dist_right = closest_recursive(right_x, right_y)

    # Finding minimal distance between points in both halves
    d = min(dist_left, dist_right)
    closest_pair = closest_left if dist_left < dist_right else closest_right

    # Making strip including points nirby divide
    strip = [p for p in points_y if abs(p[0] - midpoint[0]) < d]

    # Finding closest pair of points in strip
    closest_in_strip, dist_strip = closest_strip(strip, d)

    # Aktualizing minimal distance, if closest pair is in strip
    if dist_strip < d:
        return closest_in_strip, dist_strip
    else:
        return closest_pair, d


def closest_pair(points):
    points_x = sorted(points, key=lambda p: p[0])
    points_y = sorted(points, key=lambda p: p[1])

    closest, _ = closest_recursive(points_x, points_y)
    return closest


points = [
    (2, 2),  # A
    (2, 8),  # B
    (5, 5),  # C
    (6, 3),  # D
    (6, 7),  # E
    (7, 4),  # F
    (7, 9),  # G
]
result = closest_pair(points)

#########################################################################################################
##################################            50            #############################################
#########################################################################################################

"""A string is considered to be in title case if each word in the string is either (a) capitalised (that is, only the first letter of the word is in upper case) or (b) considered to be an exception and put entirely into lower case unless it is the first word, which is always capitalised.

Write a function that will convert a string into title case, given an optional list of exceptions (minor words). The list of minor words will be given as a string with each word separated by a space. Your function should ignore the case of the minor words string -- it should behave in the same way even if the case of the minor word string is changed.

Arguments (Haskell)
First argument: space-delimited list of minor words that must always be lowercase except for the first word in the string.
Second argument: the original string to be converted.
Arguments (Other languages)
First argument (required): the original string to be converted.
Second argument (optional): space-delimited list of minor words that must always be lowercase except for the first word in the string. The JavaScript/CoffeeScript tests will pass undefined when this argument is unused.
Example
title_case('a clash of KINGS', 'a an the of') # should return: 'A Clash of Kings'
title_case('THE WIND IN THE WILLOWS', 'The In') # should return: 'The Wind in the Willows'
title_case('the quick brown fox') # should return: 'The Quick Brown Fox'"""


def title_case(title: str, minor_words: str = ""):
    minor_words = minor_words.lower().split() if minor_words else []
    words = title.split()
    result = []

    for i, word in enumerate(words):
        if i == 0:
            result.append(word.capitalize())
        elif word.lower() in minor_words:
            result.append(word.lower())
        else:
            result.append(word.capitalize())

    return " ".join(result)


#########################################################################################################
##################################            51            #############################################
#########################################################################################################

# IDK WTF it is?!
"""Messi's Goal Total
Use variables to find the sum of the goals Messi scored in 3 competitions

Information
Messi goal scoring statistics:

Competition	Goals
La Liga	43
Champions League	10
Copa del Rey	5
Task
Create these three variables and store the appropriate values using the table above:
la_liga_goals
champions_league_goals
copa_del_rey_goals
Create a fourth variable named total_goals that stores the sum of all of Messi's goals for this year."""

la_liga_goals, champions_league_goals, copa_del_rey_goals = 43, 10, 5

total_goals = la_liga_goals + champions_league_goals + copa_del_rey_goals

#########################################################################################################
##################################            52            #############################################
#########################################################################################################

"""The museum of incredibly dull things
The museum of incredibly dull things wants to get rid of some exhibits. Miriam, the interior architect, comes up with a plan to remove the most boring exhibits. She gives them a rating, and then removes the one with the lowest rating.

However, just as she finished rating all exhibits, she's off to an important fair, so she asks you to write a program that tells her the ratings of the exhibits after removing the lowest one. Fair enough.
 
 
Task
Given an array of integers, remove the smallest value. Do not mutate the original array/list. If there are multiple elements with the same value, remove the one with the lowest index. If you get an empty array/list, return an empty array/list.

Don't change the order of the elements that are left.

Examples
* Input: [1,2,3,4,5], output = [2,3,4,5]
* Input: [5,3,2,1,4], output = [5,3,2,4]
* Input: [2,2,1,2,1], output = [2,2,2,1]"""


def remove_smallest(numbers):
    if not numbers:
        return []

    result = numbers[:]
    min_index = result.index(min(result))
    result.pop(min_index)

    return result


#########################################################################################################
##################################            52            #############################################
#########################################################################################################


"""Philip's just turned four and he wants to know how old he will be in various years in the future such as 2090 or 3044. His parents can't keep up calculating this so they've begged you to help them out by writing a programme that can answer Philip's endless questions.

Your task is to write a function that takes two parameters: the year of birth and the year to count years in relation to. As Philip is getting more curious every day he may soon want to know how many years it was until he would be born, so your function needs to work with both dates in the future and in the past.

Provide output in this format: For dates in the future: "You are ... year(s) old." For dates in the past: "You will be born in ... year(s)." If the year of birth equals the year requested return: "You were born this very year!"

"..." are to be replaced by the number, followed and proceeded by a single space. Mind that you need to account for both "year" and "years", depending on the result.

Good Luck!"""


# Solution 1
def calculate_age(year_of_birth, current_year):
    calculated_year = current_year - year_of_birth
    if calculated_year > 0:
        return f"You are {calculated_year} {'years' if calculated_year > 1 or calculated_year * (-1) > 1 else 'year'} old."
    elif current_year == year_of_birth:
        return "You were born this very year!"
    else:
        return f"You will be born in {calculated_year * (-1)} {'years' if calculated_year > 1 or calculated_year * (-1) > 1 else 'year'}."


# Solution 2
def calculate_age(year_of_birth, current_year):
    diff = abs(current_year - year_of_birth)
    age = "#d year%s" % (diff, "s" * bool(diff - 1))
    return (
        "You were born this very year!"
        if not diff
        else (
            "You are %s old." % age
            if current_year > year_of_birth
            else "You will be born in %s." % age
        )
    )


#########################################################################################################
##################################            52            #############################################
#########################################################################################################

"""Complete the function which converts a binary number (given as a string) to a decimal number."""


# Solution 1
def bin_to_decimal(inp):
    if not all(c in "01" for c in inp):
        raise ValueError("The input is not a valid binary number")

    result = 0

    for pos, num in enumerate(reversed(inp)):
        if num == "1":
            i = 2 ** int(pos)
            result += i

    return result


# Solution 2
def bin_to_decimal(inp):
    return int(inp, 2)


#########################################################################################################
##################################            53            #############################################
#########################################################################################################


"""Create a function called _if which takes 3 arguments: a value bool and 2 functions (which do not take any parameters): func1 and func2

When bool is truthy, func1 should be called, otherwise call the func2.

Example:
def truthy(): 
  print("True")
  
def falsey(): 
  print("False")
  
_if(True, truthy, falsey)
# prints 'True' to the console"""


def _if(bool, func1, func2):
    func2() if bool else func1()


#########################################################################################################
##################################            54            #############################################
#########################################################################################################

"""Jamie is a programmer, and James' girlfriend. She likes diamonds, and wants a diamond string from James. Since James doesn't know how to make this happen, he needs your help.

Task
You need to return a string that looks like a diamond shape when printed on the screen, using asterisk (*) characters. Trailing spaces should be removed, and every line must be terminated with a newline character (\n).

Return null/nil/None/... if the input is an even number or negative, as it is not possible to print a diamond of even or negative size.

Examples
A size 3 diamond:

 *
***
 *
...which would appear as a string of " *\n***\n *\n"

A size 5 diamond:

  *
 ***
*****
 ***
  *
...that is:

"  *\n ***\n*****\n ***\n  *\n"""


def diamond(n):
    if n <= 0 or n % 2 == 0:
        return None

    result = ""
    mid = n // 2

    # Upper half of diamond
    for i in range(mid + 1):
        spaces = mid - i
        stars = 2 * i + 1
        result += " " * spaces + "*" * stars + "\n"

    # Down half of diamond
    for i in range(mid - 1, -1, -1):
        spaces = mid - i
        stars = 2 * i + 1
        result += " " * spaces + "*" * stars + "\n"

    return result


#########################################################################################################
##################################            55            #############################################
#########################################################################################################

"""A stream of data is received and needs to be reversed.

Each segment is 8 bits long, meaning the order of these segments needs to be reversed, for example:

11111111  00000000  00001111  10101010
 (byte1)   (byte2)   (byte3)   (byte4)
should become:

10101010  00001111  00000000  11111111
 (byte4)   (byte3)   (byte2)   (byte1)
The total number of bits will always be a multiple of 8.

The data is given in an array as such:

[1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,0,1,0,1,0,1,0]
Note: In the C and NASM languages you are given the third parameter which is the number of segment blocks.

"""


def data_reverse(data):
    segments = [data[i: i + 8] for i in range(0, len(data), 8)]
    reversed_segments = segments[::-1]
    result = [bit for segment in reversed_segments for bit in segment]
    return result


#########################################################################################################
##################################            56            #############################################
#########################################################################################################


"""Kids drink toddy.
Teens drink coke.
Young adults drink beer.
Adults drink whisky.
Make a function that receive age, and return what they drink.

Rules:

Children under 14 old.
Teens under 18 old.
Young under 21 old.
Adults have 21 or more.
Examples: (Input --> Output)

13 --> "drink toddy"
17 --> "drink coke"
18 --> "drink beer"
20 --> "drink beer"
30 --> "drink whisky"""


# solution 1
def people_with_age_drink(age):
    instructions = [
        (14, "drink toddy"),
        (18, "drink coke"),
        (21, "drink beer"),
        (float("inf"), "drink whisky"),
    ]
    return next(drink for limit, drink in instructions if age < limit)


# solution 2
def people_with_age_drink(age):
    return "drink " + (
        "toddy"
        if age < 14
        else "coke" if age < 18 else "beer" if age < 21 else "whisky"
    )


#########################################################################################################
##################################            57            #############################################
#########################################################################################################

"""Description:
Remove all exclamation marks from the end of sentence.

Examples
"Hi!"     ---> "Hi"
"Hi!!!"   ---> "Hi"
"!Hi"     ---> "!Hi"
"!Hi!"    ---> "!Hi"
"Hi! Hi!" ---> "Hi! Hi"
"Hi"      ---> "Hi"""


# solution 1
def remove(st):
    while st.endswith("!"):
        st = st[:-1]
    return st


# solution 2
def remove(s):
    return s.rstrip("!")


#########################################################################################################
##################################            58            #############################################
#########################################################################################################

"""When provided with a letter, return its position in the alphabet.

Input :: "a"

Output :: "Position of alphabet: 1"

Note: Only lowercased English letters are tested

"""


# Solution 1
def position(alphabet):
    poz_in_alph = {
        "a": 1,
        "b": 2,
        "c": 3,
        "d": 4,
        "e": 5,
        "f": 6,
        "g": 7,
        "h": 8,
        "i": 9,
        "j": 10,
        "k": 11,
        "l": 12,
        "m": 13,
        "n": 14,
        "o": 15,
        "p": 16,
        "q": 17,
        "r": 18,
        "s": 19,
        "t": 20,
        "u": 21,
        "v": 22,
        "w": 23,
        "x": 24,
        "y": 25,
        "z": 26,
    }
    for letter, poz in poz_in_alph.items():
        if alphabet == letter:
            return f"Position of alphabet: {poz}"


# Solution 2
def position_polish(alphabet):
    alphabet_list = [
        "a",
        "b",
        "c",
        "d",
        "e",
        "f",
        "g",
        "h",
        "i",
        "j",
        "k",
        "l",
        "m",
        "n",
        "o",
        "p",
        "q",
        "r",
        "s",
        "t",
        "u",
        "w",
        "x",
        "y",
        "z",
        "ź",
        "ż",
    ]
    return f"Position of alphabet {alphabet_list.index(alphabet) + 1}"


"abcdefghijklmnopqrstuwxyz"


# Solution 3
def position(alphabet):
    return f"Position of alphabet:{ord(alphabet) - ord('a') + 1}"


#########################################################################################################
##################################            59            #############################################
#########################################################################################################

"""You were camping with your friends far away from home, but when it's time to go back, you realize that your fuel is running out and the nearest pump is 50 miles away! You know that on average, your car runs on about 25 miles per gallon. There are 2 gallons left.

Considering these factors, write a function that tells you if it is possible to get to the pump or not.

Function should return true if it is possible and false if not."""


def zero_fuel(distance_to_pump, mpg, fuel_left):
    return True if fuel_left * mpg >= distance_to_pump else False


#########################################################################################################
##################################            60            #############################################
#########################################################################################################

"""Create a method that accepts a list and an item, and returns true if the item belongs to the list, otherwise false."""


def include(arr, item):
    return item in arr


#########################################################################################################
##################################            61            #############################################
#########################################################################################################

"""Write a function which takes a number and returns the corresponding ASCII char for that value.

Example:

65 --> 'A'
97 --> 'a'
48 --> '0"""


def get_char(c):
    return chr(c)


#########################################################################################################
##################################            62            #############################################
#########################################################################################################

"""ntroduction
There is a war and nobody knows - the alphabet war!
There are two groups of hostile letters. The tension between left side letters and right side letters was too high and the war began.

Task
Write a function that accepts fight string consists of only small letters and return who wins the fight. When the left side wins return Left side wins!, when the right side wins return Right side wins!, in other case return Let's fight again!.

The left side letters and their power:

 w - 4
 p - 3
 b - 2
 s - 1
The right side letters and their power:

 m - 4
 q - 3
 d - 2
 z - 1
The other letters don't have power and are only victims.

Example
AlphabetWar("z");        //=> Right side wins!
AlphabetWar("zdqmwpbs"); //=> Let's fight again!
AlphabetWar("zzzzs");    //=> Right side wins!
AlphabetWar("wwwwwwz");  //=> Left side wins!"""


def alphabet_war(fight):
    left_side = {"w": 4, "p": 3, "b": 2, "s": 1}
    right_side = {"m": 4, "q": 3, "d": 2, "z": 1}

    count_left = 0
    count_right = 0

    for letter in fight:
        if letter in left_side:
            count_left += left_side[letter]
        elif letter in right_side:
            count_right += right_side[letter]

    if count_right > count_left:
        return "Right side wins!"
    elif count_left > count_right:
        return "Left side wins!"
    else:
        return "Let's fight again!"


#########################################################################################################
##################################            63            #############################################
#########################################################################################################


"""You get any card as an argument. Your task is to return the suit of this card (in lowercase).

Our deck (is preloaded):

DECK = ['2S','3S','4S','5S','6S','7S','8S','9S','10S','JS','QS','KS','AS',
        '2D','3D','4D','5D','6D','7D','8D','9D','10D','JD','QD','KD','AD',
        '2H','3H','4H','5H','6H','7H','8H','9H','10H','JH','QH','KH','AH',
        '2C','3C','4C','5C','6C','7C','8C','9C','10C','JC','QC','KC','AC']
('3C') -> return 'clubs'
('3D') -> return 'diamonds'
('3H') -> return 'hearts'
('3S') -> return 'spades'"""


# Solution 1
def define_suit(card):
    suits = {"c": "clubs", "d": "diamonds", "h": "hearts", "s": "spades"}
    for i, j in suits.items():
        if i in card.lower():
            return j


# Solution 2
def define_suit(card):
    return {"C": "clubs", "S": "spades", "D": "diamonds", "H": "hearts"}[card[-1]]


#########################################################################################################
##################################            64            #############################################
#########################################################################################################

"""Combine strings function
Create a function named combineNames/combine_names/CombineNames that accepts two parameters (first and last name). The function should return the full name.

Example:

With "James" as the first name and "Stevens" as the last name should return "James Stevens"""


def combine_names(first_name, last_name):
    return first_name + " " + last_name


#########################################################################################################
##################################            65            #############################################
#########################################################################################################

"""Terminal game move function
In this game, the hero moves from left to right. The player rolls the dice and moves the number of spaces indicated by the dice two times.

Create a function for the terminal game that takes the current position of the hero and the roll (1-6) and return the new position.

Example:
move(3, 6) should equal 15"""


def move(position, roll):
    return position + roll * 2


#########################################################################################################
##################################            66            #############################################
#########################################################################################################

"""In a small town the population is p0 = 1000 at the beginning of a year. The population regularly increases by 2 percent per year and moreover 50 new inhabitants per year come to live in the town. How many years does the town need to see its population greater than or equal to p = 1200 inhabitants?

At the end of the first year there will be: 
1000 + 1000 * 0.02 + 50 => 1070 inhabitants

At the end of the 2nd year there will be: 
1070 + 1070 * 0.02 + 50 => 1141 inhabitants (** number of inhabitants is an integer **)

At the end of the 3rd year there will be:
1141 + 1141 * 0.02 + 50 => 1213

It will need 3 entire years.
More generally given parameters:

p0, percent, aug (inhabitants coming or leaving each year), p (population to equal or surpass)

the function nb_year should return n number of entire years needed to get a population greater or equal to p.

aug is an integer, percent a positive or null floating number, p0 and p are positive integers (> 0)

Examples:
nb_year(1500, 5, 100, 5000) -> 15
nb_year(1500000, 2.5, 10000, 2000000) -> 10"""


def nb_year(p0, percent, aug, p):
    population = p0
    year = 0
    while population < p:
        population += population * percent * 0.01 + aug
        year += 1

    return year + 1 if round(population) else year


#########################################################################################################
##################################            67            #############################################
#########################################################################################################

"""Create a function that converts US dollars (USD) to Chinese Yuan (CNY) . The input is the amount of USD as an integer, and the output should be a string that states the amount of Yuan followed by 'Chinese Yuan'

Examples (Input -> Output)
15  -> '101.25 Chinese Yuan'
465 -> '3138.75 Chinese Yuan'
The conversion rate you should use is 6.75 CNY for every 1 USD. All numbers should be represented as a string with 2 decimal places. (e.g. "21.00" NOT "21.0" or "21")"""


def usdcny(usd):
    return f"{(usd * 6.75):.2f} Chinese Yuan"


#########################################################################################################
##################################            67            #############################################
#########################################################################################################


"""Wolves have been reintroduced to Great Britain. You are a sheep farmer, and are now plagued by wolves which pretend to be sheep. Fortunately, you are good at spotting them.

Warn the sheep in front of the wolf that it is about to be eaten. Remember that you are standing at the front of the queue which is at the end of the array:

[sheep, sheep, sheep, sheep, sheep, wolf, sheep, sheep]      (YOU ARE HERE AT THE FRONT OF THE QUEUE)
   7      6      5      4      3            2      1
If the wolf is the closest animal to you, return "Pls go away and stop eating my sheep". Otherwise, return "Oi! Sheep number N! You are about to be eaten by a wolf!" where N is the sheep's position in the queue.

Note: there will always be exactly one wolf in the array.

Examples
Input: ["sheep", "sheep", "sheep", "wolf", "sheep"]
Output: "Oi! Sheep number 1! You are about to be eaten by a wolf!"

Input: ["sheep", "sheep", "wolf"]
Output: "Pls go away and stop eating my sheep"""


def warn_the_sheep(queue):
    wolf_position = queue.index("wolf")  # Find where the wolf is

    if wolf_position == len(queue) - 1:
        return "Pls go away and stop eating my sheep"
    else:
        sheep_number = len(queue) - wolf_position - 1
        return f"Oi! Sheep number {sheep_number}! You are about to be eaten by a wolf!"


#########################################################################################################
##################################            67            #############################################
#########################################################################################################


"""You need to write regex that will validate a password to make sure it meets the following criteria:

At least six characters long
contains a lowercase letter
contains an uppercase letter
contains a digit
only contains alphanumeric characters (note that '_' is not alphanumeric)"""

# Solution
import re

regex = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[A-Za-z\d]{6,}"

# Ściągawka
"""
^              # begin word
(?=.*?[a-z])   # at least one lowercase letter
(?=.*?[A-Z])   # at least one uppercase letter
(?=.*?[0-9])   # at least one number
[A-Za-z\d]     # only alphanumeric
{6,}           # at least 6 characters long
$              # end word
"""

#########################################################################################################
##################################            68            #############################################
#########################################################################################################

"""Trolls are attacking your comment section!

A common way to deal with this situation is to remove all of the vowels from the trolls' comments, neutralizing the threat.

Your task is to write a function that takes a string and return a new string with all vowels removed.

For example, the string "This website is for losers LOL!" would become "Ths wbst s fr lsrs LL!".

Note: for this kata y isn't considered a vowel."""


# first attempt
def disemvowel(string_):
    vowels = "aeiou"
    new_str = ""
    for vowel in string_.lower():
        if vowel in vowels:
            new_str = string_.replace(vowel, "")
    return new_str


# Solution 1
def disemvowel(string_):
    for i in "aeiouAEIOU":
        text = text.replace(i, "")
    return text


# Solution 2
def disemvowel(string_):
    vowels = "aeiouAEIOU"
    return "".join([vowel for vowel in string_ if vowel not in vowels])


# attempt with re
import re


def disemvowel(string_):
    return re.sub("[aeiou]", "", string_, flags=re.IGNORECASE)


#########################################################################################################
##################################            69            #############################################
#########################################################################################################

"""
Create a function that accepts a list/array and a number n, and returns a list/array of the first n elements from the list/array.

If you need help, here's a reference:
"""


def take(arr, n):
    return arr[:n]


#########################################################################################################
##################################            70            #############################################
#########################################################################################################

"""Deoxyribonucleic acid, DNA is the primary information storage molecule in biological systems. It is composed of four nucleic acid bases Guanine ('G'), Cytosine ('C'), Adenine ('A'), and Thymine ('T').

Ribonucleic acid, RNA, is the primary messenger molecule in cells. RNA differs slightly from DNA its chemical structure and contains no Thymine. In RNA Thymine is replaced by another nucleic acid Uracil ('U').

Create a function which translates a given DNA string into RNA.

For example:

"GCAT"  =>  "GCAU"
The input string can be of arbitrary length - in particular, it may be empty. All input is guaranteed to be valid, i.e. each input string will only ever consist of 'G', 'C', 'A' and/or 'T'."""


# Solution 1
def dna_to_rna(dna):
    return "".join(["U" if nuclei == "T" else nuclei for nuclei in dna])


# Solution 2
def dna_to_rna(dna):
    return dna.replace("T", "U")


#########################################################################################################
##################################            71            #############################################
#########################################################################################################

"""The purpose of this kata is to work out just how many bottles of duty free whiskey you would have to buy such that the savings over the normal high street price would effectively cover the cost of your holiday.

You will be given the high street price (normPrice, in £ (Pounds)), the duty free discount (discount, in percent) and the cost of the holiday (in £).

For example, if a bottle costs £10 normally and the duty free discount is 10%, you would save £1 per bottle. If your holiday will cost £500, you would have to purchase 500 bottles to save £500, so the answer you return should be 500.

Another example: if a bottle costs £12 normally and the duty free discount is 50%, you would save £6 per bottle. If your holiday will cost £1000, you would have to purchase 166.66 bottles to save £1000, so your answer should be 166 bottles.

All inputs will be integers. Please return an integer. Round down."""


# For more precise mesurement but definetly worse for what you want to achive XD
def duty_free(price, discount, holiday_cost):
    return float(
        f"You have to sell: {(holiday_cost / (price * discount * 0.01)):.2f} bottle{'s' if holiday_cost / (price * discount) else ''} of stuff."
    )


# What is required to pass this exercise
def duty_free(price, discount, holiday_cost):
    return holiday_cost // (price * discount * 0.01)


#########################################################################################################
##################################            72            #############################################
#########################################################################################################

"""Description:
Remove all exclamation marks from sentence but ensure a exclamation mark at the end of string. For a beginner kata, you can assume that the input data is always a non empty string, no need to verify it.

Examples
"Hi!"     ---> "Hi!"
"Hi!!!"   ---> "Hi!"
"!Hi"     ---> "Hi!"
"!Hi!"    ---> "Hi!"
"Hi! Hi!" ---> "Hi Hi!"
"Hi"      ---> "Hi!"""
import unittest


# def remove(st):
#     return ' '.join(
#         [char.replace('!', '') + '!' for char in st.split()]
#     ) This didn;t work as intendet


def remove(st):
    cleaned = st.replace("!", "")
    return cleaned + "!"


def remove(st):
    return st.replace("!", "") + "!"


# tests = [
#     ["Hi!", "Hi!"],
#     ["Hi!!!", "Hi!"],
#     ["!Hi", "Hi!"],
#     ["!Hi!", "Hi!"],
#     ["Hi! Hi!", "Hi Hi!"],
#     ["Hi", "Hi!"],
# ]
#
# class FastTest(unittest.TestCase):
#     def test_remove(self):
#         for inp, outp in tests:
#             self.assertEqual(remove(inp), outp)

# if __name__ == '__main__':
#     unittest.main()


#########################################################################################################
##################################            73            #############################################
#########################################################################################################


"""Given two strings s1 and s2, we want to visualize how different the two strings are. We will only take into account the lowercase letters (a to z). First let us count the frequency of each lowercase letters in s1 and s2.

s1 = "A aaaa bb c"

s2 = "& aaa bbb c d"

s1 has 4 'a', 2 'b', 1 'c'

s2 has 3 'a', 3 'b', 1 'c', 1 'd'

So the maximum for 'a' in s1 and s2 is 4 from s1; the maximum for 'b' is 3 from s2. In the following we will not consider letters when the maximum of their occurrences is less than or equal to 1.

We can resume the differences between s1 and s2 in the following string: "1:aaaa/2:bbb" where 1 in 1:aaaa stands for string s1 and aaaa because the maximum for a is 4. In the same manner 2:bbb stands for string s2 and bbb because the maximum for b is 3.

The task is to produce a string in which each lowercase letters of s1 or s2 appears as many times as its maximum if this maximum is strictly greater than 1; these letters will be prefixed by the number of the string where they appear with their maximum value and :. If the maximum is in s1 as well as in s2 the prefix is =:.

In the result, substrings (a substring is for example 2:nnnnn or 1:hhh; it contains the prefix) will be in decreasing order of their length and when they have the same length sorted in ascending lexicographic order (letters and digits - more precisely sorted by codepoint); the different groups will be separated by '/'. See examples and "Example Tests".

Hopefully other examples can make this clearer.

s1 = "my&friend&Paul has heavy hats! &"
s2 = "my friend John has many many friends &"
mix(s1, s2) --> "2:nnnnn/1:aaaa/1:hhh/2:mmm/2:yyy/2:dd/2:ff/2:ii/2:rr/=:ee/=:ss"

s1 = "mmmmm m nnnnn y&friend&Paul has heavy hats! &"
s2 = "my frie n d Joh n has ma n y ma n y frie n ds n&"
mix(s1, s2) --> "1:mmmmmm/=:nnnnnn/1:aaaa/1:hhh/2:yyy/2:dd/2:ff/2:ii/2:rr/=:ee/=:ss"

s1="Are the kids at home? aaaaa fffff"
s2="Yes they are here! aaaaa fffff"
mix(s1, s2) --> "=:aaaaaa/2:eeeee/=:fffff/1:tt/2:rr/=:hh"
Note for Swift, R, PowerShell
The prefix =: is replaced by E:

s1 = "mmmmm m nnnnn y&friend&Paul has heavy hats! &"
s2 = "my frie n d Joh n has ma n y ma n y frie n ds n&"
mix(s1, s2) --> "1:mmmmmm/E:nnnnnn/1:aaaa/1:hhh/2:yyy/2:dd/2:ff/2:ii/2:rr/E:ee/E:ss"""

from collections import Counter


def mix(s1, s2):
    count1 = Counter([char for char in s1 if char.islower()])
    count2 = Counter([char for char in s2 if char.islower()])
    result = []

    for char in set(count1.keys()).union(count2.keys()):
        count_s1 = count1.get(char, 0)
        count_s2 = count2.get(char, 0)

        if max(count_s1, count_s2) > 1:
            if count_s1 > count_s2:
                result.append(f"1:{char * count_s1}")
            elif count_s2 > count_s1:
                result.append(f"2:{char * count_s2}")
            else:
                result.append(f"=:{char * count_s1}")

    result.sort(key=lambda x: (-len(x), x))

    return "/".join(result)


#########################################################################################################
##################################            74            #############################################
#########################################################################################################


"""Write a simple regex to validate a username. Allowed characters are:

lowercase letters,
numbers,
underscore
Length should be between 4 and 16 characters (both included)."""

import re
import random
import string


def validate_usr(username):
    regex = r"^([a-z0-9_]){4,16}$"
    return bool(re.fullmatch(regex, username))


tests_74 = {
    "asddsa": True,
    "a": False,
    "Hass": False,
    "Hasd_12assssssasasasasasaasasasasas": False,
    "": False,
    "____": True,
    "012": False,
    "p111p": True,
    "asd43 34": False,
    "asd43_34": True,
    "too_long_username_with_only_valid_characters_123": False,
}

# Tests


# def generate_randmo_username():
#     lenght = random.randint(1, 20)
#     chars = string.ascii_lowercase + string.digits + "_"
#     username = "".join(random.choice(chars) for _ in range(lenght))
#     is_valid = (
#         4 <= len(username) <= 16
#         and re.fullmatch(r"^([a-z0-9_]){4,16}$", username) is not None
#     )
#     return username, is_valid


# class Ex74Test(unittest.TestCase):
#     def test_validate_username(self):
#         for inp, outp in tests_74.items():
#             self.assertEqual(validate_usr(inp), outp)

#     def test_random_usernames(self):
#         for _ in range(50):
#             username, expected = generate_randmo_username()
#             with self.subTest(username=username):
#                 self.assertEqual(validate_usr(username), expected)


# if __name__ == "__main__":
#     unittest.main()

#########################################################################################################
##################################            75            #############################################
#########################################################################################################

"""Task Description
You're re-designing a blog, and the blog's posts have the Weekday Month Day, time format for showing the date and time when a post was made, e.g., Friday May 2, 7pm.

You're running out of screen real estate, and on some pages you want to display a shorter format, Weekday Month Day that omits the time.

Write a function that takes the website date/time in its original string format and returns the shortened format.

Input
Input will always be a string, e.g., "Friday May 2, 7pm". 

Output
Output will be the shortened string, e.g., "Friday May 2"."""

import datetime
import random


# Version 1
def shorten_to_date(long_date):
    long_date = long_date.replace(',', '')
    short_date = []
    for word in long_date.split(" "):
        if 'pm' not in word and 'am' not in word:
            short_date.append(word)

    return (" ").join(short_date)


# Version 2
def shorten_to_date(long_date):
    short_date = long_date.split(',')[0]
    return short_date


def generate_random_date():
    random_date = datetime.datetime.strptime(f"{random.randint(1, 365)} 2024", "%j %Y")
    weekday = random_date.strftime("%A")
    month_day = random_date.strftime("%B %d")
    hour = random.randint(1, 12)
    period = random.choice(['am', 'pm'])

    formated_date = f"{weekday} {month_day}, {hour}{period}"

    validate_date = formated_date.split(',')[0]
    return formated_date, validate_date


# class ShortDateTest(unittest.TestCase):
#     def test_validate_date(self):
#         self.assertEqual(shorten_to_date("Monday February 2, 8pm"), "Monday February 2")
#         self.assertEqual(shorten_to_date("Tuesday May 29, 8pm"), "Tuesday May 29")
#         self.assertEqual(shorten_to_date("Wed September 1, 3am"), "Wed September 1")
#         self.assertEqual(shorten_to_date("Friday May 2, 9am"), "Friday May 2")
#         self.assertEqual(shorten_to_date("Tuesday January 29, 10pm"), "Tuesday January 29")

#     def test_random_date(self):
#         for _ in range(50):
#             formated_date, validate_date = generate_random_date()
#             self.assertEqual(shorten_to_date(formated_date), validate_date)


# if __name__ == "__main__":
#     unittest.main()


#########################################################################################################
##################################            76            #############################################
#########################################################################################################

"""Given an array of integers, return a new array with each value doubled.

For example:

[1, 2, 3] --> [2, 4, 6]"""


def maps(a):
    return [i * 2 for i in a]


#########################################################################################################
##################################            77            #############################################
#########################################################################################################

"""Create a combat function that takes the player's current health and the amount of damage received, and returns the player's new health. Health can't be less than 0."""


def combat(health, damage):
    result = health - damage
    return result if result > 0 else 0


#########################################################################################################
##################################            78            #############################################
#########################################################################################################

"""
Determine the total number of digits in the integer (n>=0) given as input to the function. For example, 9 is a single digit, 66 has 2 digits and 128685 has 6 digits. Be careful to avoid overflows/underflows.

All inputs will be valid.
"""


def digits(n):
    return len(str(n))


#########################################################################################################
##################################            79            #############################################
#########################################################################################################

"""
This text is now fully mutated to this character.

Starting with the original text, and given a character, return the text once it has been mutated so that all of the characters in the original text have been replaced with the character.

If the text or the character are empty, return an empty string.
There will never be a case when both are empty as nothing is going on!!

Note: The character is a string of length 1 or an empty string.

Example
text before = "abc"
character   = "z"
text after  = "zzz"
"""
import random
import string


def contamination(text, char):
    return f'{char}' * len(text)


test_79 = {
    ('abc', 'z'): 'zzz',
    ('', 'z'): '',
    ('abc', ''): '',
    ('_3ebzgh4', '&'): '&&&&&&&&',
    ('//case', ' '): '      ',
}


def generate_random_testcase_for_contamination():
    length = random.randint(1, 400)
    characters = string.ascii_letters + string.digits
    text = ''.join(random.choices(characters, k=length))
    char = random.choice(characters)
    expected = f'{char}' * len(text)
    return text, char, expected


# class ContaminationTest(unittest.TestCase):
#     def test_contamination(self):
#         for (text, char), expected in test_79.items():
#             self.assertEqual(contamination(text, char), expected)

#     def test_random_contamination(self):
#         for _ in range(50):
#             text, char, expected = generate_random_testcase_for_contamination()
#             self.assertEqual(contamination(text, char), expected)


# if __name__ == "__main__":
#     unittest.main()


#########################################################################################################
##################################            80            #############################################
#########################################################################################################

"""In Python, there is a built-in filter function that operates similarly to JS's filter. For more information on how to use this function, visit https://docs.python.org/3/library/functions.html#filter

The solution would work like the following:

get_even_numbers([2,4,5,6]) => [2,4,6]"""
import random


def get_even_numbers(arr):
    return list(filter(lambda x: x % 2 == 0, arr))


test_80 = {
    (0, 1, 2, 3, 4, 5, 6, 7, 8, 9): [0, 2, 4, 6, 8],
    (535, 465): [],
    (10, 20, 40): [10, 20, 40],
    (3, 7, 8, 9): [8],
    (): [],
}


def generate_random_list():
    lenght = random.randint(1, 50)
    random_list = random.choices(range(1, 1001), k=lenght)
    expected = [x for x in random_list if x % 2 == 0]
    return random_list, expected


# class GetEvenNumbersTest(unittest.TestCase):
#     def test_get_even_numbers(self):
#         for input_data, expected in test_80.items():
#             with self.subTest(input_data=input_data):
#                 self.assertEqual(get_even_numbers(list(input_data)), expected)

#     def test_random_get_even_numbers(self):
#         for _ in range(50):
#             random_list, expected = generate_random_list()
#             with self.subTest(random_list=random_list, expected=expected):
#                 self.assertEqual(get_even_numbers(random_list), expected)

# if __name__ == "__main__":
#     unittest.main()


#########################################################################################################
##################################            80            #############################################
#########################################################################################################

"""
ROT13 is a simple letter substitution cipher that replaces a letter with the letter 13 letters after it in the alphabet. ROT13 is an example of the Caesar cipher.

Create a function that takes a string and returns the string ciphered with Rot13. If there are numbers or special characters included in the string, they should be returned as they are. Only letters from the latin/english alphabet should be shifted, like in the original Rot13 "implementation".

Please note that using encode is considered cheating.
"""


def rot13(message):
    result = ''
    for i in range(len(message)):
        char = message[i]
        if char == ' ':
            result += ' '

        elif char.isalpha() == False:
            result += char

        elif char.isupper():
            result += chr((ord(char) + 13 - 65) % 26 + 65)

        else:
            result += chr((ord(char) + 13 - 97) % 26 + 97)

    return result


# print(f"Coded {rot13('test')} expected 'grfg'")
# print(f"Coded {rot13('Test')} expected 'Grfg'")
# print(f"Coded {rot13('aA bB zZ 1234 *!?%')} expected 'nN oO mM 1234 *!?%'")


#########################################################################################################
##################################            81            #############################################
#########################################################################################################

"""
Create a method that takes as input a name, city, and state to welcome a person. Note that name will be an array consisting of one or more values that should be joined together with one space between each, and the length of the name array in test cases will vary.

Example:

['John', 'Smith'], 'Phoenix', 'Arizona'
This example will return the string Hello, John Smith! Welcome to Phoenix, Arizona!
"""


def say_hello(name, city, state):
    return f"Hello, {(' ').join(name)}! Welcome to {city}, {state}!"


#########################################################################################################
##################################            82            #############################################
#########################################################################################################

"""
Your task is to write function factorial.

https://en.wikipedia.org/wiki/Factorial
"""


# solution with while loop
def factorial(n):
    if n == 0:
        return 1

    current = n
    number = n

    while current > 1:
        current -= 1
        number *= current
    return number


# solution with for loop
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i

    return result


# solution with for math library
from math import factorial


def factorial(n):
    return math.factorial(n)


# solution without loops but with "funkcja rekurencyjna == recursive function"
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)


def factorial(n):
    return 1 if n <= 0 else n * factorial(n - 1)


#########################################################################################################
##################################            83            #############################################
#########################################################################################################

"""
Description:
Remove n exclamation marks in the sentence from left to right. n is positive integer.

Examples
remove("Hi!",1) === "Hi"
remove("Hi!",100) === "Hi"
remove("Hi!!!",1) === "Hi!!"
remove("Hi!!!",100) === "Hi"
remove("!Hi",1) === "Hi"
remove("!Hi!",1) === "Hi!"
remove("!Hi!",100) === "Hi"
remove("!!!Hi !!hi!!! !hi",1) === "!!Hi !!hi!!! !hi"
remove("!!!Hi !!hi!!! !hi",3) === "Hi !!hi!!! !hi"
remove("!!!Hi !!hi!!! !hi",5) === "Hi hi!!! !hi"
remove("!!!Hi !!hi!!! !hi",100) === "Hi hi hi"
"""
import unittest
import random


def remove(st, n):
    for _ in range(n):
        st = st.replace('!', '', 1)
    return st


def remove(st, n):
    return st.replace('!', '', n)


test_83 = {
    ("Hi!", 1): "Hi",
    ("Hi!", 100): "Hi",
    ("Hi!!!", 1): "Hi!!",
    ("Hi!!!", 100): "Hi",
    ("!Hi", 1): "Hi",
    ("!Hi!", 1): "Hi!",
    ("!Hi!", 100): "Hi",
    ("!!!Hi !!hi!!! !hi", 1): "!!Hi !!hi!!! !hi",
    ("!!!Hi !!hi!!! !hi", 3): "Hi !!hi!!! !hi",
    ("!!!Hi !!hi!!! !hi", 5): "Hi hi!!! !hi",
    ("!!!Hi !!hi!!! !hi", 100): "Hi hi hi",
}


def generate_random_remove():
    r_char = random.choice(['Hi', 'hi'])
    length = random.randint(1, 10)  # Ogranicz długość do testowalnych wartości
    j = [f"{'!' * random.randint(0, 5)}{r_char}{'!' * random.randint(0, 5)}" for _ in range(length)]
    st = ' '.join(j)
    n = random.randint(0, 20)
    expected = st
    for _ in range(n):  # Wykonaj tyle samo zamian, co w funkcji
        expected = expected.replace('!', '', 1)
    return st, n, expected


# class TestRemove(unittest.TestCase):
#     def test_remove(self):
#         for (st, n), expected in test_83.items():
#             with self.subTest(st=st, n=n, expected=expected):
#                 self.assertEqual(remove(st, n), expected)

#     def random_test_remove(self):
#         for _ in range(10):
#             st, n, expected = generate_random_remove()
#             with self.subTest(st=st, n=n, expected=expected):
#                 self.assertEqual(remove(st, n), expected)


# if __name__ == "__main__":
#     unittest.main()


#########################################################################################################
##################################            84            #############################################
#########################################################################################################

"""
Don Drumphet lives in a nice neighborhood, but one of his neighbors has started to let his house go.
Don Drumphet wants to build a wall between his house and his neighbor’s, and is trying to get the neighborhood association to pay for it.
He begins to solicit his neighbors to petition to get the association to build the wall. Unfortunately for Don Drumphet, he cannot read very well,
has a very limited attention span, and can only remember two letters from each of his neighbors’ names. As he collects signatures, he insists that
his neighbors keep truncating their names until two letters remain, and he can finally read them.

Your code will show Full name of the neighbor and the truncated version of the name as an array. If the number of the characters in name is less
than or equal to two, it will return an array containing only the name as is"
"""


def who_is_paying(name):
    if name == '':
        return ['']
    elif len(name) == 2 or len(name) == 1:
        return [name]
    else:
        return [name, name[0:2]]


#########################################################################################################
##################################            85            #############################################
#########################################################################################################

"""
Your function takes two arguments:

current father's age (years)
current age of his son (years)
Сalculate how many years ago the father was twice as old as his son (or in how many years he will be twice as old).
 The answer is always greater or equal to 0, no matter if it was in the past or it is in the future.
"""


# version 1
def twice_as_old(dad_years_old, son_years_old):
    dad_years_old -= 2 * son_years_old
    return dad_years_old * (-1) if dad_years_old < 0 else dad_years_old


# version 2
def twice_as_old(dad_years_old, son_years_old):
    return abs(dad_years_old - 2 * son_years_old)


test_85 = {
    (36, 7): 22,
    (55, 30): 5,
    (42, 21): 0,
    (22, 1): 20,
    (29, 0): 29,
    (50, 10): 30,
    (60, 25): 10,
}


def generate_random_test_85():
    son_years_old = random.randint(0, 60)
    dad_years_old = random.randint(son_years_old * 2, son_years_old * 3)
    expected = abs(dad_years_old - son_years_old * 2)
    return dad_years_old, son_years_old, expected


# class Test85(unittest.TestCase):
#     def test_85(self):
#         for (dad_years_old, son_years_old), expected in test_85.items():
#             with self.subTest(dad_years_old=dad_years_old, son_years_old=son_years_old, expected=expected):
#                 self.assertEqual(twice_as_old(dad_years_old, son_years_old), expected)


#     def random_test_85(self):
#         dad_years_old, son_years_old, expected = generate_random_test_85()
#         for _ in range(50):
#             with self.subTest(dad_years_old=dad_years_old, son_years_old=son_years_old, expected=expected):
#                 self.assertEqual(twice_as_old(dad_years_old, son_years_old), expected)


# if __name__ == '__main__':
#     unittest.main()


#########################################################################################################
##################################            86            #############################################
#########################################################################################################

"""Write a function that takes an array of strings as an argument and returns a sorted array containing the same strings, ordered from shortest to longest.

For example, if this array were passed as an argument:

["Telescopes", "Glasses", "Eyes", "Monocles"]

Your function would return the following array:

["Eyes", "Glasses", "Monocles", "Telescopes"]

All of the strings in the array passed to your function will be different lengths, so you will not have to decide how to order multiple strings of the same length."""


def sort_by_length(arr):
    return sorted(arr, key=len)


#########################################################################################################
##################################            87            #############################################
#########################################################################################################

"""
Given a string of digits, you should replace any digit below 5 with '0' and any digit 5 and above with '1'. Return the resulting string.

Note: input will never be an empty string
"""


# solution1
def fake_bin(x):
    result = ''
    for i in x:
        if int(i) < 5:
            result += '0'
        else:
            result += '1'
    return result


# solution 2
def fake_bin(x):
    return ''.join('0' if i < '5' else '1' for i in x)


test_87 = {
    '0123456789': '0000011111',
    '5132165131365':'1000011000011',
    '65156181161': '11011010010',
    '16516165461164164612': '01101011010010010100',
    '10000000000': '00000000000',
    '555555555555555': '111111111111111'
}

def generate_random_test_87():
    lenght = random.randint(0, 400)
    x = ''.join(str(random.randint(0, 9)) for _ in range(lenght))
    expected = ''.join('0' if i < 5 else '1' for i in x)
    return x, expected

# class Test87(unittest.TestCase):
#     def test_87(self):
#         for x, expected in test_87.items():
#             with self.subTest(input=x, expected=expected):
#                 self.assertEqual(fake_bin(x), expected)

#     def random_test_87(self):
#         for _ in range(50):
#             x, expected = generate_random_test_87()
#             with self.subTest(input=x, expected=expected):
#                 self.assertEqual(fake_bin(x), expected)

#########################################################################################################
##################################            88            #############################################
#########################################################################################################

"""
Write a method that takes one argument as name and then greets that name, capitalized and ends with an exclamation point.

Example:

"riley" --> "Hello Riley!"
"JACK"  --> "Hello Jack!"
"""

def greet(name):
    return f"Hello {name.capitalize()}!"

test_88 = {
    'jacek': 'Jacek',
    'ADAM': 'Adam',
    'BiLlY': 'Billy',
    'MaŁGoRZata': 'Małgorzata',
    'gFHDFJjdgfhj': 'Gfhdfjjdgfhj',
    '': '',
}

def generate_random_test_88():
    length = random.randint(0, 100)
    characters = string.ascii_letters
    name = ''.join(random.choices(characters, k=length))
    expected = f"Hello {name.capitalize()}!"
    return name, expected

class Test88(unittest.TestCase):
    def test_88(self):
        for name, expected_name in test_88.items():
            expected = f"Hello {expected_name}!"
            with self.subTest(input=name, expected=expected):
                self.assertEqual(greet(name), expected)

    def random_test_88(self):
        for _ in range(50):
            name, expected = generate_random_test_88()
            with self.subTest(input=name, expected=expected):
                self.assertEqual(greet(name), expected)



#########################################################################################################
##################################            89            #############################################
#########################################################################################################

"""
Story
Your online store likes to give out coupons for special occasions. Some customers try to cheat the system by entering invalid codes or using expired coupons.

Task
Your mission:
Write a function called checkCoupon which verifies that a coupon code is valid and not expired.

A coupon is no more valid on the day AFTER the expiration date. All dates will be passed as strings in this format: "MONTH DATE, YEAR".

"""

from datetime import datetime


def validation_date(func):
    def wrapper(*args):
        data = list(args)
        expiration_date = datetime.strptime(data.pop(), "%B %d, %Y")
        current_date = datetime.strptime(data.pop(), "%B %d, %Y")
        is_valid = current_date <= expiration_date
        return func(entered_code = data[0], correct_code = data[1], is_valid = is_valid)
    return wrapper



@validation_date
def check_coupon(*, entered_code: str, correct_code: str, is_valid: bool) -> bool:
    return entered_code is correct_code and is_valid


