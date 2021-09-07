# Complete the solution so that it reverses all of the words within the string passed in.

# Example:

# "The greatest victory is that which requires no battle" --> "battle no requires which that is victory greatest The"

def reverse_words(s: str) -> str:
    return ' '.join(s.split()[::-1])

def reverse_words2(s: str) -> str:
    return ' '.join(reversed(s.split()))

s = "The greatest victory is that which requires no battle"

print(reverse_words(s))
print(reverse_words2(s))