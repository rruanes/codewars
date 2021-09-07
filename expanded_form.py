# Write Number in Expanded Form
# You will be given a number and you will need to return it as a string in Expanded Form. For example:

# expanded_form(12) # Should return '10 + 2'
# expanded_form(42) # Should return '40 + 2'
# expanded_form(70304) # Should return '70000 + 300 + 4'
# NOTE: All numbers will be whole numbers greater than 0.

def expanded_form(num):
    pos = list(str(num))
    pos.reverse()
    val = [int(n) * (10**i) for i, n in enumerate(pos)]
    val.reverse()
    expanded = [str(j) for j in val if j != 0]
    return ' + '.join(expanded)

def expanded_form2(num):
    pos = list(str(num))
    # pos.reverse()
    val = [int(n)* (10**i) for i, n in enumerate(pos)]
    # val.reverse()
    expanded = [str(j) for j in val if j != 0]
    return ' + '.join(expanded)

print(expanded_form(4982342))