def number(bus_stops):
    remaining = 0
    for stops in bus_stops:
        remaining += stops[0]
        remaining -= stops[1]
    return remaining

def number2(bus_stops):
    return sum(stop[0] - stop[1] for stop in bus_stops)

def number3(bus_stops):
    return sum(get_in - get_off for get_in, get_off in bus_stops)

test1 = [[10,0],[3,5],[5,8]]
# print(number(test1))
# print(number2(test1))
print(number3(test1))