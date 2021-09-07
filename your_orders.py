# Your task is to sort a given string. Each word in the string will contain a single number. This number is # # the position the word should have in the result.

# E.g.
# "is2 Thi1s T4est 3a" --> "Thi1s is2 3a T4est"

def your_order(string):
    orig_string = string.split(' ')
    new_string = []
    for s in orig_string:
        for c in s:
            if c.isnumeric():
                new_string.insert(int(c)-1, s)
    return new_string

def your_order2(string):
    orig_string = string.split(' ')
    new_string = {}
    for s in orig_string:
        for c in s:
            if c.isnumeric():
                new_string[c] = s
    for i in sorted(new_string.keys()):
        print(new_string[i], end=' ')

def your_order3(string):
    orig_string = string.split()
    new_order = {}
    for s in orig_string:
        for c in s:
            if c.isnumeric():
                new_order[c] = s
    new_string = [new_order[key] for key in sorted(new_order.keys())]
    return ' '.join(new_string)


def order(sentence):
    return " ".join(sorted(sentence.split(), key=lambda x: int(filter(str.isdigit, x))))

string = "is2 Thi1s T4est 3a"
string2 = "4of Fo1r pe6ople g3ood th5e the2"
string3 = ''
print(your_order3(string2))
# print(order(string2))