"""
Build a Simple Spellchecker

Task
Inputs: (1) A string representing a piece of text to be spellchecked. (2) A list or array of single words. These words are (assumed to be) correctly spelled. Any word in the text that is not in the list is a misspelling.

Output: A dictionary of all misspelled words, each with a list of possible corrections. The corrections for each misspelled word are the words in the list "nearest" to it, as defined in the "Details" section below.

Example: If text = "The students were thriled to recive ther diplomas.", and
word_list = ["to", "the", "were", "there", "their", "recite", "receive", "students", "thrilled", "diplomas"],
the spellchecker should return {"thriled": ["thrilled"], {"recive": ["receive", "recite"]}, {"ther": ["the", "their", "there"]}.

Although people can tell from context that "recive" should be replaced by "receive" rather than "recite", this simple spellchecker cannot. All it knows is that "receive" and "recite" are the words nearest to "recive" in the word-list. Similarly, "the","their"and "there"are the nearest words to "ther".

Details
(1) Each word in the word-list is a non-empty string containing lower-case letters. Any character besides the first and last can also be an apostrophe or hyphen. (Apostrophes and hyphens occur in English words, like "don't, "able-bodied".)

(2) Each word in the text is a non-empty string containing at least one letter. Any character besides the first and last can also be punctuation ("internal punctuation"). Internal punctuation that results in a misspelling should be corrected. There is at least 1 whitespace character between words.

(3) The corrections for each misspelled word are the words in the list within edit distance 1 of it. If there are none, its corrections are at edit distance 2. If there are also no corrections at edit distance 2, the list of corrections is the empty list. See the "Edit Distance" section below for the precise definition of edit distance 1 and 2.

(4) Each word in the word-list is lowercase, but corrections should take case into account. Characters in a misspelled word that are in the correct position preserve their case. Incorrect characters should be corrected to be lowercase, unless the misspelled word is entirely uppercase (i.e. all letters are uppercase - the case of internal punctuation is irrelevant) and of length > 1. For strings of length 1, keep the case of the first character, whether correct or not.

Example: If text = "We CANOT belieVe 'Th$IS'. E woNT'!! and
word_list = ["we", "can't", "this", "well", "won't", "cannot", "believe"],
the checker should return {"CANOT": ["CAN'T", "CANNOT"], "Th$IS": ["This"], "E": ["We"], "woNT": ["woN't"]}.

Explanation:

"CANOT" is a misspelling of "can't" or "cannot". It's an uppercase string of length greater than 1, so the corrections should be entirely uppercase: "CAN'T", "CANNOT".
"Th$IS" is a misspelling of "this". The first 2 letters are correct and preserve case. Both "$" and "I" are wrong, so should be corrected to the correct character in lowercase. The correction is "This".
"E" is a misspelling of "we". It's an uppercase string, but since it's length 1, we keep the case of the first character, but we don't know that the rest of the string should be uppercase. So the correction is "We" rather than "WE" or "we".
woNT'!! deserves close attention. The misspelled word ends at 'T', because "'!!" is "external" punctuation. The ' is NOT part of the misspelling. The first 3 characters are correct and preserve case. The 'T' is wrong and is corrected to '. The correction is "woN't".

(5) Each list of corrections should be lexicographically sorted. This is why ["receive", "recite"] appears instead of ["recite", "receive"]in the first example.

(6) No duplicate strings should appear in any list of corrections.

Edit Distance
In this kata, the words whose edit distance is 1 from a given word are those that result from doing one of the following operations: deleting a single character, inserting a single character, replacing a single character by a different character, or transposing a pair of adjacent characters. Edit distance 2 refers to doing two of those operations. In this kata edit distance calculations ignore case.

Examples:

The following are at edit distance 1 from "hello":
"helo" (delete 'l')
"Heello" (insert 'e')
"helpo" (replace 'l' by 'p')
"hlelO" (transpose 'l' and 'e')

The following are at edit distance 2 from "hello":
"helP" (delete 'l', then replace 'o' with 'p')
"elhlo" (transpose 'h' and 'e', then transpose 'h' and 'l')
"MELLOW" (replace 'h' with 'm', then insert 'w')
"shelol" (insert 's', then transpose 'l' and 'o')

This corresponds to Damerau–Levenshtein Distance. It is NOT the same definition as used in the Levenshtein Distance kata.

Constraints: Number of words in the text ≤ 250. Number of words in the word-list ≤ 250.

Enjoy correctign yore speling!

brodiemark
https://www.codewars.com/kata/68192cd301fbd97e7191f876/train/python
"""
import re

def correct_spelling(text, word_list):
    word_set = set(word_list)
    words = text.split()
    result = {}

    for original_word in words:
        core, prefix, suffix = extract_core_word(original_word)

        if not core:
            continue

        lower_core = core.lower()

        if lower_core in word_set:
            continue

        corrections = find_corrections(lower_core, word_list)
        corrected_forms = [apply_case(core, c) for c in corrections]
        corrected_forms = sorted(set(corrected_forms))

        result[core] = corrected_forms

    return result


def extract_core_word(word):
    prefix = re.match(r"^[^A-Za-z]*", word).group()
    suffix = re.match(r".*?([^A-Za-z]*)$", word).group(1)
    core = word[len(prefix):len(word)-len(suffix)]
    return core, prefix, suffix


# --- pełny Damerau–Levenshtein (nie restricted / OSA) ---
def edit_distance(a, b):
    a = a.lower()
    b = b.lower()
    len1, len2 = len(a), len(b)
    maxdist = len1 + len2

    # macierz (len1+2) x (len2+2)
    d = [[0] * (len2 + 2) for _ in range(len1 + 2)]
    d[0][0] = maxdist
    for i in range(len1 + 1):
        d[i + 1][0] = maxdist
        d[i + 1][1] = i
    for j in range(len2 + 1):
        d[0][j + 1] = maxdist
        d[1][j + 1] = j

    da = {}
    for ch in set(a + b):
        da[ch] = 0

    for i in range(1, len1 + 1):
        db = 0
        for j in range(1, len2 + 1):
            i1 = da[b[j - 1]]
            j1 = db
            cost = 0 if a[i - 1] == b[j - 1] else 1
            if cost == 0:
                db = j

            d[i + 1][j + 1] = min(
                d[i][j] + cost,          # subst
                d[i + 1][j] + 1,         # insert
                d[i][j + 1] + 1,         # delete
                d[i1][j1] + (i - i1 - 1) + 1 + (j - j1 - 1)  # transpo (pełne DL)
            )
        da[a[i - 1]] = i

    return d[len1 + 1][len2 + 1]


def find_corrections(word, word_list):
    dist1 = []
    dist2 = []

    for w in word_list:
        d = edit_distance(word, w)
        if d == 1:
            dist1.append(w)
        elif d == 2:
            dist2.append(w)

    return dist1 if dist1 else dist2


def apply_case(misspelled, correct):
    # całe UPPER i długość > 1 → całe UPPER
    if len(misspelled) > 1 and misspelled.isupper():
        return correct.upper()

    # długość 1 → zachowaj case pierwszego znaku
    if len(misspelled) == 1:
        if misspelled.isupper():
            return correct.capitalize()
        else:
            return correct.lower()

    # mieszany case: poprawne znaki zachowują case, reszta lowercase
    res = []
    for i, c in enumerate(correct):
        if i < len(misspelled) and misspelled[i].lower() == c.lower():
            res.append(misspelled[i])
        else:
            res.append(c.lower())
    return "".join(res)