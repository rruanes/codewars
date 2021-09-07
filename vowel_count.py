# Return the number (count) of vowels in the given string.
# We will consider a, e, i, o, u as vowels for this Kata (but not y).
# The input string will only consist of lower case letters and/or spaces.

def getCount(sentence):
    vowel_count = {char: sentence.count(char) for char in sentence if char in 'aeiou'}
    return sum(vowel_count.values())

print(getCount('Should count all vowels'))