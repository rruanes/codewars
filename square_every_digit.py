# Welcome. In this kata, you are asked to square every digit of a number and concatenate them.

# For example, if we run 9119 through the function, 811181 will come out, because 92 is 81 and 12 is 1.

# Note: The function accepts an integer and returns an integer

def square_digits(num):
    square = ''
    for d in str(num):
        square += str(int(d)**2)
    return int(square)

def square_digits2(num):
    return int(''.join([str(int(d)**2) for d in str(num)]))

print(square_digits(1234))
print(square_digits2(1234))