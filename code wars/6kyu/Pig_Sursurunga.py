"""
Pig Sursurunga

Once upon a time, a CodeWarrior, after reading a discussion on what can be the plural, took a look at this page and discovered that more than 1 "kind of plural" may exist.

For example Sursurunga Language distinguishes 5 types of numbers: singular (1 thing), dual (2 things), 'trial' or 'lesser paucal' (3 or 4), 'greater paucal' (more than 4) and plural (many).

In this kata, you'll have to handle only four types of numbers:

singular: 0 or 1 thing
dual: 2 things
paucal: 3 to 9 things
plural: more than 9 things
To add some flavor the number-marker will not be added in same places:

singular, no marker : 1 cat
dual, prefixed "bu" : 2 cats -> 2 bucat
paucal, suffixed "zo" : 4 cats -> 4 catzo
plural, "circumfixed ga" : 100 cats -> 100 gacatga
As you all ("hawk eyes") have seen, the final s of english plural disappears.

( btw these markers, of course, have absolutely nothing to do with true sursurunga language, we're just talking about "pig-sursurunga" with pig as pig in "pig latin" )

Your Job . . .
. . . if you accept it, will be to write a function which get a string as argument and returns this string with words in it eventually converted to their "pig-sursurunga number type".

If a number ( ie 1 or more digit ) + a space + a word ( letters ) are found then the word should be converted.

Each group of number+space+word found in the string should be evaluated.

Examples :
"1 tiger" --> "1 tiger" (singular, nothing to change)

"2 tigers" --> "2 butiger" (dual)
"3 tigers" --> "3 tigerzo" (paucal)
"13 tigers" --> "13 gatigerga" (plural)

"5 lions and 15 zebras" --> "5 lionzo and 15 gazebraga" (paucal and plural)
You may assume at least 1 number+space+word group will be provided.

Beware s of english plural should be removed, not ending s of some singular words ( eg "kiss" )

"7 kisses" --> "7 kissezo"
"1 kiss" --> "1 kiss"
Good luck!
"""


# This works with normal sentences like 6 tails  of owl and 1 wing  of owl and 94 ears  of rat etc BUT!
# this kata also has to incorporate bullshit like this '\n3 pigs\nmet 1 wolf\n2 days ago' so solution below is uselles here so lets go for another one
def sursurungal(txt):
    text = txt.split(' ')

    for i, j in enumerate(text):
        if j.isnumeric():
            if j == '0' or j == '1':
                text[i + 1] = f"{text[i + 1]}"
            elif j == '2':
                text[
                    i + 1] = f"{'bu' + text[i + 1][0:-1] if text[i + 1][-1] == 's' else 'bu' + text[i + 1]}"
            elif int(j) <= 9:
                text[
                    i + 1] = f"{text[i + 1][0:-1] + 'zo' if text[i + 1][-1] == 's' else 'bu' + text[i + 1] + 'zo'}"
            else:
                text[
                    i + 1] = f"{'ga' + text[i + 1][0:-1] + 'ga' if text[i + 1][-1] == 's' else 'ga' + text[i + 1] + 'ga'}"

    return " ".join(text)


# Solution 1
import re


def sursurungal(txt):
    def replacer(match):
        num = int(match.group(1))
        word = match.group(2)

        if num in (0, 1):
            return f"{num} {word}"
        elif num == 2:
            if word.endswith('s') and not word.endswith('ss'):
                word = word[:-1]
            return f"{num} bu{word}"
        elif 3 <= num <= 9:
            if word.endswith('s') and not word.endswith('ss'):
                word = word[:-1]
            return f"{num} {word}zo"
        else:
            if word.endswith('s') and not word.endswith('ss'):
                word = word[:-1]
            return f"{num} ga{word}ga"

    return re.sub(r"(\d+)\s+([a-zA-Z]+)", replacer, txt)


# Solution 2
import re


def sursurungal(txt):
    txt = re.sub(r'\b2\s(\S+)s', r'2 bu\1', txt)
    txt = re.sub(r'\b([3-9])\s(\S+)s', r'\1 \2zo', txt)
    return re.sub(r'(\d+\d)\s(\S+)s', r'\1 ga\2ga', txt)


print(sursurungal("2 bananas"))
print(sursurungal('4 kisses'))
print(sursurungal('6 tails  of owl and 1 wing  of owl and 94 ears  of rat and 94 ears  of rat'))
print(sursurungal('\n3 pigs\nmet 1 wolf\n2 days ago'))
