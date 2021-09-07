# The main idea is to count all the occurring characters in a string. If you have a string like aba, then the result should be {'a': 2, 'b': 1}.

# What if the string is empty? Then the result should be empty object literal, {}.

def count(string):    # The function code should be here
    num = {}
    for char in string:
        num[char] = string.count(char)
    return num

def count2(string):
    return {char: string.count(char) for char in string}

def count3(string):
    return {} if not string else {char: string.count(char) for char in string}

s = 'aba'
s2 = ''
print(count(s))
print(count2(s))
print(count3(s2))
