"""
Keyword Cipher Helper

A keyword cipher is a monoalphabetic cipher which uses a "keyword" to provide encryption. It is somewhat similar to a Caesar cipher.

In a keyword cipher, repeats of letters in the keyword are removed and the alphabet is reordered such that the letters in the keyword appear first, followed by the rest of the letters in the alphabet in their otherwise usual order.

E.g. for an uppercase latin alphabet with keyword of "KEYWORD":

A|B|C|D|E|F|G|H|I|J|K|L|M|N|O|P|Q|R|S|T|U|V|W|X|Y|Z

becomes:

K|E|Y|W|O|R|D|A|B|C|F|G|H|I|J|L|M|N|P|Q|S|T|U|V|X|Z

such that:

cipher.encode('ABCHIJ') == 'KEYABC'
cipher.decode('KEYABC') == 'ABCHIJ'
All letters in the keyword will also be in the alphabet. For the purpose of this kata, only the first occurence of a letter in a keyword should be used. Any characters not provided in the alphabet should be left in situ when encoding or decoding.

jacobb
https://www.codewars.com/kata/535c1c80cdbf5011e600030f/train/python
"""


class keyword_cipher(object):
    def __init__(self, abc, keyword):
        kw = "".join(dict.fromkeys(keyword))

        self.abc = abc
        self.cipher = kw + ''.join(c for c in abc if c not in kw)
        self.e = str.maketrans(abc, self.cipher)
        self.d = str.maketrans(self.cipher, abc)

    def encode(self, plain):
        return plain.translate(self.e)

    def decode(self, ciphered):
        return ciphered.translate(self.d)
