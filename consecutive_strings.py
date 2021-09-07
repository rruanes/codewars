# You are given an array(list) strarr of strings and an integer k. Your task is to return the first longest string consisting of k consecutive strings taken in the array.

# Examples:
# strarr = ["tree", "foling", "trashy", "blue", "abcdef", "uvwxyz"], k = 2

# Concatenate the consecutive strings of strarr by 2, we get:

# treefoling   (length 10)  concatenation of strarr[0] and strarr[1]
# folingtrashy ("      12)  concatenation of strarr[1] and strarr[2]
# trashyblue   ("      10)  concatenation of strarr[2] and strarr[3]
# blueabcdef   ("      10)  concatenation of strarr[3] and strarr[4]
# abcdefuvwxyz ("      12)  concatenation of strarr[4] and strarr[5]

# Two strings are the longest: "folingtrashy" and "abcdefuvwxyz".
# The first that came is "folingtrashy" so 
# longest_consec(strarr, 2) should return "folingtrashy".

# In the same way:
# longest_consec(["zone", "abigail", "theta", "form", "libe", "zas", "theta", "abigail"], 2) --> "abigailtheta"
# n being the length of the string array, if n = 0 or k > n or k <= 0 return "".

# Note
# consecutive strings : follow one after another without an interruption


def longest_consec(strarr, k):
    combos, length = [], []
    for i in range(len(strarr)-(k-1)):
        concat = strarr[i] + strarr[i+1]
        combos.append(concat)
        length.append(len(concat))
    return combos[length.index(max(length))]

def longest_consec2(strarr, k):
    if len(strarr) == 0 or k > len(strarr) or k <= 0:
        return ''
    else:
        combos = []
        for i in range(len(strarr)-(k-1)):
            concat = ''
            for j in range(k):
                concat += strarr[i+j]
            combos.append(concat)
    return max(combos, key=len)

def longest_consec3(strarr, k):
    if len(strarr) == 0 or k > len(strarr) or k <= 0:
        return ''
    else:
        combos = []
        for i in range(len(strarr)-(k-1)):
            concat = ''.join(strarr[i:i+k])
            combos.append(concat)
    return max(combos, key=len)

def longest_consec4(strarr, k):
    if len(strarr) == 0 or k > len(strarr) or k <= 0:
        return ''
    else:
        combos = [''.join(strarr[i:i+k]) for i in range(len(strarr)-(k-1))]
    return max(combos, key=len)

def longest_consec5(strarr, k):
    if len(strarr) == 0 or k > len(strarr) or k <= 0:
        return ''
    else:
        return max([''.join(strarr[i:i+k]) for i in range(len(strarr)-(k-1))], key=len)

print(longest_consec4(["tree", "foling", "trashy", "blue", "abcdef", "uvwxyz"], 2))
print(longest_consec5(["zone", "abigail", "theta", "form", "libe", "zas", "theta", "abigail"], 2))
