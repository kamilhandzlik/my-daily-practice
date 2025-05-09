"""
Encrypt this!
Acknowledgments:
I thank yvonne-liu for the idea and for the example tests :)

Description:
Encrypt this!

You want to create secret messages which can be deciphered by the Decipher this! kata. Here are the conditions:

Your message is a string containing space separated words.
You need to encrypt each word in the message using the following rules:
The first letter must be converted to its ASCII code.
The second letter must be switched with the last letter
Keepin' it simple: There are no special characters in the input.
Examples:
encrypt_this("Hello") == "72olle"
encrypt_this("good") == "103doo"
encrypt_this("hello world") == "104olle 119drlo"

Decipher this!
Description:
You are given a secret message you need to decipher. Here are the things you need to know to decipher it:

For each word:

the second and the last letter is switched (e.g. Hello becomes Holle)
the first letter is replaced by its character code (e.g. H becomes 72)
there are no special characters used, only letters and spaces
words are separated by a single space
there are no leading or trailing spaces
Examples

'72olle 103doo 100ya' --> 'Hello good day'
'82yade 115te 103o'   --> 'Ready set go'
"""
############################
###### ENCRYPT PART ########
############################


# First solution that came to my mind
def encrypt_this(text):
    if not text:
        return ''
    words = text.split(' ')
    encrypted = []

    for word in words:
        if len(word) == 1:
            encrypted_word = str(ord(word[0]))
        elif len(word) == 2:
            encrypted_word = str(ord(word[0])) + word[1]
        else:
            encrypted_word = (
                    str(ord(word[0])) +
                    word[-1:] +
                    word[2:-1] +
                    word[1]
            )
        encrypted.append(encrypted_word)
    return ' '.join(encrypted)

 # Slightly optimized solution
def encrypt_this(text):
    def encrypt_word(word):
        if not word:
            return ''
        first = str(ord(word[0]))
        if len(word) == 1:
            return first
        if len(word) == 2:
            return first + word[1]
        return first + word[-1] + word[2:-1] +word[1]
    return ' '.join(encrypt_word(word) for word in text.split(' '))

"""
Regex version - warning may not work properly (\w?) as second and (\w?) as last letter may pull each other together.
Moreover Lazy matching *? may catch not what is required especially if len(word) == 3 
"""
# import re
# def encrypt_this(text):
#     return re.sub(r'\b(\w)(\w?)(\w*?)(\w?)\b', lambda m: f'{str(ord(m.group(1))) + m.group(4) + m.group(3) + m.group(2)}', text).replace('   ', ' ').replace('  ', ' ')

############################
###### DECIPHER PART #######
############################

def decipher_this(s):
    def encrypt_word(word):
        if not word:
            return ''
        ascii_part = ''
        letters_part = ''
        for i in word:
            if i.isdigit():
                ascii_part += i
            else:
                letters_part += i

        first = str(chr(int(ascii_part)))
        new_word = first + letters_part
        if len(new_word) == 1:
            return first
        if len(new_word) == 2:
            return first + new_word[1]
        return first + new_word[-1] + new_word[2:-1] + new_word[1]
    return ' '.join(encrypt_word(word) for word in s.split(' '))


import re

def decipher_this(s):
    def decrypt_word(word):
        match = re.match(r'(\d+)(\w*)', word)
        if not match:
            return word
        ascii_code, rest = match.groups()
        first = chr(int(ascii_code))

        if len(rest) < 2:
            return first + rest
        return first + rest[-1] + rest[1:-1] + rest[0]

    return ' '.join(decrypt_word(word) for word in s.split())


print(encrypt_this("A wise old owl lived in an oak"))
print(decipher_this("65 119esi 111dl 111lw 108dvei 105n 97n 111ka"))