# Step 1: Create a function called encode() to replace all the lowercase vowels in a given string with numbers according to the following pattern:

# a -> 1
# e -> 2
# i -> 3
# o -> 4
# u -> 5
# For example, encode("hello") would return "h2ll4". There is no need to worry about uppercase vowels in this kata.
# Step 2: Now create a function called decode() to turn the numbers back into vowels according to the same pattern shown above.
# For example, decode("h3 th2r2") would return "hi there".

# For the sake of simplicity, you can assume that any numbers passed into the function will correspond to vowels.

def encode(st):
    vowels = list('aeiou')
    msg = list(st)
    for i, c in enumerate(msg):
        if c in vowels:
            msg.pop(i)
            msg.insert(i, str(vowels.index(c)+1))
    return ''.join(msg)
    
def decode(st):
    vowels = list('aeiou')
    numbers = list('12345')
    msg = list(st)
    for i, c in enumerate(msg):
        if c in numbers:
            msg.pop(i)
            msg.insert(i, vowels[numbers.index(c)])
    return ''.join(msg)

print(encode('hi there'))
print(decode('h3 th2r2'))