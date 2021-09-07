# The goal of this exercise is to convert a string to a new string where each character in the new string is "(" if that character appears only once in the original string, or ")" if that character appears more than once in the original string. Ignore capitalization when determining if a character is a duplicate.

# Examples
# "din"      =>  "((("
# "recede"   =>  "()()()"
# "Success"  =>  ")())())"
# "(( @"     =>  "))((" 

from collections import Counter

def duplicate_encode(word: str) -> str:
    counts = Counter(word.lower())
    new_word = list(word.lower())
    new = []
    for char in new_word:
        if counts[char] == 1:
            new.append('(')
        else:
            new.append(')')
    return ''.join(new)

def duplicate_encode2(word: str) -> str:
    counts = Counter(word.lower())
    new_word = ['(' if counts[char] == 1 else ')' for char in word.lower()]
    return ''.join(new_word)

# 
print(duplicate_encode('CLarOY)tXjK@RMWtuhiS'), '((()((()(((()(()((((')
print(duplicate_encode2('CLarOY)tXjK@RMWtuhiS'), '((()((()(((()(()((((')