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
        return 'small'
    else:
        return 'wide'


# solution 2
def mouth_size(animal):
    return 'small' if animal.lower() == "alligator" else 'wide'


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

    def __str__(self): return "Fighter({}, {}, {})".format(self.name, self.health, self.damage_per_attack)

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
    return ''.join(x for x in s if not x.isdigit())


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
    mistakes = {'5': 'S', '0': 'O', '1': 'I'}

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

#XDD
# second solution
def is_palindrome(s):
    s = s.lower()
    middle_index = len(s) // 2
    return s[:middle_index] == s[middle_index:][::-1] if len(s) % 2 == 0 else s[:middle_index] == s[middle_index + 1:][::-1]

#XD
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
    return f"Hello, World!" if name == '' or name == None else f"Hello, {name.lower().capitalize()}!"

# second solution
def hello(name=''):
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


