# Your task is to make function, which returns the sum of a sequence of integers.

# The sequence is defined by 3 non-negative values: begin, end, step.

# If begin value is greater than the end, function should returns 0

# Examples

# sequenceSum(2,2,2) === 2
# sequenceSum(2,6,2) === 12 // 2 + 4 + 6
# sequenceSum(1,5,1) === 15 // 1 + 2 + 3 + 4 + 5
# sequenceSum(1,5,3) === 5 // 1 + 4

def sequence_sum(begin, end, step):
    sum = 0
    for i in range(begin, end+1, step):
        sum += i
    return sum

def sequence_sum2(begin, end, step):
    return sum([i for i in range(begin, end+1, step)])

def sequence_sum3(begin, end, step):
    return sum(range(begin, end+1, step))

print(sequence_sum3(2, 6, 2))